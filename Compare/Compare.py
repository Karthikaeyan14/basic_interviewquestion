"""def compare(expected,actual):
    if expected==actual:
        return "Pass"
    return "Fail"

print(compare(11,10))
print(compare("string","string"))
print(compare("100.3","100.4"))

def compare_text(expected,actual):
    if expected.upper().split()==actual.upper().split():
        return True
    return False


print(compare_text("OK"," ok"))"""
def compare_dict(actual,expected):
    if expected.values()!=actual.values():
        print(expected.values())






expected = {"status": 200, "name": "Rahul", "role": "admin"}
actual   = {"status": 200, "name": "Rahul", "role": "user"}
compare_dict(actual, expected)