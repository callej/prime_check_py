import re


def prime_check():
    num = int(input("Type a number to see if that is a prime: "))
    if re.match("^.?$|^(..+?)\\1+$", " " * num):
        print(f'{num} is not a prime\n')
    else:
        print(f'{num} is a prime\n')


def prime_print():
    print(f'The prime numbers up to 100:')
    for i in range(0, 101):
        if not re.match("^.?$|^(..+?)\\1+$", " " * i):
            print(i)


def main():
    prime_check()
    prime_print()


if __name__ == '__main__':
    main()

