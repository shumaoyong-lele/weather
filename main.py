Temperature = float(input("请输入华氏度："))
def Calculate(Temperature):
    Celsius = (Temperature - 32) * 5 / 9
    Celsius = str(Celsius) + "°F"
    Temperature = str(Temperature) + "°C"
    return Celsius, Temperature

Celsius = Calculate(Temperature)[1]
Temperature = Calculate(Temperature)[0]
print(f"您输入的是{Temperature}，转换后的华氏度为{Celsius}")
