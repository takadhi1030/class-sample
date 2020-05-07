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
    def __init__(self, value, step):
        self.value = value
        self.step = step

    def increase(self):
        self.value += self.step

if __name__ == "__main__":
    counter_1 = Counter(value=0, step=1)
    print(counter_1.value)
    counter_1.increase()
    print(counter_1.value)

    counter_2 = Counter(value=15, step=3)
    print(counter_2.value)
    counter_2.increase()
    print(counter_2.value)
