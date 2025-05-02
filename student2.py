class student:
    year = 2
    name = "Nziza"

    def introduction(self):
        print("Hi i am a student")

    def details(self):
        print("My name is", self.name)
        print("I am in Year", self.year)

ob = student()
ob.introduction()
ob.details()