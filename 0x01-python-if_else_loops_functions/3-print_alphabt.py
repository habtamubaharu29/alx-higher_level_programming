#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if char(i) != 'e' and chr(i) != 'q':
        print('{:c}'.format(i), end='')
