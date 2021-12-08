c1='4fd098298db95b7f1bc205b0a6d8ac15f1f821d72fbfa979d1c2148a24feaafdee8d3108e8ce29c3ce1291'
p1="hey let's rob the bank at midnight tonight!"
c2='41d9806ec1b55c78258703be87ac9e06edb7369133b1d67ac0960d8632cfb7f2e7974e0ff3c536c1871b'
c1_dec=[i for i in bytes.fromhex(c1)]
p1_dec=[ord(i) for i in p1]
key_dec=[c1_dec[i]^p1_dec[i] for i in range(0,len(p1_dec))]
c2_dec=[i for i in bytes.fromhex(c2)]
p2_dec=[c2_dec[i]^key_dec[i] for i in range(0,len(c2_dec))]
for i in p2_dec:
    print(chr(i),end='')
