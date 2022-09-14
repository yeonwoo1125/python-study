class Calculator:
    def __init__(self, li):
        self.li = li

    def sum(self):
        print(sum(self.li))

    def avg(self):
        print(sum(self.li) / len(self.li))


cal1 = Calculator([1, 2, 3, 4, 5])
cal1.sum()
cal1.avg()

cal2 = Calculator([6, 7, 8, 9, 10])
cal2.sum()
cal2.avg()
