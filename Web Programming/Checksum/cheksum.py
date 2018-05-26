# debugging - put this line in the code where you want the debugger to start.
# h = help
# n = next command (also, 's' does the same thing?)
# c = continue to next break point (might need to hit this a few times)
#
# NOTE, to do this in dexcenter, you need a few pre-requisite changes to disable
# the SessionMgr logfiles:
#   - in DEXSessionMgr.cfg, comment out the logfile declaration
#   - in DEXClient.py, set taskLogName = '' around line 86 (before it gets called in the try)
#
import pdb;pdb.Pdb().set_trace()


# checksum
import md5
m=md5.new()
m.update(open('filename.zip', 'rb').read())
checksum = m.hexdigest()


#
# Launching a process asynchronously (ie, don't wait for it, just launch it and
# go on to the rest of the python code)
#
# Note... the run function must be called below its definition
#
import os
import string

def run(program, *args):
    try:
        return os.spawnv(os.P_NOWAIT, program, (program,) + args)
    except os.error:
        pass
    raise os.error, 'problem encountered when trying to run program: ' + program

run('C:\\UGS\\IDEAS12\\bin\\ideas.cmd', '')
run("c:\\windows\\system32\\notepad.exe", "somefile.txt")

# determine the user id of the person running python - only works on unix?
import os, pwd
user = pwd.getpwuid(os.getuid())[0]
print user


# reading an ini file into a dictionary
v4_profile = ConfigReader.readConfig('.' + os.sep + 'v4_profile.ini', 'catia_environ')
   (arg1 = ini filename, arg2 = section to read)
      ===> NOTE... v4_profile will be a dictionary with keys for each option set
      in the ini file section.  However, the option names end up as UPPERCASE
      keys in the dictionary.


# mapping a drive on win
   mapstring = os.sep + os.sep + 'milford6' + os.sep + 'cadshare'
   os.system('net use w: ' + mapstring + ' /USER:iti-sc.com' + os.sep + 'dexadm dkn.59q')

# poor man's debugger
# for windows, put this in place of the os.system that launches the cad system
# this provides a dos prompt in the DTS's environment, to try running the cad
# system etc  (note, must have desktop interaction enabled)
      os.system('start cmd')
      dexlib.pause()



# Network issues
# To verify a network machine name, do the following.  In this case, 'claude' is the DTS and
# the python commands are executed on 'iti100675' which is the DXS.
import socket
socket.getfqdn('claude')


# to compile a .py file (generates a .pyc)
# Note - per Laurine, the .pyc files are platform independent.
# They are python version dependent though.  Python version mismatches can result in "bad magic number" error.
>>> import py_compile
>>> py_compile.compile('CADDS5.py')



# figure out the os
# NOTE - this returns win32 even if running a 64bit os
if string.find(sys.platform, 'win') != -1:
   print "windows"
else:
   print "unix"

# figure out if we're running python32 or python64?
# 4 indicates 32bit python
# 8 indicates 64bit python
import struct 
struct.calcsize('P') 

# figure out if we're running a 64bit OS
# look at environment variable PROCESSOR_ARCHITECTURE... although this may not
# always be set right in the DTS service.

###
### filename globbing - behaves differently on windows vs unix!!!
###

# on windows, this finds lowercase AND uppercase .prt extensions
if string.find(sys.platform, 'win') != -1:
   print 'win'
   files = glob.glob('*.prt')

# on unix, we need to find lowercase and uppercase .prt seperately
else:
   print 'unix'
   files = glob.glob('*.prt') + glob.glob('*.PRT')







# To force a pause which can be continued by creating a file
# Note, this has been implemented as dexlib.pause()
import os, os.path, time

print 'pausing... to continue, create ' + os.getcwd() + os.sep + 'go'
while 1:
   if not os.path.exists('go'):
      time.sleep(1)
   else:
      os.remove('go')
      break


# to determine a filename's extension
ext = string.split(filename, '.')[len(string.split(filename, '.'))-1]



# if/else syntax
if x==y:

elif:

else:



# see if a string is in a list (if not, will be 0)
print l.count('a')



# Lookup the section names in the ini file.
config = ConfigParser.ConfigParser()
config.read('iqr_list.txt')
sections = config.sections()


# Check for a key's existence in a dictionary
dict.has_key('kljsjkl')


# spit out the environment to a file
envfile = open('cadiq_report_combine_env.txt', 'a')
for key in os.environ.keys():
   envfile.write(key + '=' + os.environ[key] + '\n')
envfile.flush()
envfile.close()


# open a file and loop through its lines
for line in open('test.py').readlines():
   print line


# To list all of the methods and attributes associated with an object, do this:
import string
dir(string)


# To get a list of ini file sections, do this.
config=ConfigParser.ConfigParser()
config.read('CONFIG')
print config.sections()



# To determine if a number is odd or even...
for num in range (0,100):
   result = float(num)/float(2)
   if result == int(result):
      print str(num) + ' is an even number.'
   else:
      print str(num) + ' is an odd number.'



# To determine if a string can be converted to an integer:
def isInteger(str):
   import types
   try:
      test = int(str)
   except:
      # We get in here if there was a problem in the try block.
      return 0
   else:
      # The 'else' is optional.
      if type(test) is types.IntType:
         return 1
      else:
         return 0

# quick-and-dirty code for renaming all files in the local directory to remove
# the .1 (for proe)
import glob, string, os
for file in glob.glob('*.*.*'):
   newname = string.replace(file, '.1', '')
   os.rename(file, newname)

# create big files quickly - this one is about 7.7MB
file = open('pinion.jt.txt', 'w')
for i in range(1,1000000):
   file.write(str(i) + '\n')
   file.flush()
file.close()






# Execute some_function at run-time
if __name__ == '__main__':
   exit_code = some_function()
   sys.exit(exit_code)
