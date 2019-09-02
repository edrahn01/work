#!/usr/bin/python3
import struct

f = open('./txnlog.dat', 'rb')

magic = f.read(4)
version = ord(f.read(1))
records = int.from_bytes(f.read(4), byteorder='big')

#print(magic)
#print(version)
#print(records)

payment_type = {0: 'Debit',
        1: 'Credit',
        2: 'StartAutopay',
        3: 'EndAutopay'}

data = {}
for i in range(0, records):
    e = f.read(1)
    e = ord(e)

    e_name = payment_type[e]

    t = f.read(4)
    t = struct.unpack('!I', t)[0]
    
    u = f.read(8)
    u = struct.unpack('!Q', u)[0]

    if e == 0 or e == 1:
        d = f.read(8)
        d = struct.unpack('!d', d)[0]
    else:
        d = None

    data[i] = [e_name, t, u, d]

#    print(e_name)
#    print(t)
#    print(u)
#    print(d)

total = 0
for i, d in data.items():
    if d[0] == 'Debit':
        total += d[3]

print("What is the total amount in dollars of debits? %.2f"%(total))

total = 0
for i, d in data.items():
    if d[0] == 'Credit':
        total += d[3]

print("What is the total amount in dollars of credits? %.2f"%(total))

total = 0
for i, d in data.items():
    if d[0] == 'StartAutopay':
        total += 1

print("How many autopays were started? %i"%(total))

total = 0
for i, d in data.items():
    if d[0] == 'EndAutopay':
        total += 1

print("How many autopays were ended? %i"%(total))

balance = 0
for i, d in data.items():
    if d[2] == 2456938384156277127:
        balance = d[3]

print("What is balance of user ID 2456938384156277127? %.2f"%(balance))
