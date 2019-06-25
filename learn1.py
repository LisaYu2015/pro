
def dupl_search(input_list):
    len_list = len(input_list)
    input_list.sort()
    dupl = []
    for i in range(0,(len_list - 1)):
        if input_list[i] == input_list[i+1]:
            dupl.append(input_list[i])
    return dupl
            
print(dupl_search(new_ls))