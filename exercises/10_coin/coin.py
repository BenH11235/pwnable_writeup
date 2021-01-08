from pwn import *
import re

#constants
INTRO_LENGTH =  10024
PORT = 9007
NUMBER_OF_ROUNDS = 100
LOCALHOST = '0'
REMOTEHOST = "pwnable.kr"

def main():
    conn = remote(LOCALHOST, PORT)
    conn.recv(INTRO_LENGTH)
    for i in range(NUMBER_OF_ROUNDS):
        n, c = re.compile("N=(\d+) C=(\d+)").match(nextline(conn)).groups()
        n ,c = int(n), int(c)
        lpivot, rpivot = 0, n//2
        guesses = 0
        while rpivot - lpivot > 0 and guesses < c:
            guess = list(range(lpivot, rpivot))
            send(conn, ' '.join([str(j) for j in guess]))
            guesses += 1
            counterfeit = (int(nextline(conn)) != len(guess)*10)
            delta = rpivot - lpivot
            
            rpivot -= delta // 2
            if not counterfeit:
                lpivot += delta
                rpivot += delta
        
        #use up leftover guesses
        while guesses < c:
            send(conn, "0")
            _ = nextline(conn)

        #done weighing, report guess
        send(conn, str(lpivot))
        success_msg = nextline(conn)
            

    #flag should be printed here
    print(nextline(conn))
    conn.close()  

def send(c, l):
    print(l)
    c.sendline(l)

def nextline(c):
    l = c.recv(1024).decode('UTF-8')
    print(l)
    return(l)

main()
