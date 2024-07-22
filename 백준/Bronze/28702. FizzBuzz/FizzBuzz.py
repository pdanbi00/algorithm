for i in range(3):
    line = input()
    if line not in ['Fizz', 'Buzz', 'FizzBuzz']:
        num = int(line) + (3-i)
if num:
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)