#!/usr/bin/python3
if __name__ == '__main__':
    import sys
if len(sys.argv) == 1:
    print(0, 'arguments:')
else:
    if len(sys.argv) is 2:
        print(len(sys.argv) - 1, 'arguments:')
        print("{}:".format(len(sys.argv) - 1), sys.argv[1])
    else:
        print(len(sys.argv) - 1, 'arguments:')
        for a in range(1, len(sys.argv)):
            print('{}:'.format(a), sys.argv[a])
