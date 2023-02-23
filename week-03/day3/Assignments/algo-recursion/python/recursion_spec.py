from recursion_challenge import factorial, palindrome, bottles, roman_num

print(factorial(-4) == 'Invalid Input')
print(factorial(8) == 40320)
print(factorial(18) == 6402373705728000)
print(factorial(45) == 119622220865480194561963161495657715064383733760000000000)

print(palindrome('racecar') == True)
print(palindrome('Noon') == True)
print(palindrome('ciVic') == True)
print(palindrome('nice') == False)
print(palindrome(434) == True)
print(palindrome(123) == False)
print(palindrome('bomb') == False)
print(palindrome('Sore was I ere I saw Eros.') == True)
print(palindrome('A man, a plan, a canal -- Panama') == True)
print(palindrome('A men, a plan, a canal -- Panama') == False)

print(roman_num(1) =='I')
print(roman_num(3) == 'III')
print(roman_num(4) == 'IV')
print(roman_num(999) == 'CMXCIX')
print(roman_num(99)== 'XCIX')
print(roman_num(44) == 'XLIV')
print(roman_num(497) == 'CDXCVII')

print(bottles(5))
