'''
In Python, the seek() and tell() functions are used to 
work with th file objects and thier positions within a 
file. These functions are part of the built-in io module,
which provies a consistence inteface for reading and writig
to various file-like objects, such as files, pips, and in-memory
buffers.
'''

with open('file.txt', 'r') as f:
    print(type(f))
    # Move to the 10th btein the file
    f.seek(10)
    
    l = f.tell() # tell will returs the currnt location in the file
    print(l)
    
    # Read the next 5 bytes
    data = f.read(50)
    print(data)

with open('sample.txt', 'w') as f:
    f.write('Hello World!')
    f.truncate(3) 
    
with open('sample.txt', 'r') as f:
    print(f.read())