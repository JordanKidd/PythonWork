import time


def main():
    x = time.time()
    for i in range(0, 9999):
        print(i)

    current = time.time()
    print(str(current - x))


if __name__ == '__main__':
    main()