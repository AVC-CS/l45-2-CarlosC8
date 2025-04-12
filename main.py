import random


def main():
    total = 0
    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """

    numbers = []
    total = 0
    i = 0

    while total < 100:
        numbers.append(random.randint(1,10))
        total = total + numbers[i]
        i = i + 1

    idx = len(numbers)
    if total > 100:
        total = total - numbers[idx - 1]
        

    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
