# find duplicates in a list
new_str = "my first day"
new_ls =  list(new_str)
print(new_ls)

def dupl_search(list):
    sorted_list = list.sort()
    len_list = len(sorted_list)
    for i in range(0,(len_list - 1)):
        if sorted_list(i) == sorted_list(i+1):
            dup_item = sorted_list(i)
    return sorted_list(i)


duplicatte = dupl_search(new_ls)

print(duplicatte)

