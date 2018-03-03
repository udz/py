# This file takes input from the dataset of Kickstarter and formulates the
# dictionary object which could later be manupulated programatically

import os

os.getcwd()

path = '.\Data Sets\Kaggle\kickstarter-project-statistics'
dataFile = 'most_backed.csv'

os.chdir(path)

print('*****Opening File****')
dataFile = open(dataFile,mode='r')

data = []
data = dataFile.readline().split(',')
data[0] ='Sno'
print('*****Initiating Header*****')
print(data)

master = {}
#records = {}

for i in range(1,11):
    row = dataFile.readline().split(',')
    records = {}
    for j in range(0,len(data)):
        key = data[j]
        records[key]=row[j]
    #print(records)
    master[i] = records

print('******Closing File******')
dataFile.close()

print(master[9])
print(master)
