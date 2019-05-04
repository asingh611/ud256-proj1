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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
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

# Get the first record from the list of texts
# Time complexity to get item from position in list -> O(1)
first_text = texts[0]

# Print out message
# Time complexity to print message -> O(1)
print("First record of texts, %s texts %s at time %s"
      % (first_text[col_textFrom], first_text[col_textTo], first_text[col_textTime]))


# Get last record from list of calls
# Time complexity to get item from position in list -> O(1)
last_call = calls[-1]

# Print out message
# Time complexity to print message -> O(1)
print("Last record of calls, %s calls %s at time %s, lasting %s seconds"
      % (last_call[col_callFrom], last_call[col_callTo], last_call[col_callStartAt], last_call[col_callDuration]))

# Overall worst-case time complexity -> O(1)
