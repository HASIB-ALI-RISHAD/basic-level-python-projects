'''
=====================================================================
Write a Python program that will ask the user to input a string (containing exactly one word). Then your program should print subsequent substrings of the given string as shown in the examples below.

Sample Input:
BANGLA

Sample Output:
B
BA
BAN
BANG
BANGL
BANGLA

Explanation: Simply, no of lines = length of the input string and no of letters in each line = line number.

=====================================================================
'''
word = input("Enter your desired word: ")
for i in range(len(word)):
    print(word[0:i+1])
