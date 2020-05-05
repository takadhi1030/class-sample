class User:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def display_profil(self):
        # display_profil() は Userクラスのインスタンスメソッド
        print(f"{self.name} 国籍: {self.country} {self.age}歳")

    def change_nationality(self, country_name):
        self.country = country_name


if __name__ == "__main__":
    Bob = User("Bob", 15, "USA")  # Userクラスをインスタンス化
    Bob.display_profil()
    Bob.change_nationality("China")
    Bob.display_profil()

    Tom = User("Tom", 57, "USA")
    Tom.display_profil()
    Tom.change_nationality("UK")
    Tom.display_profil()

    Ken = User("Ken", 49, "Japan")
    Ken.display_profil()
    Ken.change_nationality("Korea")
    Ken.display_profil()
