import datetime

def style(name):
    """Say hello to a person.
    Args:        
        name: the name of the person as string        
        language: the language code string
    Returns:        
        A number.    
    """
    print("{}".format(name))

    
style('Ujjwal')

today = datetime.datetime.now()
print(str(today))
print(repr(today))
print(eval(repr(today)))

result = 'Ujjwal D Shrestha'
print(result.upper())
print(result.title())

print(result.startswith('Ujj'))
print(result.endswith('tha'))


