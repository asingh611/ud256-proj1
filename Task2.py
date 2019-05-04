"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# Choosing to use a dictionary where the key is the phone number and the total talk time is the value
# Pseudocode
# For each entry in the call log
#   If key is in dictionary
#       Add to existing time
#   Else If key is not in dictionary
#       Add new entry into dictionary
#   Compare to longest time
#   If greater than current longest time, set as new longest time
# Print out message

# Phone call column definitions
col_callFrom = 0
col_callTo = 1
col_callStartAt = 2
col_callDuration = 3

callTimes = dict()
longestTimePhoneNumber = calls[0][0]  # Setting the initial value as the first number

# Iterating over the call entries -> O(n)
for entry in calls:
    # Get the phone numbers for this entry and how long they were talking
    callFromPhoneNumber = entry[col_callFrom]
    callToPhoneNumber = entry[col_callTo]
    callDuration = entry[col_callDuration]

    # Check if the caller's phone number is already in the dictionary
    # If so, add the current call to the total duration
    # Checking for key in dictionary -> O(1)
    # Setting value in dictionary -> O(1)
    if callFromPhoneNumber in callTimes:
        callTimes[callFromPhoneNumber] += int(callDuration)
    else:
        callTimes[callFromPhoneNumber] = int(callDuration)

    # Check if sum of the call duration is now the longest
    # Checking values in dictionary -> O(1)
    if callTimes[callFromPhoneNumber] > callTimes[longestTimePhoneNumber]:
        longestTimePhoneNumber = callFromPhoneNumber

    # Now check for the phone number of the person being called
    if callToPhoneNumber in callTimes:
        callTimes[callToPhoneNumber] += int(callDuration)
    else:
        callTimes[callToPhoneNumber] = int(callDuration)

    # Check if sum of the call duration is now the longest
    if callTimes[callToPhoneNumber] > callTimes[longestTimePhoneNumber]:
        longestTimePhoneNumber = callToPhoneNumber

print("%s spent the longest time, %s seconds, on the phone during September 2016." %
      (longestTimePhoneNumber, callTimes[longestTimePhoneNumber]))

# Overall time complexity -> O(n)
