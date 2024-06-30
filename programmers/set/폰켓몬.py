def solution(nums):
    answer = 0
    N = len(nums)//2 
    set_nums = set(nums)
    if N >= len(set_nums):
        return len(set_nums)
    else:
        return N 
