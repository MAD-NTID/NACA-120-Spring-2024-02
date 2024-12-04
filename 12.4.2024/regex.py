import re

def search(regex, data):
    match = re.search(regex, data)

    if match is None:
        print("No Match Found")
    else:
        print(f"Match is found: {match.group()}")

# search(r'\d+', "Trent123")

def match(regex, data):
    match = re.match(regex, data)

    if match is None:
        print("Nothing was found")
    else:
        print(match.group())

# this will print Nothing was found, because "Welcome" is not the same as the start "Hello,..."
# match("Welcome", "Hello, Welcome to RIT!")

# this will print the match, because "Hello" is the same as the start "Hello,..."
# match("Hello", "Hello, Welcome to RIT!")

def start_with(regex, data):
    reg = r'' + regex
    match = re.match(reg, data)

    if match is None:
        print(False)
    else:
        print(True)

# start_with("Welcome", "Welcome to RIT!")

def is_digit(data):
    regex = r'^\d+$'
    match = re.search(regex, data)

    if match is None:
        print(False)
    else:
        print(True)

# this should be false
# is_digit("abc123")

# this should be true
# is_digit("123")

# Assume that a string has many phone numbers using the same pattern.
# You are assigned to extract all of these phone numbers from the string using regex
phone_numbers_string = """
    RIT has many phone numbers, Here are some numbers we use on campus:
    123-123-1234
    1-569-123-3654
    +1-569-235-1245
    1234567890
    +11234567890
    11234567890
    (123)-584-2369
    4444
"""

def extract_phone_numbers(phone_numbers_string):
    regex = r'\+?\d?-?\(?\d{3}\)?-?\d{3}-?\d{4}'
    matches = re.findall(regex, phone_numbers_string)

    if matches is None:
        print("No matches were found")
    else:
        print(matches)

# extract_phone_numbers(phone_numbers_string)

def validate_phone_numbers(phone_numbers):
    regex = r'\+?\d?-?\(?\d{3}\)?-?\d{3}-?\d{4}'
    matches = re.findall(regex, phone_numbers)

    if matches is not None:
        # is matches length is 1 or more, it will return True (the numbers are valid)
        return len(matches) > 0
    
    # otherwise, it will return False
    return False

# print(f'Is Phone Number Valid: 123-123-1234 - {validate_phone_numbers("123-123-1234")}')
# print(f'Is Phone Number Valid: +1-123-123-1234 - {validate_phone_numbers("+1-123-123-1234")}')
# print(f'Is Phone Number Valid: 1231231234 - {validate_phone_numbers("1231231234")}')
# print(f'Is Phone Number Valid: 123 - {validate_phone_numbers("123")}')

def show_last_four_ssn(ssn):
    valid_regex = regex = r'\d{3}-?\d{2}-?\d{4}'
    match = re.search(valid_regex, ssn)

    if match is None:
        return "SSN is Invalid"    

    regex = r'\d{3}-?\d{2}-?'
    replacement = '***-**-'
    last_four = re.sub(regex, replacement, ssn)

    return last_four

print(f'The last four digits of the ssn: 123-12-1234 is {show_last_four_ssn("123-12-1234")}')
print(f'The last four digits of the ssn: 123-1-123 is {show_last_four_ssn("123-1-123")}')