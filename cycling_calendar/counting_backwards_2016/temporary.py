import re
"""
string1 = "15 km"
string2 = "\n16 x 30/50s\n34.2 km"
string3 = "45 min - 14,9 km"

pattern = re.compile(r'(\d+)[\.?\,?]?\d+?\s?[k]')
pattern2 = '\d+[\.?\,?]?\d+?\s?[kK]'
pattern3 = "(\d+)['.'?','?]?\d+?\s?[kK]"

a = re.search(pattern2, string3).group()
print(a, "search")
a = re.sub(",", ".", a)
print(a, "sub")
index = a.find("k")
print(index, "index k")
a = a[:index]
print(a, "bez k")
print(a[4])
print(len(a))
a = a.strip()
print(len(a))
print(a)

b = float(a)
print(b)
print(type(b))
"""
events = [
    {"summary": "HIIT na rotopedu", "description": "\n16 x 30/50s\n34.2 km"},
    {"summary": "posilovna", "description": None},
    {"summary": "rotoped", "description": "45 min - 14,9 km"},
    {"summary": "rotoped", "description": "15 km"}
]

initial_sum = 300
# function for processing inputs
def count_kms(iterable):
    part_count = 0
    pattern = '\d+[\.?\,?]?\d+?\s?[kK]'
    for item in iterable:
        if "rotoped" in item["summary"]:
            comment_string = re.sub(",", ".", item["description"])
            kms = re.search(pattern, comment_string).group().lower()
            kms = kms[:kms.find("k")]
            kms = float(kms.strip())
            part_count += kms
    return part_count + initial_sum

total = count_kms(events)
print(total)


