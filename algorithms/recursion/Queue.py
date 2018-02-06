class Queue:
    def __init__(self):
        self.q = []

    def push(self,x):
        self.q.append(x)

    def pop(self):
        if self.q:
            print(self.q[0])
            del self.q[0]
        else:
            print(-1)

    def size(self):
        print(len(self.q))

    def empty(self):
        if self.q:
            print(0)
        else:
            print(1)
    def front(self):
        if self.q:
            print(self.q[0])
        else:
            print(-1)
    def back(self):
        if self.q:
            print(self.q[-1])
        else:
            print(-1)

n = int(input())

q = Queue()
for i in range(n):

    s = str(input())
    s = s.split(' ')

    if s[0] == 'push':
        q.push(s[1])
    elif s[0] == 'front':
        q.front()
    elif s[0] == 'pop':
        q.pop()
    elif s[0] == 'size':
        q.size()
    elif s[0] == 'empty':
        q.empty()
    elif s[0] == 'back':
        q.back()