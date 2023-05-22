class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
            print(f"Название Ресторана -  {self.restaurant_name} \nКухня:{self.cuisine_type}Русская.")

    def open_restaurant(self):
            print("Ресторан сейчас открыт.")


newRestaurant = Restaurant("Богодельня"," ")
print(newRestaurant.cuisine_type)

newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()