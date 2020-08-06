from time import sleep
from ctypes import *

# Cursor position code from C --------------
STD_OUTPUT_HANDLE = -11

class COORD(Structure):
    pass

COORD._fields_ = [("X", c_short), ("Y", c_short)]

def printAt(r, c, s):
    h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))

    c = s.encode("windows-1252")
    windll.kernel32.WriteConsoleA(h, c_char_p(c), len(c), None, None)
# End of cursor position code --------------

def animateRangoli(size, wait):
    if size == None or wait == None:
        raise Exception('Invalid argument.')

    alphaRange = 30
    startChar = 'a'
    increment = size # Current position of word.

    while True:
        n = 1 + (4 * (size - 1))
        m = (2 * size) - 1
        numOfLetter = 1

        for i in range(m):
            next = 0
            currentIndex = increment % alphaRange # Goes from 0 to alphaRange - 1
            diff = 0
            for j in range(n):
                if j == ((n - ((2 * numOfLetter) - 1)) / 2) + next:
                    printAt(i, j, chr(ord(startChar) + currentIndex + diff))
                    if (next / 2) + 1 != numOfLetter:
                        next += 2
                    if j >= (n - 1) / 2: # Later half
                        if currentIndex + diff < alphaRange - 1:
                            diff += 1
                        else:
                            diff -= alphaRange - 1
                    else: # First half
                        if currentIndex + diff > 0:
                            diff -= 1
                        else:
                            diff += alphaRange - 1
                else:
                    printAt(i, j, '-')
            if i < (m - 1) / 2:
                numOfLetter += 2
            else:
                numOfLetter -= 2
        increment += 1
        sleep(wait)

if __name__ == '__main__':
    animateRangoli(7, 0.1)