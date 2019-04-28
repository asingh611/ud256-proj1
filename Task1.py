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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# Text column definitions
col_textFrom = 0
col_textTo = 1
col_textTime = 2

# Phone call column definitions
col_callFrom = 0
col_callTo = 1
col_callStartAt = 2
col_callDuration = 3

# Choosing a set because they maintain only unique values
uniqueNumbers = set()

# Iterate over the list of entries in the text log -> O(n)
for entry in texts:
    # Adding to a set -> O(1)
    uniqueNumbers.add(entry[col_textFrom])
    uniqueNumbers.add(entry[col_textTo])

# Iterate over the list of entries in the call log -> O(n)
for entry in calls:
    # Adding to a set -> O(1)
    uniqueNumbers.add(entry[col_callFrom])
    uniqueNumbers.add(entry[col_callTo])

# Getting the length of a set -> O(1)
print("There are %d different telephone numbers in the records." % len(uniqueNumbers))

# Overall time complexity -> O(n) (considering n as the sum of the number of entries in both the call and text logs)
