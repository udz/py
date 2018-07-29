import subprocess

noteProcess = subprocess.Popen('C:\\Program Files (x86)\\Notepad++\\notepad++.exe')

# passing argument
noteProcess2 = subprocess.Popen(['C:\\Windows\\notepad.exe', 'E:\\Learning\\learn.txt'])

#subprocess.Popen(['C:\\python34\\python.exe', 'hello.py'])

#subprocess.Popen(['start', 'hello.txt'], shell=True)

print(noteProcess.poll())  # None if the program is running
noteProcess.wait() # Waits until the program finishes executing
print(noteProcess.poll()) # Prints exit code. 0 means process terminated without any error. 
                          # 1 or other integer if error occurred
print('Done')