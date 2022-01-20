# If given a large string (like a multi-line string or a .txt file) take that string and return a dictionary that has the words as the key, and the value is a count of how many times that word was used.  There is no difference in a word that is capital or lowercase.  It still counts for the same word. 
#  For example if given: "This is a test string.  It is not very long.", your function should return 
# {
#   this: 1,
#   is: 2,
#   a: 1,
#   test: 1
#   string: 1
#   it: 1,
#   not: 1,
#   very: 1,
#   long: 1
# }
import re
data = 'This is a test sentence. It is not very long.'

test = data
punctuation = [","," ", "  ", "   ", "'", "\n", "?", "!", "."]
for c in punctuation:
    if c in test:
        test = test.replace(c, " ")
test = test.split(' ')

def word_count(input):
    words = {}
    for word in input:
        if word == "":
            continue
        lower = word.lower()
        if lower not in words:
            words[lower] = 1
        else:
            words[lower] += 1
    max_value = max(list(words.values()))
    print('MAX VALUE: ' + str(max_value))
    max_words = []
    for key in words:
        if words[key] == max_value:
            max_words.append(key)
    if len(max_words)==1:
        return max_words[0]
    else:
        return max_words
returned = word_count(test)
print(returned)




# print(re.match("\w*",input))