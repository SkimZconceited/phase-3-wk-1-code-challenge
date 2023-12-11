def numbers(a, b, c):
    all_numbers = []
    all_numbers.append(a)
    all_numbers.append(b)
    all_numbers.append(c)
    count = 0
    print(all_numbers)
    for num in all_numbers:
        if num > 0:
            count += 1
            if count == 1:
                print(count)
                print(num)
                print('we are here')
                return True
            else:
                print('we are here else')
                return False
    pass

numbers(2, 4, -3)
numbers(-4, 6, 8)
numbers(4, -6, 9)
numbers(-4, 6, 0)
numbers(4, 6, 10)
numbers(-14, -3, -4)