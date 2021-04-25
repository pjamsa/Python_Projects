from abc import ABC, abstractmethod
class cat(ABC):
    def catNip(self, quantity):
        print("Your cat needs {} of Cat nip a day.".format(quantity))
        @abstractmethod
        def food(self, quantity): ##abstract property user can't see
            pass

class OverFed(cat):
    def food(self, quantity):
        print("You fed your cat {} of CatNip two times today, that's too much!".format(quantity))

obj = OverFed()
obj.catNip("1 cup")
obj.food("1 cup")


