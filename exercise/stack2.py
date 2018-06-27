'''
I have a file in a special format .cns,which is a segmented file used to analyze copy number. 
It is a text file, that looks like this (first line plus header):

chromosome,start,end,gene,log2 
chr1,13402,861395,"LOC102725121,DDX11L1,OR4F5,LOC100133331,LOC100132062,LOC100132287,LOC100133331,LINC00115,SAMD11",-0.28067

The output I need is something like this:

gene log2
LOC102725121 -0.28067
DDX11L1 -0.28067
OR4F5 -0.28067
PIK3CA 0.35475
NRAS 3.35475
'''
import csv

list1 = []
with open('exercise\copynumber.cns','r') as file:
    exampleReader = csv.reader(file)
    for row in exampleReader:
        list1.append(row)

for row in list1:
    strings = row[3].split(',')   # Get fourth column in CSV, i.e. gene column, and split on occurrance of comma
    for string in strings:  # Loop through each string
        print(string + ' ' + str(row[4])) 