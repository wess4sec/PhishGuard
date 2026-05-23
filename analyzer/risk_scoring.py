class RiskScorer:

    def calculate(self, url_flags, unicode_data, brand_data) -> dict:

        score = 0
        reasons = []

        # URL signals
        if "possible_nested_domain" in url_flags:
            score += 25
            reasons.append("nested_domain")

        if "excessive_subdomains" in url_flags:
            score += 15
            reasons.append("excessive_subdomains")

        if "suspicious_tld" in url_flags:
            score += 20
            reasons.append("suspicious_tld")

        # Unicode signals
        if unicode_data.get("is_homograph"):
            score += 40
            reasons.append("unicode_homograph")

        # Brand signals
        if brand_data.get("matches"):
            score += 30
            reasons.append("brand_impersonation")

        # Classification
        if score >= 80:
            level = "CRITICAL"
        elif score >= 60:
            level = "HIGH"
        elif score >= 30:
            level = "MEDIUM"
        else:
            level = "LOW"

        return {
            "score": score,
            "level": level,
            "reasons": reasons
        }