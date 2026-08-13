def celsius_to_fahrenheit(func):
    def wrapper(celsius):
        fahrenheit = celsius * 1.8 + 32
        return func(fahrenheit)

    return wrapper


@celsius_to_fahrenheit
def show_temperature(temp):
    print(f"Function received: {temp}°F")


show_temperature(30)