def process(number):
    if number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    elif number % 6 == 0:
        return 'Fizz'
    elif number % 10 == 0:
        return 'Buzz'
    elif number % 15 == 0:
        return 'FizzBuzz'
    else:
        return number

if __name__ == '__main__':
    for i in range(1, 101):
        print(process(i))  