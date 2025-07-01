number_of_students = int(input("Enter number of students : "))
boys_height = list(map(int, input().strip().split()))
girls_height = list(map(int, input().strip().split()))

boys_height.sort()
girls_height.sort()

if boys_height[0] < girls_height[0]:
    boys_arragement = True
    for i in range(number_of_students):
        if boys_height[i] > girls_height[i]:
            boys_arragement = False
            break
    print("YES B")

else:
    girls_arragement = True
    for i in range(number_of_students):
        if girls_height[i] < girls_height[i]:
            girls_arragement = False
            break
    print("YES G")