def factorial(x):
    if x < 0:
        return 'Invalid Input'
    if x == 1:
        return 1
    return x * factorial(x-1)


def palindrome(string, counter=0):
    if counter == 0:
        string = str(string).lower()
        for char in string:
            if not char.isalpha() and not char.isnumeric():
                string = string.replace(char, '')
    if len(string) < 2:
        return True
    elif string[0] == string[len(string)-1]:
        string = string[1:-1]
        return palindrome(string, 1)
    return False


def bottles(num):
    if num == 0:
        return (f"No more bottles of beer on the wall, \nno more bottles of beer.\nGo to the store and buy some more, \n99 bottles of beer on the wall.")
    elif num == 1:
        return (f"1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, \nno more bottles of beer on the wall.\n"+bottles(num-1))
    else:
        return (f"{num} bottles of beer on the wall, \n{num} bottles of beer,\nTake one down and pass it around, \n{num - 1} bottles of beer on the wall!\n"+bottles(num-1))


def roman_num(num, rom_num = None):
    output = [] if rom_num is None else rom_num
    print (output)
    rn_map = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,
              'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    if num == 0:
        print('returning output')
        return output
    even_div_times = 0
    for key in rn_map:
        even_div_times = num/rn_map[key]
        if even_div_times >= 1:
            output.append(key)
            num = num - rn_map[key]
            return (''.join(roman_num(num, output)))

