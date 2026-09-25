def cube(number: int) -> int:
    return number * number * number

from typing import Any
def by_three(number:int)-> Any:
    if number % 3 ==0:
        return cube(number)
    else:
       return False
    
