import sys
import urllib.request

from wordfreq import tokenize, countWords, printTopMost

def main(args):
    stopWordsFile = open(args[1], encoding="utf-8")
    stopWords = stopWordsFile.read().strip().splitlines()
    stopWordsFile.close()
    
    if args[2].startswith(("http://", "https://")):
        response = urllib.request.urlopen(args[2])
        lines = response.read().decode("utf8").splitlines()
    else:
        textFile = open(args[2], encoding="utf-8")
        lines = textFile.readlines()
        textFile.close()
    
    words = tokenize(lines)
    frequencies = countWords(words, stopWords)
    printTopMost(frequencies, int(args[3]))

if __name__ == "__main__":
    main(sys.argv)