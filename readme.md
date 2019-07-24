# UD256 Project 1

## About this project
In this project a call log and text message log is provided as CSV files. Provided the format for each file and the rules for the phone numbers present in the log, the following tasks were implemented in Python

## Task 0
**Get the first record in the text message log and the last record in the call log.**

This task involved retrieving an item from a fixed position in a list, which is a constant time operation O(1) 

## Task 1
**Get the number of unique phone numbers from both logs**

This task involved iterating through all the items within the two log files. I chose to use a set to store the phone numbers as I iterated through the logs because sets maintain only unique values. The worst-case runtime is O(n) from iterating through the log files 

## Task 2
**Find the phone number that spent the longest total time in calls, and total amount of call time for that phone number**

In this task, a dictionary is used to hold each unique phone number and the sum of the time that phone number was on calls. Iterating through each entry in the call log, if that phone number already exists in the dictionary, then the call duration for that particular entry is added to the existing sum in the dictionary. Otherwise the phone number is added to the dictionary with the current call's duration. This is done for both the caller's phone number and for the phone number being called. With each entry, it is compared with the call duration of the current longest duration and the longest value is updated as needed. The worst-case runtime is O(n) from iterating through the log file

## Task 3
**Part 1: Find all of the area codes and mobile prefixes called by people in Bangalore printed in lexicographic order with no duplicates**

**Part 2: Find the percentage of calls from fixed lines in Bangalore that are made to fixed lines also in Bangalore**

The rules for determining location information from the area code was provided in the code comments in the starter file for this task. The code implementation is illustrated with the following pseudocode:

```
 For each entry in the log

   If calling phone number has area code 080 (isBangloreNumber):

       Check the format of the called phone number and extract the area code/prefix (getCodesAndPrefixes)

           If has parentheses, then extract characters between parentheses (ex: (080)xxxxxxx - 080)

           Else if contains a space, extract the first four digits
           
           Else - 140 (telemarketer)

       Add to set of codes/prefixes

       If called number had 080 area code (isBangloreNumber), increment sumOfBangloreNumbersCalled

 Print Message 1

 Print Message 2
```

 This assumes all phone numbers are of a valid format as outlined in the starter file

Since lexicographic order is required when printing the results, Python's sort function is used, which makes the worst-case runtime O(nlog(n))

## Task 4
**Create a set of possible telemarketers: these are numbers that make outgoing calls but never send texts, receive texts or receive incoming calls**

For this task, the call and text logs are iterated through in order to generate 4 sets:
* Set 1: Unique numbers making outgoing calls
* Set 2: Unique numbers receiving incoming calls
* Set 3: Unique numbers sending text messages
* Set 4: Unique numbers receiving text messages

Then for each phone number that is in Set 1 but not in Set 2, 3 or 4, add that number to a set of potential telemarketer phone numbers

The resulting potential telemarketer set is printed. Since lexicographic order is required when printing the results, Python's sort function is used, which makes the worst-case runtime O(nlog(n))


