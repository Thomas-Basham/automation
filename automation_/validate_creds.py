import re
string = ''
with open("assets/potential-contacts.txt") as f:
    for line in f:
        string += line

# https://stackoverflow.com/questions/3868753/find-phone-numbers-in-python-script
# https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
phone_pattern = r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

phone_nums = re.findall(phone_pattern, string)
emails = re.findall(email_pattern, string)


phone_textfile = open("assets/phone_numbers.txt", "w")
for line in phone_nums:

    phone_textfile.write(line + "\n")

phone_textfile.close()


email_textfile = open("assets/emails.txt", "w")
for line in emails:

    email_textfile.write(line + "\n")

email_textfile.close()

# f.close()

print(f"Found {len(phone_nums)} phone numbers")
print(f"Found {len(emails)} email numbers")
