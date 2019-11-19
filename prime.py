# Python program to print all prime numbers in an interval 
  
prime_nums = [1,2]
val = 3
prime = True

while len(prime_nums) <= 100:
    for n in range(2, val): 
        if (val % n) == 0: 
            prime = False
    if prime == True:
        prime_nums.append(val)
    val += 1
    prime = True
print(prime_nums)
