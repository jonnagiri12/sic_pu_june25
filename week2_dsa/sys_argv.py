import sys

states = ["Arunachal Pradesh : Itanagar", "Assam : Dispur", "Manipur: Imphal", "Meghalaya: Shillong", "Mizoram: Aizawl", 
"Nagaland: Kohima", "Tripura: Agartala"]
state_name = []
capital_name = []

for i in states:
    state, capital = i.split(":")
    state_name.append(state)
    capital_name.append(capital)
    

print("State                      Capital")
print("------------------------------------")
for i in range(len(state_name)):
    print("{:25} {:28}".format(state_name[i], capital_name[i]))
