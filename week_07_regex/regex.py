import re

def find_name(line):
    pattern = r"(Mr|Mrs|Ms|Dr)\.?( [A-Z][a-z]*)( [A-Z][A-Za-z]*)*"
    result = re.findall(pattern,line)

    pattern = r"John Smith"
    result = result + re.findall(pattern,line)
    return result


#result = find_name("John Smith is a friend of Mrs. Cho")
#print(result)

f = open("namefile.dat")
for line in f.readlines():
    #print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)

