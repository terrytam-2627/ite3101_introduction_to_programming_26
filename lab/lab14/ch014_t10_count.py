from typing import List

def count(sequece: List[int], item:int)->int:
    result = 0
    for i in sequece:
        if i == item:
            result += 1
    return result