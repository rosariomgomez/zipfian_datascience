import sys
import json

############################################
# Generate dictionaries with files data for easy manipulation
# key = business_id
# values: {} with key the date for inspections and violations
#############################################
def createDict(file,type):
    tags = file.readline().split(',"') #tags descriptors are the first row of the files (e.g.: "business_id", "name", ...)
    tags = [tag.strip('"') for tag in tags]
    dic = {}
    for line in file:
        key = line.split(',"')[0]  # The file is delimited by commas.
        values = line.split(',"')[1:]
        i = 1
        attr = {}
        for val in values:
       	    attr[tags[i]] = val.strip('"')
       	    i += 1
       	if type == 'businesses':
       		dic[key] = attr
        else:
        	if key not in dic.keys():
        		dic[key] = {}
        	dic[key][attr['date']] = attr
    return dic


def printDict(dict):
    print dict.items()


def main():
    businesses_file = open(sys.argv[1])
    inspections_file = open(sys.argv[2])
    violations_file = open(sys.argv[3])
    #restaurants = createDict(businesses_file, 'businesses')
    inspections = createDict(inspections_file, 'inspections')
    printDict(inspections)
    #violations = createDict(violations_file, 'violations')


if __name__ == '__main__':
    main()