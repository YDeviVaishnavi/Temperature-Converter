Unit = input("Is the Temperature is in Celsius or Fahrenheit (C/F/K): ")
Temp = float(input("Enter the Temperature: "))

if Unit == "C" :
    Temp = round((9 * Temp) / 5 +32,1)
    print (f"Temperature in Fahrenheit is: {Temp}°F")
    Temp = round(Temp + 273.15,1)
    print (f"Temperature in Kelvin is: {Temp}°K")
elif Unit == "F" :
    Temp = round((Temp-32) * 5 / 9,1)
    print (f"Temperature in Celsius is: {Temp}°C")
    Temp = round(((Temp - 32)*5)/9 + 273.15,1)
    print (f"Temperature in Kelvin is: {Temp}°K")
elif Unit == "K":
    Temp = round(Temp - 273.15,1)
    print (f"Temperature in Celsius is: {Temp}°C")
    Temp = round(((Temp - 273.15)*9)/5 +32,1) 
    print (f"Temperature in Fahrenheit is: {Temp}°F")
else:
    print(f"{Temp}is a invalid unit of measurement")