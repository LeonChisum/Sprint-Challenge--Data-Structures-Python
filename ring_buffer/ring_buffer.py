class RingBuffer:
    def __init__(self, capacity=1):
        self.capacity = capacity
        self.items = []
        self.oldest_item = 0

    def append(self, item):
        # checking to see if my list is below the capacity
        if len(self.items) < self.capacity:
            self.items.append(item)
        #     once the list is at capacity
        elif len(self.items) == self.capacity:
            # replacing the item in the list at the index of the oldest item
            self.items[self.oldest_item] = item
            # setting the next oldest item index based on the given capacity
            self.oldest_item = (self.oldest_item + 1) % self.capacity

    def get(self):
        if len(self.items) <= self.capacity:
            return self.items
        else:
            return self.items[self.oldest_item:]+self.items[:self.oldest_item]