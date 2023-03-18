import os

if(not os.path.exists("data")):
    os.mkdir("data")

for i in range(0,100):
    os.rename(f"data/tut{i+1}",f"data/tut {i+1}")

folders = os.listdir("data")

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))
    
print(os.getcwd())
os.chdir("")
print(os.getcwd())

