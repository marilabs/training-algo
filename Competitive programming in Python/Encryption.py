vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
alphabet = 'azertyuiopqsdfghjklmwxcvbn'

def find_pos(char, string):
    for i in range(len(string)):
        if string[i] == char:
            return i
    return -1

def decrypt(seq):
    word = ''
    occurences = {}
    for letter in alphabet:
        occurences[letter] = 0
    for letter in seq:
        occurences[letter] += 1
        if letter in vowels:
            current = vowels
            other = consonants
        else:
            current = consonants
            other = vowels
        k = occurences[letter]
        pos = find_pos(letter, current) + (k - 1) * len(current)
        word += other[pos % len(other)]
    return word

print(decrypt(input()))