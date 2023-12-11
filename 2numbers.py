def numbers(a, b, c):
    all_numbers = []
    all_numbers.append(a)
    all_numbers.append(b)
    all_numbers.append(c)
    count = 0
    # print(all_numbers)
    for num in all_numbers:
        if num > 0:
            count += 1
            if count == 1:
                # print(count)
                # print(num)
                # print('we are here')
                return True
    return False
    pass

print(numbers(2, 4, -3))
print(numbers(-4, 6, 8))
print(numbers(4, -6, 9))
print(numbers(-4, 6, 0))
print(numbers(4, 6, 10))
print(numbers(-14, -3, -4))