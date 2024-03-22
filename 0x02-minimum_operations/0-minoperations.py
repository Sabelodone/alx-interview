def minOperations(n):
    if n <= 1:
        return 0
    
    min_ops = 0
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            min_ops += divisor
            n //= divisor
        divisor += 1
    
    return min_ops