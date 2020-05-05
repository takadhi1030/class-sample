class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return self.first_name + self.family_name

    def display_profil(self):
        print(f"Name: {self.full_name()}, Age: {self.age}")


if __name__ == "__main__":
    Tom = Customer("Tom", "Ford", 57)
    Ken = Customer("Ken", "Yokoyama", 49)

    Tom.display_profil()  # "Name: Tom Ford, Age: 57"と出力する
    Ken.display_profil()
