no_of_req = int(input())
requriments = input().strip().split()

server1 = 0
if len(requriments) == no_of_req:
    for i in range(no_of_req):
        if i % 2 == 0:
            server1 += int(requriments[i])
    print("Allocation :", server1)
else:
    print("Invaild requriments.")