class MinStack:
    def __init__(self):
        self.min = []
        self.stack = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if not self.min or x < self.getMin():
            self.min.append((x,1))
        elif self.min and x == self.getMin():
            self.min[-1] = (x, self.getMinCount()+1)

    # @return nothing
    def pop(self):
        x = self.stack.pop()
        if x == self.getMin():
            if self.getMinCount() == 1:
                self.min.pop()
            else:
                self.min[-1] = (x, self.getMinCount() - 1)

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.min[-1][0]

    def getMinCount(self):
        return self.min[-1][1]
