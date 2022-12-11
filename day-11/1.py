class Monkey:
    def __init__(self, items, function, test):
        self.items = items
        self.function = function
        self.test = test
        self.inspected = 0

    def turn(self):
        throws = []
        self.inspected += len(self.items)
        while len(self.items) > 0:
            item = self.items.pop(0)
            item = self.function(item)
            item //= 3
            throws.append([self.test(item), item])
        return throws

monkeys = [
    Monkey(
        [59, 65, 86, 56, 74, 57, 56], 
        lambda old : old * 17,
        lambda x : 3 if x % 3 == 0 else 6
    ),
    Monkey(
        [63, 83, 50, 63, 56],
        lambda old : old + 2,
        lambda x : 3 if x % 13 == 0 else 0
    ),
    Monkey(
        [93, 79, 74, 55],
        lambda old: old + 1,
        lambda x : 0 if x % 2 == 0 else 1
    ),
    Monkey(
        [86, 61, 67, 88, 94, 69, 56, 91],
        lambda old: old + 7,
        lambda x: 6 if x % 11 == 0 else 7
    ),
    Monkey(
        [76, 50, 51],
        lambda old: old * old,
        lambda x: 2 if x % 19 == 0 else 5
    ),
    Monkey(
        [77, 76],
        lambda old: old + 8,
        lambda x: 2 if x % 17 == 0 else 1,
    ),
    Monkey(
        [74],
        lambda old: old * 2,
        lambda x: 4 if x % 5 == 0 else 7,
    ),
    Monkey(
        [86, 85, 52, 86, 91, 95],
        lambda old: old + 6,
        lambda x: 4 if x % 7 == 0 else 5
    )
]

monkeys = [
    Monkey([79, 98], lambda x : x * 19, lambda x : 2 if x % 23 == 0 else 3),
    Monkey([54, 65, 75, 74], lambda x : x + 6, lambda x : 2 if x % 19 == 0 else 0),
    Monkey([79, 60, 97], lambda x : x * x, lambda x : 1 if x % 13 == 0 else 3),
    Monkey([74], lambda x : x + 3, lambda x : 0 if x % 17 == 0 else 1),
]

for i in range(20):
    for monkey in monkeys:
        result = monkey.turn()
        for c in result:
            monkeys[c[0]].items.append(c[1])
    #print([monkey.items for monkey in monkeys])
    print(f"finished round {i+1}")

s = [monkey.inspected for monkey in sorted(monkeys, key=lambda x : x.inspected)]
print(s[-2] * s[-1])