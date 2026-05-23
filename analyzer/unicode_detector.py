import idna
import unicodedata


class UnicodeDetector:

    def is_homograph(self, domain: str) -> dict:
        result = {
            "is_homograph": False,
            "reason": []
        }

        # 🔴 Punycode detection
        if "xn--" in domain:
            result["is_homograph"] = True
            result["reason"].append("punycode_detected")

        # 🔴 Mixed script detection
        for char in domain:
            if unicodedata.category(char).startswith("L"):
                if ord(char) > 127:
                    result["is_homograph"] = True
                    result["reason"].append("unicode_character_detected")
                    break

        return result