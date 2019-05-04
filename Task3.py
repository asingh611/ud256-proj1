"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Psuedocode
# This assumes all phone numbers are of a valid format as outlined above

# For each entry in the log
#   If calling phone number has area code 080 (isBangloreNumber):
#       Check the format of the called phone number and extract the area code/prefix (getCodesAndPrefixes)
#           If has parentheses, then extract characters between parentheses (ex: (080)xxxxxxx -> 080)
#           Else if contains a space, extract the first four digits
#           Otherwise -> 140 (telemarketer)
#       Add to set of codes/prefixes
#       If called number had 080 area code (isBangloreNumber), increment sumOfBangloreNumbersCalled
# Print Message 1
# Print Message 2

# Phone call column definitions
col_callFrom = 0
col_callTo = 1
col_callStartAt = 2
col_callDuration = 3


# Extract the codes and prefixes from phone numbers based on the conventions outlined above
def get_codes_and_prefixes(phone_number):
    # Case 1: Is it a fixed line? (Has area code enclosed in parenthesis)
    # Will look up whether phone number has open parenthesis
    if '(' in phone_number:
        # Return the portion of the string between the parenthesis
        return phone_number.split(')')[0][1:]

    # Case 2: Is the phone number a mobile number? (No parenthesis but has space in middle)
    # Will check if phone number contains space
    elif ' ' in phone_number:
        # Return the portion of the string before the space
        return phone_number.split(' ')[0]

    # Case 3: Otherwise it's a telemarketer (with a 140 prefix)
    else:
        return '140'


# Figure out if the phone number comes from a Bangalore fixed line (has 080 area code)
# Time complexity: O(1)
def is_bangalore_number(phone_number):
    return phone_number[:5] == '(080)'


# Testing
# print(get_codes_and_prefixes('78130 00821'))    # Expected: 78130
# print(get_codes_and_prefixes('(080)33118033'))  # Expected: 080
# print(get_codes_and_prefixes('1408371942'))     # Expected: 140
# print(get_codes_and_prefixes('(04344)322628'))  # Expected: 04344
#
# print(is_bangalore_number('78130 00821'))    # Expected: False
# print(is_bangalore_number('(080)33118033'))  # Expected: True
# print(is_bangalore_number('1408371942'))     # Expected: False
# print(is_bangalore_number('(04344)322628'))  # Expected: False

codesAndPrefixesCalled = set()
numOfBangaloreNumbersCalled = 0

# Time complexity to iterate through call entries O(n)
for entry in calls:
    call_from = entry[col_callFrom]
    call_to = entry[col_callTo]

    if is_bangalore_number(call_from):
        codesAndPrefixesCalled.add(get_codes_and_prefixes(call_to))
        if is_bangalore_number(call_to):
            numOfBangaloreNumbersCalled += 1


# Output for part 1:
print("The numbers called by people in Bangalore have codes:")
for code in sorted(codesAndPrefixesCalled):
    print(code)

# Output for Part 2:
percentOfBangaloreCalls = '{0:.2f}'.format(100 * numOfBangaloreNumbersCalled/len(calls))
print("%s percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
      % percentOfBangaloreCalls)
