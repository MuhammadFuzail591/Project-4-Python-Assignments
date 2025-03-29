import random

N_NUMBERS = 10
MAX_RANGE = 100
MIN_RANGE = 1

def main():
    for i in range(N_NUMBERS):
        print(random.randint(MIN_RANGE, MAX_RANGE),end=' ')


if __name__ == '__main__':
    main()