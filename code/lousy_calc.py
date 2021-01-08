#! /usr/bin/python3
import time
import random

delay = lambda: time.sleep(random.choice(range(100)) / 10)

if random.choice(range(5))!=0:
    print("Not feeling like working today! lol")
    exit(0)
delay()
print("You have to insert the first number manually! Haha!")
print("Not letting you pick a random value! Insert it yourself!")
x1 = int(input("!#@#$@> "))
delay()
#Maybe we should explicitly prompt for the second number? haha lol no
x2 = int(input("!#$@$> "))
delay()
print(f"Fine here's your sum: {x1}+{x2}={x1+x2+9} go ahead and choke on it")


