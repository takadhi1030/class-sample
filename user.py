class User:
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    user1 = User("Bob")  # Userクラスをインスタンス化

    print(user1)  # <__main__.User object at 0x0000016ECE2F7400>
    print(user1.name)  # Bob
