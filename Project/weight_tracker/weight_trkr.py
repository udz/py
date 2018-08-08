'''
A weight tracker app
Requirements:
- It accepts a set of manual entries of weight measurements taken at different dates
- It can plot a graph
- It can allow you to track multiple entities, for example more than one person’s weight
- It stores the weights somewhere
'''


def start_program():
    print('\nPress 1. to setup measurement unit')
    print('Press 2. to setup person')
    print('Press 3. to record weight')
    print('Press 4. to display all recorded measurements')
    print('Press 5. to display graph of recorded measurements')
    print('Press 0. to Quit the program')
    option = input('\nPlease enter your selection: ')
    return int(option)

def set_unit(units):
    var = input('Setup Weight Measurement Unit. Options: 1. ' + units[0] + ' 2. '+ units[1] + '\nPlease enter your selection:')
    if int(var) == 1:
        print('\nSetting measurement unit as',units[0])
        v = input('Press any key to continue...')
        return units[0]
    elif int(var) == 2:
        print('\nSetting measurement unit as',units[1])
        v = input('Press any key to continue...')
        return units[1]
    else:
        return -1

def capture_measurement(cnt):
    measurment = input('Enter weight on day ' + str(cnt) + ' :')
    return {cnt:int(measurment)}

def display_measurements(recording,unit):
    print('Following are the recorded weight measurements')
    for key,value in recording.items():
        print('   Weight on day',key,'is',value,unit)
    print('End of the recording')
    v = input('\nPress any key to continue')

def display_graph(dict):
    import matplotlib.pyplot as plt
    plt.plot(list(dict.keys()),list(dict.values()))
    plt.show()

units = ['lb','kg']
unit = ''
count = 1
recording = {}

print('Welcome to the weight measurement recording program.')
print('Please use the following options to navigate the program functionalities')

while True:
    selection = start_program()
    if selection == 1:
        unit = set_unit(units)
    elif selection== 2:
        pass
    elif selection == 3:    
        recording.update(capture_measurement(count))
        print(recording)
        count += 1
    elif selection == 4:
        display_measurements(recording,unit)
    elif selection == 5:
        display_graph(recording)
    elif selection == 0:
        print('Thank you for using this program.\nHave a nice day!')
        break
    else:
        print('Wrong selection entered. Please try re-entering selection again.')
