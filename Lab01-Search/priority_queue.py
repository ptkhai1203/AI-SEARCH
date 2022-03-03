import sys

class priorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == 0

    def push(self, data):
        self.queue.append(data)

    def pop(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i] < self.queue[min] :
                    min = i
            res = self.queue[min]
            del self.queue[min]
            return res
        except error:
            print()
            exit()