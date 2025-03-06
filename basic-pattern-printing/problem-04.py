"""
Write a function called show_palindrome that takes a number as an argument and then returns a palindrome string. Finally, prints the returned value in the function call.
=====================================================
Example:
Function Call:
show_palindrome(5)
Output:
123454321
===================

"""
def show_palindrome(n):
    for i in range(1, n + 1):
        print(i, end="")
    for j in range(n - 1, 0, -1):
        print(j, end="")
    print()

n = int(input("Enter a number: "))
show_palindrome(n)

"""
=====================================================

Write a function called show_palindromic_triangle that takes a number as an argument and prints a Palindromic Triangle in the function.
[Must reuse the show_palindrome() function of the previous task]
=====================================================

Example: Function Call: show_palindromic_triangle(5) Output: 
................1
............1...2...1
........1...2...3...2...1
....1...2...3...4...3...2...1
1...2...3...4...5...4...3...2...1
=============================================================
"""
def show_palindromic_triangle(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        show_palindrome(i)

n = int(input("Enter a number: "))
show_palindromic_triangle(n)

