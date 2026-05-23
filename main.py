from analyzer.url_analyzer import URLAnalyzer
from analyzer.unicode_detector import UnicodeDetector
from analyzer.brand_detector import BrandDetector
from analyzer.risk_scoring import RiskScorer


def run(url: str):

    url_analyzer = URLAnalyzer()
    unicode_detector = UnicodeDetector()
    brand_detector = BrandDetector()
    scorer = RiskScorer()

    url_data = url_analyzer.analyze(url)

    unicode_data = unicode_detector.is_homograph(url_data["domain"])

    brand_data = brand_detector.match_brand(url_data["domain"])

    risk = scorer.calculate(
        url_data["flags"],
        unicode_data,
        brand_data
    )

    return {
        "input": url,
        "url_analysis": url_data,
        "unicode_analysis": unicode_data,
        "brand_analysis": brand_data,
        "risk": risk
    }


if __name__ == "__main__":
    test_url = "google.com.evil.ru"
    result = run(test_url)

    import json
    print(json.dumps(result, indent=4))