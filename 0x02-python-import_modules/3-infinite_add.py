#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    count = len(argv) - 1
    if count == 0:
        print("0")
    else:
        sum = 0

    for i in range(1, count + 1):
        sum += int(argv[i])

    print("{:d}".format(sum))

