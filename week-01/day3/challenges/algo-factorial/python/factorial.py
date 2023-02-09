def factorial(num):
  if num < 0:
    return 'Invalid Input'
  print(num)
  if num == 0 or num == 1:
    return 1
  return num * factorial(num-1)


print(factorial(-4))
print(factorial(8) == 40320)
print(factorial(18) == 6402373705728000)
print(factorial(45) == 119622220865480194561963161495657715064383733760000000000)