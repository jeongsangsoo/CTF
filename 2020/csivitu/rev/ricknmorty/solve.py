from pwn import * 
def GCD(n,n2):
    i = 1
    v4 = 0
    while(n>=i or n2>=i):
        if(not n % i and not n2 % i):
            v4 = i
        i+=1
    return v4
def fact(n):
    result = 1
    if n:
        result =  n * fact(n-1)
    return result 
if name == 'main':
    print("[+] connect")
    p = remote('chall.csivit.com','30827')
    while True:
        leak = p.recv(1024)
        tmp = leak.split(' ')
        first = tmp[0]
        second = tmp[1]
        if not first.isdigit():
            break
        print(first)
        print(second)
        v5 = GCD(int(first),int(second))
        v6 = int(fact(v5+3))
        p.sendline(str(v6))
    p.interactive()

