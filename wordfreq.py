def tokenize(lines):
    words = []
    for line in lines:
        line = line.rstrip()
        start = 0
        while start < len(line):
            while line[start].isspace():
                start += 1

            end = start
            if line[start].isdigit():
                while end < len(line) and line[end].isdigit():
                    end += 1  
            elif line[start].isalpha():
                while end < len(line) and line[end].isalpha():
                    end += 1  
            else:
                end += 1
            
            word = line[start:end].lower()
            words.append(word)
            start = end
    
    return words

def countWords(words, stopWords):
    stopWords = set(stopWords)
    frequencies = {}

    for word in words:
        if word not in stopWords:        
            if word in frequencies:
                frequencies[word] += 1
            else:
                frequencies[word] = 1

    return frequencies

def printTopMost(frequencies,n):
    sortedWords = sorted(frequencies.items(), key=lambda x:-x[1])
    for word in sortedWords[:n]:
        print(word[0].ljust(20), str(word[1]).rjust(5)) 