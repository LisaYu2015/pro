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
output all possible reorderings of a list
new_str2 = "abcdefg"
new_ls2= list(new_str2)
print(new_ls2)
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
  """

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








 