import sys

Zero = ["   ***   ",
        "  *   *  ",
        " *     * ",
        " *     * ",
        " *     * ",
        "  *   *  ",
        "   ***   "]
One = ["  *  ",
       " **  ",
       "  *  ",
       "  *  ",
       "  *  ",
       "  *  ",
       " *** "]
Two = ["  ***  ",
       " *   * ",
       " *   * ",
       "    *  ",
       "   *   ",
       "  *    ",
       " ***** "]
Three = ["  ***  ",
         " *   * ",
         "     * ",
         "  ***  ",
         "     * ",
         " *   * ",
         "  ***  "]
Four = ["    *   ",
        "   **   ",
        "  * *   ",
        " *  *   ",
        " ****** ",
        "    *   ",
        "    *   "]
Five = ["  ****  ",
        "  *     ",
        "  *     ",
        "  ***   ",
        "     *  ",
        "     *  ",
        "  ***   "]
Six = ["    *  ",
       "   *   ",
       "  *    ",
       " ****  ",
       " *   * ",
       " *   * ",
       "  ***  "]
Seven = [" ***** ",
         "     * ",
         "    *  ",
         "   *   ",
         "  *    ",
         " *     ",
         " *     "]
Eight = ["  ***  ",
         " *   * ",
         " *   * ",
         "  ***  ",
         " *   * ",
         " *   * ",
         "  ***  "]
Nine = ["  **** ",
        " *   * ",
        " *   * ",
        "  **** ",
        "     * ",
        "     * ",
        "     * "]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        p = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            #line += digit[row].replace("*", str(number)) + "  "
            #print(digit[row])
            for i in digit[row]:
                if i == "*":
                    p += str(number)
                else: p += " "
                    
            #print(digit)
            #line += digit[row] + "  "
            column += 1
        print(p)
        row += 1
    
except IndexError:
    print("usage: bigdigits.py <number>")
except ValueError as err:
    print(err, "in", digits)
            















