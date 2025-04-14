class StockSpanner:

    def __init__(self):
        self.stack = []
        self.count = []

    def next(self, price: int) -> int:
        count = 1
        
        while( self.stack and self.stack[-1] <= price):
            val = self.count[-1]
            self.stack.pop()
            self.count.pop()
            count += val
            
            
        self.stack.append(price)
        self.count.append(count)
            
        return count