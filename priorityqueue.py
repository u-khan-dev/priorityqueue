class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ', '.join([i.name for i in self.queue])

    def insert(self, data):
        self.queue.append(data)

    def isEmpty(self):
        return len(self.queue) == 0

    def pop_and_delete(self):
        max_key = 0

        for i in range(len(self.queue)):
            if self.queue[i].priority > self.queue[max_key].priority:
                max_key = i

        item = self.queue[max_key]
        del self.queue[max_key]
        return item.name
