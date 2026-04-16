class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0

        indicator = 0
        sum = 0

        if s[0] == '-':
            indicator = 1
            s = s[1:]
        elif s[0] == '+':
            indicator = 0
            s = s[1:]

        INT_MAX = 2147483647
        INT_MIN = -2147483648

        for j in s:
            if j.isdigit():
                d = ord(j) - ord('0')
                sum = sum * 10 + d

                if indicator == 0 and sum >= INT_MAX:
                    return INT_MAX
                elif indicator == 1 and sum >= INT_MAX + 1:
                    return INT_MIN
            else:
                break

        if indicator == 1:
            return -1 * sum
        else:
            return sum