# original_str = input()
# rotated_str = input()

# rotated_str_list = list(rotated_str)
# for _ in range(len(original_str)):
#     last_char = rotated_str_list.pop()
#     rotated_str_list.insert(0, last_char)
#     rotated = ''.join(map(str, rotated_str_list))
#     if rotated == original_str:
#         print("yes")

original_str = input()
rotated_str = input()

temp_str = rotated_str*2
if temp_str.find(original_str):
    print(1)
else:
    print(0)