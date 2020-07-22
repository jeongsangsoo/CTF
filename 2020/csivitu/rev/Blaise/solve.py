from pwn import *
def fact(n):
    result = 1
    if n:
        result = n * fact(n-1)
    return result
if __name__ == '__main__':
    p = remote('chall.csivit.com', '30808')
    display_num = int(p.recv(1024))
    print(display_num)
    index = 0
    while(index <= int(display_num)):
        v2= fact(display_num)
        v3 = fact(index)
        print("index "),
        print(index)
        v4 = v2 / (fact(int(display_num)-int(index)) * v3)
        print(v4)
        p.sendline(str(v4))
        index += 1
    print("[+] END")
    p.interactive()
