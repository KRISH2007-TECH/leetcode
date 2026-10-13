1class Solution(object):
2    def intToRoman(self, num):
3        values = [
4        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
5        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
6        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
7    ]
8
9        roman = ""
10        for value, symbol in values:
11            count = num // value
12            roman += symbol * count
13            num %= value
14
15        return roman
16
17        roman_list = [int_to_roman(i) for i in range(1, 4001)]
18
19        print(roman_list)