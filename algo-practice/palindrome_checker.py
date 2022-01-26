def pal_check1(word):
    # palindrome checker
    print('Word: ', word)
    # slice a string in reverse: string[end:start:-1]
    # start is non-inclusive in reverse! Ok for odd length strings because middle char does not need to be tested
    # need to reduce by one for reverse test if length is even: -(len(word)+1)%2
    return word[:int(len(word)/2)-(len(word)+1)%2:-1].lower() == word[:int(len(word)/2)].lower()

def pal_check2(word):
    # palindrome checker
    print('Word: ', word)
    return word.lower() == word[::-1].lower()


test_words = ['bob','Bob','palindromeemordnilap','not','nada','y','no']
# test_words = ['bob']
for word in test_words:
    print(pal_check1(word),'\n')
    print(pal_check2(word),'\n')