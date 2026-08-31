from typing import List
from sortedcontainers import SortedDict


def remove_keys(sorted_dict: SortedDict[str, int], keys: List[str]) -> SortedDict[str, int]:
    for x in keys:
        if x in sorted_dict:
            sorted_dict.pop(x)
    return sorted_dict


def get_values_before_target(sorted_dict: SortedDict[str, int], target: str) -> List[int]:
    values_list = []
    found = False
    if target in sorted_dict and not found:
        for k,v in sorted_dict.items():
            if found:
                break
            if k == target:
                found = True
                continue
            else:
                values_list.append(v)
    return values_list


# do not modify below this line
print(remove_keys(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35}), ['Bob']))
print(remove_keys(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}), ['Bob', 'David']))
print(remove_keys(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40, 'Eve': 45}), ['Alice', 'Eve']))

print(get_values_before_target(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35}), 'Bob'))
print(get_values_before_target(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}), 'David'))
print(get_values_before_target(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}), 'Charlie'))
print(get_values_before_target(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}), 'Bob'))
print(get_values_before_target(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}), 'Alice'))
