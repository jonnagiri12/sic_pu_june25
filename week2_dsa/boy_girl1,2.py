# boy girl 1 problem 

number_of_students = int(input("Enter number of students : "))
boys_height = list(map(int, input("Enter boys heights : ").strip().split()))
girls_height = list(map(int, input("Enter girls heights : ").strip().split()))
        
if number_of_students == len(boys_height) and number_of_students == len(girls_height):
    boys_height.sort()
    girls_height.sort()
            
if boys_height[0] < girls_height[0]:
    boys_arragement = True
    for i in range(2, number_of_students+1):
        if boys_height[i-1] > girls_height[i-1] or girls_height[i-2] > boys_height[i-1]:
            boys_arragement = False
            break
    if boys_arragement == True:
        print("YES")
    else:
        print("NO")
            
else:
    girls_arragement = True
    for i in range(2, number_of_students+1):
        if boys_height[i-1] < girls_height[i-1] or boys_height[i-2] > girls_height[i-1]:
            girls_arragement = False
            break
    if girls_arragement == True:
        print("YES")
    else:
        print("NO")

# boy girl 2 problem 

number_of_times = int(input("Enter number of times : "))
for _ in range(number_of_times):
        number_of_students = int(input("Enter number of students : "))
        boys_height = list(map(int, input("Enter boys heights : ").strip().split()))
        girls_height = list(map(int, input("Enter girls heights : ").strip().split()))
        
        if number_of_students == len(boys_height) and number_of_students == len(girls_height):
            boys_height.sort()
            girls_height.sort()
            
            if boys_height[0] < girls_height[0]:
                boys_arragement = True
                for i in range(2, number_of_students+1):
                    if boys_height[i-1] > girls_height[i-1] or girls_height[i-2] > boys_height[i-1]:
                        boys_arragement = False
                        break
                if boys_arragement == True:
                    print("YES")
                else:
                    print("NO")
            
            else:
                girls_arragement = True
                for i in range(2, number_of_students+1):
                    if boys_height[i-1] < girls_height[i-1] or boys_height[i-2] > girls_height[i-1]:
                        girls_arragement = False
                        break
                if girls_arragement == True:
                    print("YES")
                else:
                    print("NO")
