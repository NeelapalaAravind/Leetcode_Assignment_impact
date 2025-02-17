class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        lists = list(map(str,nums))
        n = len(lists)
        for i in range(n):
            for j in range(i+1,n):
                if lists[i]+lists[j] < lists[j]+lists[i]:
                    lists[i],lists[j] = lists[j],lists[i]
        
        final_answer = ''.join(lists)
        if final_answer[0] == "0":
            return "0"
            
        return final_answer
        