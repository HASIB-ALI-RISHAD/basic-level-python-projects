'''
==========================================================
Write a python program that prints a rectangle of size M (height/line numbers) and N (length/column numbers) using incrementing numbers where M and N will be given as input. Please look at the examples below for clarification.

Sample Input:
4
6

Sample Output:
123456
123456
123456
123456

Explanation: The user has given 4 rows/lines and 6 columns as input. Therefore, we have 4 lines in our output here and in each line, the column number is printed from 1 through to 6 for the 6 columns.

==========================================================
'''
row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
for i in range(row):
    for j in range(1,col+1):
        print(j, end=" ")
    print()