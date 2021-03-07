# Enter your code here. Read input from STDIN. Print output to STDOUT
phoneBook = {}
for i in range(int(input())):
    inputString = str(input()).split()
    phoneBook[inputString[0]] = inputString[1]

while True:
    try:
        query = str(input())
        if query in phoneBook:
            print("{}={}".format(query,phoneBook[query]))
        else:
            print("Not found")
    except:
        break