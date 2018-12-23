class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        mydeque = collections.deque()
        
        deck.sort(reverse = True)
        print deck
        for i in deck:
            mydeque.appendleft(i)
            end = mydeque.pop()
            mydeque.appendleft(end)
            # print mydeque
            
        x = mydeque.popleft()
        mydeque.append(x)
        # print mydeque
        return list(mydeque)
