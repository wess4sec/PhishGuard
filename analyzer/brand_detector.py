from difflib import SequenceMatcher


BRANDS = [
    "google",
    "microsoft",
    "paypal",
    "github",
    "amazon",
    "linkedin"
]


class BrandDetector:

    def match_brand(self, domain: str) -> dict:
        matches = []

        for brand in BRANDS:
            similarity = SequenceMatcher(None, domain.lower(), brand).ratio()

            if brand in domain.lower():
                matches.append({
                    "brand": brand,
                    "type": "keyword_match",
                    "severity": "high"
                })

            elif similarity > 0.85:
                matches.append({
                    "brand": brand,
                    "type": "fuzzy_match",
                    "similarity": similarity,
                    "severity": "medium"
                })

        return {
            "matches": matches
        }