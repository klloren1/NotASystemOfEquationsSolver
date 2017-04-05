inputFile = file("tom_sawyer.txt").read()
words = dict()
frequencies = list()
wordCount = 0
for word in inputFile.split():
    if words.has_key(word):
        words[word] += 1
    else:
        words[word] = 1
    wordCount += 1

for word in words.keys():
    frequencies.append((word, words[word]))

frequencies.sort(key=lambda tup: tup[1],reverse=True)

for entry in frequencies:
    print("Word: '{}' | count: {} | frequency: {}%".format(entry[0], entry[1], "{0:.4f}".format(float(entry[1])/wordCount*100)))