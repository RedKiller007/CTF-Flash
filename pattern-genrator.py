#!/usr/bin/env python2
import sys
import struct


def char_generator(length):
    chartr = ''
    alph = ['A', 'a', '0']
    while len(chartr) != length:
        chartr += alph[len(chartr) % 3]
        if len(chartr) % 3 == 0:
            alph[2] = chr(ord(alph[2]) + 1)
            if alph[2] > '9':
                alph[2] = '0'
                alph[1] = chr(ord(alph[1]) + 1)
                if alph[1] > 'z':
                    alph[1] = 'a'
                    alph[0] = chr(ord(alph[0]) + 1)
                    if alph[0] > 'Z':
                        alph[0] = 'A'
    return chartr


def main():
    if len(sys.argv) < 3 or sys.argv[1].lower(): #not in ['gener']:
        sys.exit(255)

    CMD = sys.argv[1].lower()
    Val_ID = sys.argv[2]

    if CMD == 'gener':
        print char_generator(int(Val_ID))
    else:
        if len(sys.argv) == 4:
            try:
                buffer_len = int(sys.argv[3])
            except ValueError:
                sys.exit(254)
if __name__ == '__main__':
    main()
