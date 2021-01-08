#! /usr/bin/python3

import pexpect
import random
import re


while True:
    p = pexpect.spawn("./lousy_calc.py")
    p.setecho(False)
    result = p.expect(["> ", "lol"])
    if result != 0:
        print("Just a moment, the adder is not being cooperative...")
        continue
    print("I've persuaded the adder to cooperate =)")
    x1 = random.choice(range(100))
    print(f"I chose x1 randomly for your convenience: {x1}")
    p.sendline(str(x1))
    p.expect("> ")
    x2 = int(input("Please kindly supply a value for x2: "))
    p.sendline(str(x2))
    p.expect(pexpect.EOF)
    answer = p.before.decode("ascii")
    lousy_result = int(re.search("=([0-9]+)", answer).group(1))
    print(f"Kind sir, your resulting sum is {lousy_result-9}. Have a nice day!")
    break

