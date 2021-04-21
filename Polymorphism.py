#Parent Class User
class Person:
    name = "Unknown"
    ability = "Unknown"
    gender = "Unknown"
    age = None

    def information(self):
        msg = "\nName: {}\nAbility: {}\nGender: {}\nAge: {}" \
              .format(self.name, self.ability, self.gender, self.age)
        return msg

#child class
class Hero(Person):
    name = "Hulk"
    ability = "Super Strength"
    gender = "Male"
    age = 32

    def strength(self):
        msg = "\nDue to Gamma radiation, the Hulk turns green and has super strength!"
        return msg

#another child class
class Villain(Person):
    name = "Lex Luthor"
    ability = "Super Smart"
    gender = "Male"
    age = "41"

    def smarts(self):
        msg = "\nLuthor's genius intellect makes him very powerful and dangerous!"
        return msg
    
if __name__ == "__main__":
    hero = Hero()
    print(hero.information())
    print(hero.strength())

    villain = Villain()
    print(villain.information())
    print(villain.smarts())


