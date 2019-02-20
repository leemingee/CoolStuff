'''
Created by Ming Li at 2019-02-12

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''

def counter(lst, target):
    cnt = 0
    dup = 0
    lst = list(set(lst))
    reverse_dict = {
        (target - elem): i for i, elem in enumerate(lst)
    }
    for j, num in enumerate(lst):
        idx = reverse_dict.get(num, None)
        if idx is not None:
            # print([lst[idx],lst[j]])
            cnt += 1
            if j == idx:
                dup += 1
    return int((cnt+dup)/2)

lst = [2,3,4,5,5,5,5,5,6,7,8]
target = 10
# print(counter(lst, target))
