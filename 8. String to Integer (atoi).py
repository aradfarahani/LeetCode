class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if len(s) == 0:
            return 0
        sign = 1
        if s[0] == '-' :
            sign = -1
        num,i = 0,0
        if s[0] =='-' or s[0] == '+' :
            s=s[1:]
        for i in range(len(s)+1) :
            if i<len(s):
                if (s[i].isdigit()) :
                    num = num*10 + int(s[i])
                else :
                    a = num*sign
                    if a < -(2**31) :
                        return -(2**31)
                    elif a > (2**31)-1:
                        return (2**31)-1
                    else :
                        return a
            if i == len(s) :
                a = num*sign
                if a < -(2**31) :
                    return -(2**31)
                elif a > (2**31)-1:
                    return (2**31)-1
                else :
                    return a
