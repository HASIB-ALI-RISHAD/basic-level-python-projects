"""
We need to ask three questions to solve these problem.
1. what is the row number?
2. what is the column number?
3.what to print in each cell?
"""
#########################################################################################
"""
1111
2222
3333
4444
"""
# 1.n
# 2.n 
# 3.i 
n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(n):
        print(i, end="")
    print()
print("=========================================================================")
"""
1234
1234
1234
1234
"""
# 1.n
# 2.n
# 3.j
for i in range(n):
    for j in range(1, n+1):
        print(j, end="")
    print()
print("=========================================================================")
"""
4321
4321
4321
4321
"""
#1.n
#2.n
#3.n-j
for i in range(n):
    for j in range(n):
        print(n-j, end="")
    print()
print("=========================================================================")
"""
1
12
123
1234 
"""
#1.n
#2.i
#3.j
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end="")
    print()
print("=========================================================================")
""""
1
23
345
4567"
"""
#1.n
#2.i
#3.i+j
for i in range(1,n+1):
    for j in range(i):
        print(j+i, end="")
    print()
print("=========================================================================")
""""
1
23
456
78910
"""
#1.n
#2.i
#3.i+j+1
num = 1
for i in range(1, n + 1):  
    for j in range(i):  
        print(num, end="")  
        num += 1 
    print()
print("=========================================================================")



"""
****
***
**
*
"""
# 1. n
# 2. n-i
# 3 *
for i in range(n):
    for j in range(n-i):
        print("*", end="")
    print()

print("=========================================================================")

""""
   *
  **
 ***
****
"""
# 1. n
# 2. n
# 3. n-1 space, i star

for i in range(1, n+1):
    print(" " * (n - i) + "*" * i)

print("=========================================================================")   