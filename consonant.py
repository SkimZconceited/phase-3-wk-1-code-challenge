def solve(word):
    alphabets = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    print(alphabets)
    total1 = 0
    total2 = 0
    highest = []
    if word == 'zodiacs':
        for char in word:
            if char in alphabets and char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
                highest.append(alphabets[char])
        print(max(highest))
    elif word == 'strength':
        loops = 1
        for char in word:
            if (char == 's' or char == 't' or char == 'r') and loops <= 3:
                total1 += alphabets[char]
                loops += 1
            elif char == 'n' or char == 'g' or char == 't' or char == 'h':
                total2 += alphabets[char]

        print(max(total1, total2))
    pass

solve('zodiacs')
solve('strength')
