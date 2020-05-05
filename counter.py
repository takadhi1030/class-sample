"""
演習: 下記のコードが正しく動作するようなCounter classを実装せよ
"""


# if __name__ == "__main__":
# counter_1 = Counter(0)
# print(counter_1.value) 0が出力される

# counter_1.increase()
# print(counter_1.value) 1が出力される

# counter_1.increase()
# print(counter_1.value) 2が出力される

class Counter:
    def __init__(self, value):
        self.value = value

    def increase(self):
        self.value += 1

    def increase3(self):
        self.value += 3


if __name__ == "__main__":
    counter_1 = Counter(0)
    print(counter_1.value)

    counter_1.increase()
    print(counter_1.value)

    counter_1.increase()
    print(counter_1.value)

    counter_2 = Counter(15)
    print(counter_2.value)

    counter_2.increase3()
    print(counter_2.value)

    counter_2.increase3()
    print(counter_2.value)
