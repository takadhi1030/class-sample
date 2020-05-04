class User:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country


if __name__ == "__main__":
    Bob = User("Bob", 15, "USA")  # Userクラスをインスタンス化

    print(Bob)  # <__main__.User object at 0x0000016ECE2F7400>
    print(Bob.name)  # Bob
    print(Bob.age)  # 15
    print(Bob.country)  # 15

    Tom = User("Tom", 57, "USA")
    print(Tom)
    print(Tom.name)
    print(Tom.age)
    print(Tom.country)

    Ken = User("Ken", 49, "Japan")
    print(Ken)
    print(Ken.name)
    print(Ken.age)
    print(Ken.country)
