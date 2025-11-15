class Punkt:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

if __name__ == '__main__':
    p = Punkt()
    print(p.x, p.y)

    q = Punkt(3, 4)

    p.x = 5
    p.y = 10
    print(p.x, p.y)

    q.move(1, 2)
    print(q.x, q.y)



