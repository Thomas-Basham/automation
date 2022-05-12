import re
string = ''
with open("assets/existing-contacts.txt") as f:
    for line in f:
        string += line

# https://stackoverflow.com/questions/3868753/find-phone-numbers-in-python-script
# https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/

phone_pattern = r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

phone_nums = re.findall(phone_pattern, string)

emails = re.findall(email_pattern, string)


print(phone_nums)
print(emails)


assert len(phone_nums) == 20, f"Found {len(phone_nums)} social security numbers"
