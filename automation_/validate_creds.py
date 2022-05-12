import re
string = ''
with open("assets/existing-contacts.txt") as f:
    for line in f:
        string += line
        # print(line)
# with open("assets/existing-contacts.txt") as f:
#     text_from_file = f.read()
#     for line in f:
#         print(line)

pattern = r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"

phone_nums = re.findall(pattern, string)
# print(string)
print(phone_nums)

assert len(phone_nums) == 20, f"Found {len(phone_nums)} social security numbers"
