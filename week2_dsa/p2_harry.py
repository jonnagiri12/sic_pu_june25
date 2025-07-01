number_of_goldcoins = int(input("Enter number of gold coins : "))
goldcoins_bag = list(map(int, input("Enter gold coins worth : ").strip().split()))

no_of_instructions, x = input("Enter no of instrctions and x value : ").split()
i = 1
monk = []
for _ in range(int(no_of_instructions)):
    instruction = input("Enter instructions : ").lower()
    if instruction == "harry":
        goldcoin = goldcoins_bag[i-1]
        monk.append(goldcoin)
        i += 1
    elif instruction == "remove":
        monk.pop()
if sum(monk) == int(x):
    print(len(monk))