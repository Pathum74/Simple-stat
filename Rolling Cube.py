#Rolling cube
#not suver

import random

one=0
notOne=0
n=int(input('Number of rolling:'))
x=0

while x < n:
    random_num = random.choice([1,2,3,4,5,6])
    if (random_num ==1):
        one += 1
    else:
        notOne += 6
    x+=1

print("One: ",one)
print("No one: ",notOne)

print("Probability of getting one",(one/6**n))
