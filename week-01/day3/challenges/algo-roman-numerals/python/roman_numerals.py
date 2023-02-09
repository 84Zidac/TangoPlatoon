def to_roman(num):
    output = []
    ROMAN_NUMERAL_TO_ARABIC_MAP = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                                   'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    EVENLY_DIVISIBLE_TIMES = 0
    for key in ROMAN_NUMERAL_TO_ARABIC_MAP:
        EVENLY_DIVISIBLE_TIMES = num/ROMAN_NUMERAL_TO_ARABIC_MAP[key]
        while EVENLY_DIVISIBLE_TIMES >= 1:
            output.append(key)
            num = num - ROMAN_NUMERAL_TO_ARABIC_MAP[key]
            EVENLY_DIVISIBLE_TIMES -= 1
    print(output)
    return ''.join(output)
print(to_roman(1) == 'I')
print(to_roman(3) == 'III')
print(to_roman(4) == 'IV')