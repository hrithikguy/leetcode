class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        
        #preprocess nearest next and nearest prev
        #for each index, for each character
        
        def dist(i,j):
            return min(abs(i-j), len(ring) - abs(i-j))
        
        indexes_map = collections.defaultdict(list)
        for i,j in enumerate(ring):
            indexes_map[j].append(i)
        
        next_closest = {}
        prev_closest = {}
        
        #keys are chars, values are lists of ints
        #from position i, the closest next index with char is next_closest[char][i]
        for char in indexes_map.keys():
            cur_next = []
            cur_prev = []
            ptr = 0
            for i in range(len(ring)):
                cur_next.append(indexes_map[char][ptr])
                cur_prev.append(indexes_map[char][(ptr-1) % len(indexes_map[char])])
                if i == indexes_map[char][ptr]:
                    ptr = (ptr + 1) % len(indexes_map[char])
            next_closest[char] = cur_next
            prev_closest[char] = cur_prev
            
        # all the starting positions from the last stage 
        # second element is accumulated distance, first is index in ring
        prev_list = {0: 0}
        
        for i in range(len(key)):
            cur_char = key[i]
            state = {}
            # map from index to minimum cost
            
            for i in prev_list.keys():
                next_i = next_closest[cur_char][i]
                if next_i in state:
                    state[next_i] = min(state[next_i], dist(i, next_i) + prev_list[i])
                else:
                    state[next_i] = dist(i, next_i) + prev_list[i]
                prev_i = prev_closest[cur_char][i]
                if prev_i in state:
                    state[prev_i] = min(state[prev_i], dist(i, prev_i) + prev_list[i])
                else:
                    state[prev_i] = dist(i, prev_i) + prev_list[i]
                    
            prev_list = state
            
        return len(key) + min(prev_list.values())
        
        
                
        
        
