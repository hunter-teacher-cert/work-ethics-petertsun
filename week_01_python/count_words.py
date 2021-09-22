# The following program is from an example in https://books.trinket.io/pfe/09-dictionaries.html

fhand = open('data.dat')

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
       counts[word] = counts.get(word, 0) + 1   # if counts does not have word in the dictionary
                                                # the get() will return a 0. Now, counts[word] = 0 + 1 = 1
#print(counts)
for key in counts:
    print(key, counts[key])
                                                
