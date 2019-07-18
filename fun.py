def vowels(s):
    v = ['a','e','i','o','u']
    c = 0
    for char in s:
        if char in v:
            c += 1
    return c
print(vowels("gokul"))