class FreqStack(object):

    def __init__(self):
        self.freq = collections.Counter()
        self.maxfreq = 0
        self.group = collections.defaultdict(list)

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curfreq = self.freq[x] + 1
        self.freq[x] = curfreq
        if curfreq > self.maxfreq:
            self.maxfreq = curfreq
            
        self.group[curfreq].append(x)

    def pop(self):
        """
        :rtype: int
        """
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if self.maxfreq == self.freq[x] + 1 and self.group[self.maxfreq] == []:
            self.maxfreq -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
