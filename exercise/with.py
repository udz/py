# More detail in following site
# https://stackoverflow.com/questions/1984325/explaining-pythons-enter-and-exit

# Without 'with' keyword
fp=open(r"exercise\music.txt")
try:
    for line in fp:
        print(line)
finally:
    fp.close()

# With 'with' keyword which doesn't require try block and close() method because code will be cleaned
# up automatically since __enter__ and __exit__ magic methods will be called
with open(r"exercise\music.txt") as fp:
    for line in fp:
        print(line)

'''
Implementing Context Manager Class
'''
class Log:
    def __init__(self,filename):
        self.filename=filename
        self.fp=None    
    def logging(self,text):
        self.fp.write(text+'\n')
    def __enter__(self):
        print("__enter__")
        self.fp=open(self.filename,"a+")
        return self    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        self.fp.close()

with Log(r"exercise\mylog.txt") as logfile:
    print("Main")
    logfile.logging("Test1")
    logfile.logging("Test2")