"""Multiple Inheritance Program"""
class Camera:
    def __init__(self, camera_quality):
        self.camera_quality = camera_quality

    def display_camera_details(self):
        print(f"Camera Quality: {self.camera_quality} MP")

class MusicPlayer:
    def __init__(self, sound_quality):
        self.sound_quality = sound_quality

    def display_music_details(self):
        print(f"Sound Quality: {self.sound_quality}")

class SmartPhone(Camera, MusicPlayer):
    def __init__(self, brand, camera_quality, sound_quality):
        Camera.__init__(self, camera_quality)
        MusicPlayer.__init__(self, sound_quality)
        self.brand = brand

    def display_smartphone_details(self):
        print(f"--- {self.brand} Smartphone Details ---")
        self.display_camera_details()
        self.display_music_details()
        print(f"Brand: {self.brand}")

my_phone = SmartPhone("Galaxy S24", 200, "Dolby Atmos")

my_phone.display_smartphone_details()


""" Multilevel Inheritance Program Online Shopping System """
class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def display_product(self):
        print(f"Product: {self.product_name}")
        print(f"Price: ${self.price}")

class ElectronicProduct(Product):
    def __init__(self, product_name, price, brand, warranty):
        super().__init__(product_name, price)
        self.brand = brand
        self.warranty = warranty

    def display_electronic_product(self):
        self.display_product()
        print(f"Brand: {self.brand}")
        print(f"Warranty: {self.warranty} years")

class MobilePhone(ElectronicProduct):
    def __init__(self, product_name, price, brand, warranty, ram, storage):
        super().__init__(product_name, price, brand, warranty)
        self.ram = ram
        self.storage = storage

    def display_mobile_details(self):
        print("--- Mobile Phone Specifications ---")
        self.display_electronic_product()
        print(f"RAM: {self.ram} GB")
        print(f"Storage: {self.storage} GB")

my_mobile = MobilePhone("iPhone 15", 999, "Apple", 1, 6, 128)

my_mobile.display_mobile_details()