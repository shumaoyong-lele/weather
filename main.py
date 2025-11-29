Temperature = float(input("请输入华氏度："))
def Calculate(Temperature):
    Celsius = (Temperature - 32) * 5 / 9
    Celsius = str(Celsius) + "°F"
    Temperature = str(Temperature) + "°C"
    return Celsius, Temperature

weather = Calculate(Temperature)
print(weather[0])
print(weather[1])