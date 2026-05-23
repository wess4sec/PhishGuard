import email


class HeaderAnalyzer:

    def analyze(self, raw_headers: str) -> dict:

        msg = email.message_from_string(raw_headers)

        results = {
            "spf": "unknown",
            "dkim": "unknown",
            "dmarc": "unknown",
            "flags": []
        }

        # Simple keyword-based detection (starter logic)
        headers = raw_headers.lower()

        if "spf=fail" in headers:
            results["spf"] = "fail"
            results["flags"].append("spf_failed")

        if "dkim=fail" in headers:
            results["dkim"] = "fail"
            results["flags"].append("dkim_failed")

        if "dmarc=fail" in headers:
            results["dmarc"] = "fail"
            results["flags"].append("dmarc_failed")

        if "reply-to" in headers and "from" in headers:
            results["flags"].append("possible_spoofing")

        return results