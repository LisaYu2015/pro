"""
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

"""



"list the first K prime number"
"""
def prime_num(num):
    divisor_ls = []
    prime = False
    for divisor in range(2, num):
        if num % divisor == 0:
            divisor_ls.append(divisor)
        if len(divisor_ls) == 0 or num == 2: 
            prime = True
        else:
            prime = False    
    return prime


def prime_num(num):
    return not any(num % divisor == 0 for divisor in range(2, num))

print(prime_num(2))

def prime_ls(K):
    prime_list = []
    num = 1
    while len(prime_list) < K:
        if prime_num(num):
            prime_list.append(num)
        num += 1
    return prime_list

print(prime_ls(10))

"print out all the prime factors of a number: 12= 2, 3, "

def find_pfactor(num):
    prime_divisor = []
    for divisor in range(2, num+1):
        if num % divisor == 0 and prime_num(divisor):
                prime_divisor.append(divisor)
    return prime_divisor
"""


"""
output all possible reorderings of a list

new_str2 = "abcdefg"
new_ls2= list(new_str2)
print(new_ls2)

def reordering_ls(input_ls):
    len_ls = len(input_ls)
    for i in len_ls:
        input_ls[i] = 


"""
"""
def pattern_str(input_str):
    output_str = ""
    for i in range(1, len(input_str)-1):
            if input_str[i-1] == input_str[i+1]:
                output_str += " "
            elif input_str[i-1] != input_str[i+1] and input_str[i+1] != "\n":
                output_str += "*"   
            else:
                output_str += "\n"   
    return output_str

def triangle(edge_len):
    empty_space = " " * int((edge_len-1)/2)
    line = empty_space + "*" + empty_space + "\n"
    for len_triangle in range(edge_len,edge_len * edge_len):
        if len_triangle < 
        line += pattern_str(line) 
    return line

print(triangle(10))

"""
def pattern_str(edge_len):
    empty_space = " " * int((edge_len-1)/2)
    line = empty_space + "*" + empty_space + "\n"
    for i in range(edge_len +2, edge_len * edge_len+1):
        if i % edge_len == 2 or i % edge_len == 0:
            line += " "
        elif i % edge_len == 1 :
                line += "\n"   
        else:
            if line[i-(edge_len+1)-1] ==line[i-(edge_len+1)+1]:
                line += " "
            else: 
                line += "*"   
    return line

print(pattern_str(29))