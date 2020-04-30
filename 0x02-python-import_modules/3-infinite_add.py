#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    for str in range(len(sys.argv)):
        if str == 0:
            continue
        else:
            sum += int(sys.argv[str])
    print("{}".format(sum))
