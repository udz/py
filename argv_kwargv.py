# *argv and **kwargv

def printlist(*args):
    for count,var in enumerate(args):
        print('{0} = {1}'.format(count,var))

printlist('a','b','c')

def printkwlist(**kwargs):
    for key,value in kwargs.items():
        print('{0} = {1}'.format(key,value))

printkwlist(name='Ujjwal',age=40)