import random
import struct
import sys
 
# Count of generated numbers
length = 300000

# Generate random numbers in the random.dat file
def generate():
    # Delete content from previous file
    open("random.dat", "w").close()
    # Generate numbers and write them into the file as bytes
    with open("random.dat", "wb") as fout:
        for i in range(length):
            r = random.randint(0, 2**31-1)
            fout.write(r.to_bytes(4, byteorder='little'))

#Generate numbers in ascending order
def generateAscending():
    # Delete content from previous file
    open("random.dat", "w").close()
    # Generate numbers and write them into the file as bytes
    with open("random.dat", "wb") as fout:
        for i in range(length):
            r = i
            fout.write(r.to_bytes(4, byteorder='little'))

# Read file that contains the numbers
# @return the numbers in the file as a list
def read():
    global length
    with open("random.dat", "rb") as fin:
        # Read data from file
        data = fin.read()
        int_list = []
        for i in range(0, len(data), 4):
            # Convert data to integers and add them to the list
            int_value = struct.unpack('<i', data[i:i+4])[0]
            int_list.append(int_value)
        return int_list

# Identify functions directly from the console
if __name__ == '__main__':
    globals()[sys.argv[1]]()