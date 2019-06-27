new_str = "hello, this is Lisa"
new_ls = list(new_str)
print(new_ls)

def repli_count(input_list):
    repl_dic = dict()
    for i in input_list:
        if i in repl_dic:
            repl_dic[i] = repl_dic[i] + 1
        else:
            repl_dic[i] = 1
    return repl_dic

def eliminate_single(input_dic):
    for i in list(input_dic):
        if input_dic[i] == 1:
            del input_dic[i]
    return input_dic

new_dic = repli_count(new_ls)
print(new_dic)
replic_dic = eliminate_single(new_dic)
print(replic_dic)


