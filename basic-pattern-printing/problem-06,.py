
# # print nth alphabet
# n=int(input("Enter a number: "))
# # 'A' + k - 1
# x = ord('A')
# asciiTarget = x + k - 1
# targetChar = chr(asciiTarget)
# print(targetChar)

"""
ABCD
ABCD
ABCD
ABCD
"""

n=int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        letter = ord("A")+j
        print(chr(letter),end="")
    print()
    # ord return int and chr return char
print("=========================================================================")

''''
ABCD
BCDE
CDEF
DEFG
'''

for i in range(n):
    start_letter = ord("A")+i
    for j in range(n):
        letter = start_letter+j
        print(chr(letter),end="")
    print()
print("=========================================================================")
    
'''
Sample Input: 4
Sample Output:
A
BB
CCC
DDDD
'''
for i in range(n):
    letter = ord("A")+i
    for j in range(i+1):
        print(chr(letter),end="")
    print()
print("=========================================================================")

"""
A
BC
CDE
DEFG
"""
for i in range(n):
    letter = ord("A")+i
    for j in range(i+1):
        print(chr(letter+j),end="")
    print()
print("=========================================================================")

"""
Sample Input: 8

H
GH
FGH
EFGH
DEFGH
CDEFGH
BCDEFGH
ABCDEFGH
"""
for i in range(n):
    last_letter = ord("A")+n-1
    srt_letter= last_letter -i
    for j in range(i+1):
        print(chr(srt_letter+j),end="")
    print()
print("=========================================================================")
