# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for num in range(n):
    str = input()
    print(str[::2]+" "+str[1::2])
