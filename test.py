def prime_num(num):
    divisor_ls = []
    prime = ""
    for divisor in range(2, num):
        if num % divisor == 0:
            divisor_ls.append(divisor)
        if len(divisor_ls) == 0 or num == 2: 
            prime = True
        else:
            prime = False    
    return prime
    

print(prime_num(2))

def prime_ls(K):
    prime_list = []
    num = 1
    while len(prime_list) < K:
        if prime_num(num) == True:
            prime_list.append(num)
        num += 1
    return prime_list

print(prime_ls(10))







