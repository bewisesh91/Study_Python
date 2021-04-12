"""
**Instruction**
Please see instruction document.

"""
def P1(path: str) -> str:        
    ##### Write your Code Here #####
    path = path.replace('//', '/')
    path = path.split('/')
    result = ''
    for i in path :
        if i == '.' or i == '' :
            pass
        elif i == '..' :
            result = result[:-2]
        else :
            result += f'{i}/'
    result = f'/{result[:-1]}'

    return result
    ##### End of your code #####
