class Monkey:
    def __init__(self, items, function, test, m):
        self.items = items
        self.function = function
        self.test = test
        self.m = m
        self.inspected = 0

    def turn(self):
        throws = []
        self.inspected += len(self.items)
        while len(self.items) > 0:
            item = self.items.pop(0)
            item = self.function(item) % self.m
            throws.append([self.test(item), item])
        return throws

m = 3 * 13 * 2 * 11 * 19 * 17 * 5 * 7
monkeys = [
    Monkey([59, 65, 86, 56, 74, 57, 56], lambda old : old * 17, lambda x : 3 if x % 3 == 0 else 6, m),
    Monkey([63, 83, 50, 63, 56], lambda old : old + 2, lambda x : 3 if x % 13 == 0 else 0, m),
    Monkey([93, 79, 74, 55], lambda old: old + 1, lambda x : 0 if x % 2 == 0 else 1, m),
    Monkey([86, 61, 67, 88, 94, 69, 56, 91], lambda old: old + 7, lambda x: 6 if x % 11 == 0 else 7, m),
    Monkey([76, 50, 51], lambda old: old * old, lambda x: 2 if x % 19 == 0 else 5, m),
    Monkey([77, 76], lambda old : old + 8, lambda x : 2 if x % 17 == 0 else 1, m),
    Monkey([74], lambda old : old * 2, lambda x : 4 if x % 5 == 0 else 7, m),
    Monkey([86, 85, 52, 86, 91, 95], lambda old : old + 6, lambda x : 4 if x % 7 == 0 else 5, m)
]

for i in range(10000):
    for monkey in monkeys:
        throws = monkey.turn()
        for throw in throws:
            monkeys[throw[0]].items.append(throw[1])

s = [monkey.inspected for monkey in sorted(monkeys, key=lambda x : x.inspected)]
print(s[-2] * s[-1])