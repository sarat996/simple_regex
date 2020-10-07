from os import listdir
from os.path import isfile, join
import sys
import re
from collections import defaultdict
#onlyfiles contains names of all the files in the directory
onlyfiles = [f for f in listdir('./') if isfile(join('./', f))]

#Whether it is string or regex
search_type = sys.argv[1][1]

#If it is a string search
hits = 0
mydict = defaultdict(int)
# mydict = {}
if search_type == 's':
    string = sys.argv[2]
    #Iterate over each file in the directory
    for f in onlyfiles:
        #count the line number
        count = 0
        with open(f, 'r') as ff:
            # Iterate over each line in the file
            for line in ff:
                # Increment the line number
                count += 1
                # Print if the string is found in any line
                if(string in line):
                    print("{}:{}:{}".format(f, count, line.strip()))
                    mydict[f] += 1

elif search_type == 'r':
    string = sys.argv[2]
    # print(string)
    pattern = re.compile(string)
    # print(pattern)
    for f in onlyfiles:
        count = 0
        with open(f, 'r') as ff:
            for line in ff: 
            # print(i, line)
                count += 1
                for match in re.finditer(pattern, line):                    
                    mydict[f] += 1
                for match in re.finditer(pattern, line):
                    print ('{}:{}:{}'.format(f, count, line.strip()))
                    break

print("Total hits: {}".format(sum(mydict.values())))

for key in mydict:
    print('{}:{} hits'.format(key,mydict[key]))