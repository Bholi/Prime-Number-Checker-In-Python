print('Prime Number Checker !')
n = int(input('Enter any number : '))


def prime_check(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    if count == 2:
        print('Prime Number')
    else:
        print('Not a prime number')


prime_check(number=n)
