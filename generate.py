import random
import struct
 
length = 300000
 
def generate():
    with open("random.dat", "wb") as fout:
        for i in range(length):
            r = random.randint(0, 2**31-1)
            fout.write(r.to_bytes(4, byteorder='little'))

def read():
    global length
    with open("random.dat", "rb") as fin:
        data = fin.read()
        int_list = []
        for i in range(0, len(data), 4):
            int_value = struct.unpack('<i', data[i:i+4])[0]
            int_list.append(int_value)
        return int_list

generate()