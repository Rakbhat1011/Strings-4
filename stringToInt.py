"""
Skip leading spaces, then check for optional sign (+ or -)
Convert digits until a non-digit is found, while checking for overflow/underflow
Clamp result to [-2^31, 2^31 - 1]
"""
"""
Time Complexity: O(n), scanning each character once
Space Complexity: O(1)
"""
class stringToInt:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  
        if not s:
            return 0
        
        sign, i = 1, 0
        if s[0] in ["-", "+"]:
            if s[0] == "-":
                sign = -1
            i += 1
        
        result = 0
        INT_MAX, INT_MIN = 2**31 - 1, -2**31

        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1
        
        return sign * result


if __name__ == "__main__":
    obj = stringToInt()
    print(obj.myAtoi("42"))            
    print(obj.myAtoi("   -42"))       
    print(obj.myAtoi("4193 with words")) 
    print(obj.myAtoi("words and 987"))
    print(obj.myAtoi("-91283472332")) 
    print(obj.myAtoi("91283472332")) 
