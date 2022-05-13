import re


def return_string_from_txt_file(txt_file):
    string = ''
    with open(txt_file) as f:
        for line in f:
            string += line
    f.close()

    return string


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


def write_to_txt_file(file, text_list, a=False):

    if a == True:
        textfile = open(file, "a")
    else:
        textfile = open(file, "w")

    for line in text_list:
        textfile.write(line + "\n")

    textfile.close()


def compare_text_files(file, existing_contacts):
    file_string = []
    with open(file) as f:
        for line in f:
            file_string.append(line)

    existing_file_string = []
    with open(existing_contacts) as g:
        for line in g:
            existing_file_string.append(line)

    no_duplicates = []
    [no_duplicates.append(x) for x in file_string if x not in existing_file_string]

    print(f"We already had {(len(file_string)) - (len(no_duplicates))} items from {file}")

    write_to_txt_file("assets/new_contacts.txt", no_duplicates, a=True)
    f.close()
    g.close()


text_file_string = return_string_from_txt_file("assets/potential-contacts.txt")

write_to_txt_file("assets/phone_numbers.txt", validate_phone_numbs(text_file_string))
write_to_txt_file("assets/emails.txt", validate_emails(text_file_string))

print(f"Found {len(validate_emails(text_file_string))} phone numbers")
print(f"Found {len(validate_phone_numbs(text_file_string))} email numbers")

compare_text_files("assets/phone_numbers.txt", "assets/existing-contacts.txt")
compare_text_files("assets/emails.txt", "assets/existing-contacts.txt")
