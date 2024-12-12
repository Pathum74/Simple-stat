#Tossing a coin

import random

head=0
tail=0
n=int(input('Number of tossing:'))
x=0

while x < n:
    random_num = random.randint(1, 100)
    if (random_num < 50):
        head += 1
    else:
        tail += 1
    x+=1

print("Head: ",head)
print("Tail: ",tail)

print("Probability of getting head",head/n)
print("Probability of getting tail",tail/n)