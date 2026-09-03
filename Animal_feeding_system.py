class Food:
    def __init__(self,food_name):
        self.food_name=food_name
   
class Meat(Food):
    pass
    
class Vegetable(Food):
   pass
   
class Fruit(Food):
    pass
    
class Animal:
    def __init__(self,name):
         self.name=name
         self.eaten=[]
    def eat(self,food):
        self.food=food
    def can_eat(self):
        return False
    def show_diet(self):
          if self.can_eat():
             self.eaten.append(self.food.food_name)
          print(self.eaten)

class Owl(Animal):
     def can_eat(self):
         if isinstance(self.food,Food):
             if isinstance(self.food,Meat):
                 print(f"{self.name} can eat Meat.")
                 return True
             else:
                 print(f"{self.name} can't eat vegetable or fruit.")
                 return False
         else:
             print("This is not a food.")
             return False

class Mouse(Animal):
     def can_eat(self):
         if isinstance(self.food,Food):
             if isinstance(self.food,Vegetable) or isinstance(self.food,Fruit):
                 print(f"{self.name} can eat vegetable or fruit.")
                 return True
             else:
                 print(f"{self.name} can't' eat Meat.")
                 return False
         else:
             print("This is not a food.")
             return False
             
class Cat(Owl):
    pass            
flesh=Meat("Chicken")           
owl1=Owl("owl1")
owl1.eat(flesh)
owl1.show_diet()
kitty=Cat('Kitty')
kitty.eat(flesh)
kitty.show_diet()
Apple=Fruit("Apple")  
Stuart=Mouse("Stuart")
Stuart.eat(Apple)
Stuart.show_diet()

