class User:
    def __init__(self, name, age):
        self.name = name


if __name__ == "__main__":
    user1 = User("Bob", 15)  # Userクラスをインスタンス化

    print(user1)  # <__main__.User object at 0x0000016ECE2F7400>
    print(user1.name)  # Bob

    user2 = User("Tom", 57)
    print(user2)
    print(user2.name)

    user3 = User("Ken", 49)
    print(user3)
    print(user3.name)
