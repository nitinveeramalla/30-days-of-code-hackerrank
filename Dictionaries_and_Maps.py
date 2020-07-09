n = int(input())
phoneBook = dict()
for item in range(n):
    key,value = input().split()
    phoneBook[key] = value
while True:
    try:
        query = input()
        if query in phoneBook.keys():
            print(query+'='+phoneBook[query])    
        else:
            print('Not found')
    except:
        break