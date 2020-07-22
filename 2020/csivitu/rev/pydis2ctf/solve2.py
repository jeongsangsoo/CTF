c = "¤"
encodedflag = "¤Ä°¤ÆªÔ\x86$\xa04\x9cÌ`H\x9c¬>¼f\x9c¦@HH\xa0\x84¨\x9a\x9a¢vÐØ"
flag = ''

for i in encodedflag:
    flag += chr(ord('c') + int(((ord(i) - ord(c)) / 2)))
print(flag)
