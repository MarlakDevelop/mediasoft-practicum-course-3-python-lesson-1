def problem_1():
    for i in range(1, 100 + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')


def problem_2(a: list[int], b: list[int]) -> list[int]:
    if len(a) != len(b):
        return a
    b = sorted([{"index": i, "value": b[i]} for i in range(len(b))], key=lambda x: x["value"])
    return [a[elem["index"]] for elem in b]


def problem_3(strings: list[str]) -> list[str]:
    if len(strings) == 0:
        return []
    first_string = strings[0]
    letters = []
    for char in first_string:
        new_strings = []
        for string in strings:
            if char in string:
                new_strings.append(string.replace(char, '', 1))
            else:
                break
        else:
            letters.append(char)
            strings = new_strings[:]
    return letters


def problem_4(number: str) -> int:  # XD
    if len(number) == 0:
        return 0
    chars_weights = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    for i in range(len(number) - 1):
        current_number = chars_weights[number[i]]
        next_number = chars_weights[number[i + 1]]
        if current_number < next_number:
            result -= current_number
        else:
            result += current_number
    result += chars_weights[number[-1]]
    return result


def main():
    problem_1()
    print(problem_2([1, 4, 6], [11, 33, 22]))
    print(problem_3(["bella", "label", "roller"]))
    print(problem_3(["cool", "lock", "cook"]))
    print(problem_4('II'))
    print(problem_4('XXVII'))
    print(problem_4('IV'))
    print(problem_4('IX'))
    print(problem_4('XL'))
    print(problem_4('XC'))
    print(problem_4('CD'))
    print(problem_4('CM'))
    print(problem_4('CMXI'))


if __name__ == '__main__':
    main()
