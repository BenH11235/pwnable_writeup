#! /usr/bin/python3

import sys
import pexpect
import time

if sys.argv[1] == "mock":
    target = "./bof"

if sys.argv[1] == "target":
    target = "nc pwnable.kr 9000"

p = pexpect.spawn(target)
with open("solution","rb") as fh:
    p.sendline(fh.read())
p.interact()
