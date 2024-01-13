from collections import deque 
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        cnt = [1e9]*len(nums)

        def BFS(idx):
            q = deque()
            q.append(idx)
            cnt[idx] = 0 
            while q: 
                idx = q.popleft()
                for i in range(nums[idx],-1,-1):
                    if idx+i < n and cnt[idx+i] == 1e9:
                        if idx+i == n-1: 
                            cnt[idx+i] = min(cnt[idx]+1,cnt[idx+i])  
                        q.append(idx+i)
                        cnt[idx+i] = cnt[idx]+1
        BFS(0)

        return cnt[-1] 
       
