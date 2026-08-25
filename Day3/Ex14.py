class Camera:
    def take_photo(self):
        print("Photo taken")


class Phone:
    def call(self):
        print("Calling")


class SmartPhone(Camera, Phone):
    pass


phone = SmartPhone()

phone.take_photo()
phone.call()