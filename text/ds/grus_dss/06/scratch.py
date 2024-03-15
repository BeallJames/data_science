import math, random

def random_kid():
    return random.choice(['b', 'g'])

g=0
b=0
eg=0
eb=0
bg=0
bb=0

# random.seed(0)
for _ in range(10000):
    older = random_kid()
    younger = random_kid()
    if older == 'g':
        g += 1
    if older == 'g' and younger == 'g':
        bg += 1
    if older == 'g' or younger == 'g':
        eg += 1

print(f'g {g/10000:0%}')
print(f'eg {eg/10000:0%}')
print(f'bg {bg/10000:0%}')

random_kid()