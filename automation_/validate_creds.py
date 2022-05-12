import re


def return_string_from_txt(txt_file):
    string = ''
    with open(txt_file) as f:
        for line in f:
            string += line
    f.close()
    return string

# TODO Remove duplicate entries

def validate_phone_numbs(string):
    # https://stackoverflow.com/questions/3868753/find-phone-numbers-in-python-script
    phone_pattern = r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
    phone_nums = re.findall(phone_pattern, string)
    phone_nums.sort()
    no_duplicates = []
    [no_duplicates.append(x) for x in phone_nums if x not in no_duplicates]
    return no_duplicates


def validate_emails(string):
    # https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, string)
    emails.sort()
    no_duplicates = []
    [no_duplicates.append(x) for x in emails if x not in no_duplicates]
    return no_duplicates


def write_to_txt_file(file, phone_nums_list):
    textfile = open(file, "w")
    for line in phone_nums_list:
        textfile.write(line + "\n")

    textfile.close()

text_file_string = return_string_from_txt("assets/potential-contacts.txt")

write_to_txt_file("assets/phone_numbers.txt", validate_phone_numbs(text_file_string))
write_to_txt_file("assets/emails.txt", validate_emails(text_file_string))

print(f"Found {len(validate_emails(text_file_string))} phone numbers")
print(f"Found {len(validate_phone_numbs(text_file_string))} email numbers")
