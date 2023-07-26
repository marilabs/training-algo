t9 = "22233344455566677778889999"

def letter_to_digit(char):
    assert 'a' <= char <= 'z'
    return t9[ord(char) - ord('a')] # ord(char): unicod of char

def word_to_digit(word):
    return ''.join(map(letter_to_digit, word)) # map(function, iterable)

def prediction(dico):
    total_weight = {}
    for word, weight in dico:
        prefix = ''
        for letter in word:
            prefix += letter
            if prefix in total_weight:
                total_weight[prefix] += weight
            else:
                total_weight[prefix] = weight
    prop = {}
    for prefix in total_weight:
        digit = word_to_digit(prefix)
        if (digit not in prop or total_weight[prop[digit]] < total_weight[prefix]):
            prop[digit] = prefix
    return prop

def suggestion(dico, sequence):
    if sequence in dico:
        return dico[sequence]
    return None

