n_size, x_size, y_size = input().split()
num_lst = list(map(int, input().split()))

if(int(x_size) + int(y_size) == int(n_size)):
    num_lst.sort(reverse = True)
    p_count = num_lst[int(x_size)-1] - num_lst[int(x_size)]
    print(p_count)
