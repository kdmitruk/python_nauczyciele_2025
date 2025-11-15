class Punkt:
    def __init__(self):
        self.x = 0
        self.y = 0


if __name__ == '__main__':
    p = Punkt()
    print(p.x, p.y)

    q = Punkt()

    p.x = 5
    p.y = 10
    print(p.x, p.y)
    print(q.x, q.y)



