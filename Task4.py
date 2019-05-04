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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# Create 5 sets
# Set 1: Key = Outgoing Calls
# Set 2: Key = Incoming Calls
# Set 3: Key = Outgoing Texts
# Set 4: Key = Incoming Texts
# Set 5: Key  = Candidate telemarketers
# Check where number is in outgoing calls dictionary
# But NOT in incoming calls, outgoing texts and incoming texts

# Phone call column definitions
col_callFrom = 0
col_callTo = 1
col_callStartAt = 2
col_callDuration = 3

# Text column definitions
col_textFrom = 0
col_textTo = 1
col_textTime = 2

outgoingCalls = set()
incomingCalls = set()
outgoingTexts = set()
incomingTexts = set()
candidateTelemarketers = set()

# Iterate through calls and add phone numbers into sets -> O(number of call entries)
for entry in calls:
    # Adding items to a set -> O(1)
    outgoingCalls.add(entry[col_callFrom])
    incomingCalls.add(entry[col_callTo])

# Iterate through texts and add phone numbers into sets -> O(number of text entries)
for entry in texts:
    # Adding items to a set -> O(1)
    outgoingTexts.add(entry[col_textFrom])
    incomingTexts.add(entry[col_textTo])

# Iterate through unique outgoing phone numbers -> O(unique outgoing phone numbers)
for phoneNumber in outgoingCalls:
    # Checking for items in a set -> O(1)
    if phoneNumber not in incomingCalls \
        and phoneNumber not in incomingTexts \
            and phoneNumber not in outgoingTexts:

        # Adding items to a set -> O(1)
        candidateTelemarketers.add(phoneNumber)

print("These numbers could be telemarketers: ")
# Python sorting -> O(n*log(n))
# Iterating through list -> O(number of phone numbers)
for phoneNumber in sorted(candidateTelemarketers):
    print(phoneNumber)

# Overall worst-case complexity: O(n*log(n)) due to sorting
