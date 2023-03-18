# READLINES METOD 

f = open('mfile.txt', 'r')
i = 0
while True:
    line = f.readline()
    i = i + 1
    if not line:
        break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print(f"Marks of student {i} in math is: {m1}")
    print(f"Marks of student {i} in SST is: {m2}")
    print(f"Marks of student {i} in English is: {m3}")
    print(line)
    
# WRITE LINE METHODS

f = open('mfile2.txt', 'w')
lines = ['line 1\n','line 2\n','line 3\n']
f.writelines(lines)
f.close()
