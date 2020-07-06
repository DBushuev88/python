def int_func(word):
    small = word[0]
    big = chr(ord(small) - ord('a') + ord('A'))
    return big + word[1:]


source = input("Type some lowercase text").split()
res = []
for word in source:
    res.append(int_func(word))
print(' '.join(res))