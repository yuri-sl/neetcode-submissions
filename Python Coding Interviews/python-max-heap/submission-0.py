import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    max_heaped = []
    array = []
    for num in nums:
        heapq.heappush(max_heaped,-num)
    while max_heaped:
        top = -heapq.heappop(max_heaped)
        array.append(top)
    return array





# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
