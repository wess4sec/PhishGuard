import tldextract
import urllib.parse


SUSPICIOUS_TLDS = ["zip", "mov", "xyz", "top", "ru", "cn"]


class URLAnalyzer:

    def analyze(self, url: str) -> dict:
        parsed = urllib.parse.urlparse(url)
        extracted = tldextract.extract(url)

        domain = extracted.domain
        suffix = extracted.suffix
        subdomain = extracted.subdomain

        full_domain = f"{domain}.{suffix}" if suffix else domain

        flags = []

        # 🔴 Nested domain attack
        if full_domain not in url:
            flags.append("possible_nested_domain")

        # 🔴 Excessive subdomains
        if subdomain and subdomain.count(".") >= 2:
            flags.append("excessive_subdomains")

        # 🔴 IP-based URL
        if parsed.hostname and parsed.hostname.replace(".", "").isdigit():
            flags.append("ip_based_url")

        # 🔴 Suspicious TLD
        if suffix in SUSPICIOUS_TLDS:
            flags.append("suspicious_tld")

        return {
            "url": url,
            "domain": domain,
            "registered_domain": full_domain,
            "subdomain": subdomain,
            "path": parsed.path,
            "flags": flags
        }