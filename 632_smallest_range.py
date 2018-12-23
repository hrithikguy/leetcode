class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        
        all_elems = collections.defaultdict(list)
        for i,j in enumerate(nums):
            for k in j:
                all_elems[k].append(i)
                
        for i in all_elems:
            print i, all_elems[i]
            
        best_range = [-100000, 100000]
        smallest_range = 200001
        
        # seen = [0 for arr in nums]
        # all_seen = [1 for arr in nums]
        cur_range = [-200001 for arr in nums]
        all_seen = False
        
        keys = sorted(all_elems.keys())
        # print keys
        for i in keys:
            for j in all_elems[i]:
                cur_range[j] = i
            # print cur_range
            if all_seen == True or -200001 not in cur_range:
                all_seen = True
                
                if max(cur_range) - min(cur_range) < smallest_range:
                    best_range = [min(cur_range), max(cur_range)]
                    smallest_range = max(cur_range) - min(cur_range)
                    
        return best_range
            
