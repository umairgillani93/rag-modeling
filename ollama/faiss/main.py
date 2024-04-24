import os 
import sys 
import numpy as np 
from typing import List


def distance(x1: List[int], x2: List[int]) -> List[int]:
    new_list: List[int] = []

    for (x1i, x2i) in list(zip(x1, x2)):
        new_list.append(x2i - x1i)

    return new_list

def argmin(arr: List[int]) -> int:
    return np.argmin(arr)


if __name__ == '__main__':
    X = [
        [1,2,3,4],
        [2,3,4,5],
        [3,4,5,6],
        [4,5,6,7]
    ]
    
        
