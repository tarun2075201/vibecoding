import re

def test_regex(pattern, test_str):
    try:
        matches = re.findall(pattern, test_str)
        return {"matches": matches}
    except re.error as e:
        return {"error": str(e)}
