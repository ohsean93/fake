from random import random, uniform, randrange, choice, choices, sample, shuffle

print("random() => {0}".format(random()))

print("uniform({0}, {1}) => {2}".format( 1 , 10 , uniform(1.0,10.0) ))

print(randrange(1, 10))

print(choice(['a','b','c']))

print(choices(['a','b','c'],k=2))

print(sample(range(10),k=5))

a = list(range(10))
shuffle(a)
print(a)
