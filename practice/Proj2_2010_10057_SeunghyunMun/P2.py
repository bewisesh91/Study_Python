"""
**Instruction**
Please see instruction document.

"""
def P2(parentheses: str) -> bool:        
    ##### Write your Code Here #####
    result = []
    for i in parentheses :
        result.append(i)
        if len(result) > 1 :
            if (result[0] == '(' and result[1] == ')') or (result[0] == '[' and result[1] == ']') or (result[0] == '{' and result[1] == '}') :
                result = []
            else :
                return False
    return True
    ##### End of your code #####


