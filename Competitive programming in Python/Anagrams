def anagrams(sentence):
    dico = {}
    for word in sentence:
        sig = ''.join(sorted(word))
        if sig in dict:
            dico[sig].append(word)
        else:
            dico[sig] = [word]
    return [dico[sig] for sig in dico if len(dico[sig]) > 1]

# Solution for https://www.spoj.com/problems/ANGRAM/

n = int(input())
l = []
for i in range(n):
    sentence = input().split()
    sig1 = sorted(sentence[0])
    sig2 = sorted(sentence[1])
    l.append((sig1, sig2))
for i in range(n):
    print(l[i][0] == l[i][1])
