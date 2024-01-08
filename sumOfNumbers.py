a = 98799
sum = 0
t = 0

while a > 0:
    sum += a % 10
    a = a // 10
   
    
print(sum)
x = sum

while sum > 0:
    t += 1
    sum = sum // 10    
    
sum1 = 0

while x > 10:
    sum1 += (x % 10) * 10**(t-1)
    t -= 1
    x = x // 10

res = sum1 + x
print(res)