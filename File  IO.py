"""
read(r): This mode opens the file for reading 
         only and gives error if the file does not
         exisr . This is the file does not exist.
         This is the default mode if no mode is passed
         as a parameter.

write(w): This mode opens the file for writing only and 
          creates a new file if doesn't exist.
          
append(a): This mode opens the file for appending only and 
           creates a new file if the file doesn't exist.
        
create(x): This mode creats a file and gives an error if the
            file is already exists.
            
text(t): Apart from all modes we also need to specify how
         the file must be handled. t mode is used to handle 
         text files t referse to text mode . There is no 
         difference  r andrt or w and wt since text mode is 
         default .The default mode 'r'.
"""
# READING A FILE


f = open('myfile.txt', 'rb')  # read mode is default
text = f.read()
print(text)
f.close()


# WRITTING A FILE

f =  open('myfile2.txt', 'w')
f.write("Hello world!!")
f.close()


with open('myfile2.txt', 'a') as f:
    f.write("I am inside with")