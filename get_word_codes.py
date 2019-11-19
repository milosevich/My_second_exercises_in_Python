def get_word_codes(words):
    """Given a list of words, return a dictionary where the words are keys,
        and the value for each key is a list of the character codes of the
        letters of the word that is its key"""
    return {
        word: [ord(c) for c in word]
            for word in words
    }
    
words = ['hello', 'Python is fun!']
codes = get_word_codes(words)
print(codes)