import re
import sys

def main():
    # input file
    inputFile = sys.argv[1]
    
    # output file
    outFile = sys.argv[2]
    
    # dictionary to keep track of all words and their counts
    word_count = {}

    # pattern to match
    pattern = re.compile(r'[a-zA-Z]+')
    
    with open(inputFile, 'r') as f:
        contents = f.read()
        matches = pattern.finditer(contents)
        
        for match in matches:
            word = match.group(0).lower()
            if word in word_count.keys():
                word_count[word] += 1
            else:
                word_count[word] = 1

    sorted_words = list(word_count.keys())
    sorted_words.sort()

    with open(outFile, 'w') as f:
        for word in sorted_words:
            f.write(word + ' ' + str(word_count[word]) + '\n')


if __name__ == "__main__":
    main()
