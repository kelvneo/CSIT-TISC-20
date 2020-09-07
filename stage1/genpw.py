#!/usr/bin/python3

with open('pwlist.txt', 'w+') as f:
    for i in range(0, 0xffffff + 1):
        f.write('{:06x}\n'.format(i))


