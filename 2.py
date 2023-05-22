class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана - {self.restaurant_name} \nКухня: {self.cuisine_type}.")

        def open_restaurant(self):
            print("Ресторан сейчас открыт")



    restaurant1 = Restaurant("В большой семье клювом не щелкают!", "Русская")
    restaurant2 = Restaurant("Я такое дома вкуснее могу сделать!", "Домашняя")
    restaurant3 = Restaurant("Почему такие маленькие порции? ", "Японская")

    # Вызываем метод describe_restaurant() для каждого экземпляра
    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()