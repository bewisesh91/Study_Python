"""
**Instruction**
<Factor into two prime numbers>
Input of P2 function is natural number.
P2 function returns whether the input nubmer could be factored into two prime numbers.
Do not worry about invalid input.

>>> P2(6) #2 * 3
True

>>> P2(9) #3 * 3
True

>>> P2(12) # 2 * 2 * 3
False

>>> P2(7) # 7
False


"""

def P2(n:int) -> bool:        
    ##### Write your Code Here #####
    
    def prime_num(n) :
        count = 0
        for i in range(1, n+1) :
            if n % i == 0 :
                count += 1
        if count == 2 :
            return True
        else :
            return False
    
    if prime_num(n) :
        return False
    else :
        count = 0
        num = 2
        result = []
        while count < 2 :
            if n % num == 0 :
                count += 1
                result.append(num)
                n2 = n // num
                if n2 % num == 0 :
                    count += 1
                    result.append(n)
                    if n2 // num == 1 :
                        return True
                    else :
                        return False
                else :
                    num += 1
            else :
                num += 1
        
        if len(result) == 2 :
            for i in result :
                if not prime_num(i) :
                    return False
                else :
                    pass
            return True
        else :
            return False
    ##### End of your code #####
