class User:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country


if __name__ == "__main__":
    Bob = User("Bob", 15, "USA")  # Userクラスをインスタンス化

    Tom = User("Tom", 57, "USA")

    Ken = User("Ken", 49, "Japan")
