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

def triangle(x):
    output_str = ""
    line = ""
    for line_num in range(1, x):
        empty_space = " " * int(((x - line_num)/2))
        line = empty_space + "x" * line_num + empty_space + "\n"
        output_str += line 
    for i in range(1, len(line)-1):
        if line[i-1] == line[i+1]:
            line.replace(line[i], "*")
        else:
            line.replace(line[i], "x")
       
    return output_str

print(triangle(57))

