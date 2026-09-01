import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    alist = []
    while len(heap) >0:
        for x in heap:
            alist.append(heapq.heappop(heap))
    return alist


# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
