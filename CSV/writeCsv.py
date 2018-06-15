import csv

outFile = open('CSV/out.csv','w',newline='')

# Comma separated values
outputWriter = csv.writer(outFile)
# Following code for Tab Separated Values with two newlines as line terminator
#outputWriter = csv.writer(outFile,delimiter = '\t',lineterminator = '\n\n')

outputWriter.writerow(['First','Second','Third','Fourth'])
outputWriter.writerow(['Hello, World','Second','Third','Fourth'])
outputWriter.writerow([1.2,1,3.23,4])

outFile.close()
