def slow_division(dividend, divisor):
    quotient = 0
    remainder = 0
    
    for i in range(len(bin(dividend))-2):
        remainder = (remainder << 1) | ((dividend >> (len(bin(dividend))-2-i-1)) & 1)
        
        if remainder >= divisor:
            remainder -= divisor
            quotient = (quotient << 1) | 1
        else:
            quotient = (quotient << 1)
    
    return quotient, remainder


def fast_division(dividend, divisor):
    quotient = 0
    remainder = dividend
    sign = 0
    
    for i in range(len(bin(dividend))-2):
        remainder = (remainder << 1) | ((dividend >> (len(bin(dividend))-2-i-1)) & 1)
        quotient = (quotient << 1)
        
        if remainder >= 0:
            remainder -= divisor
            quotient |= 1
        else:
            remainder += divisor
    
    return quotient, remainder


# Test the slow division algorithm
dividend = 50
divisor = 7
quotient, remainder = slow_division(dividend, divisor)
print(f"Slow Division Result:")
print(f"Quotient: {quotient}")
print(f"Remainder: {remainder}")

# Test the fast division algorithm
dividend = 50
divisor = 7
quotient, remainder = fast_division(dividend, divisor)
print(f"\nFast Division Result:")
print(f"Quotient: {quotient}")
print(f"Remainder: {remainder}")