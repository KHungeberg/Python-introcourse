# ASSIGNMENT 5C: Temperature conversion:
    
# Problem definition
# Implement a function that converts temperatures between the three different units of measurement. The function
# must take three inputs: A decimal number T, which specifies the temperature and two strings, unitFrom and
# unitTo which specify the units to convert from and to. The strings must take one of the values Celsius,
# Fahrenheit, or Kelvin.

# Looking up a template of how different units of temperature is converted from one to another, we can define our 
# function as such: 
    
def convertTemperature(T, unitFrom, unitTo):
    if unitFrom=="Fahrenheit" and unitTo=="Celsius":
        T = (T-32)/1.8
    elif unitFrom=="Fahrenheit" and unitTo=="Kelvin":
        T = (T+459.67)/1.8
    elif unitFrom=="Celsius" and unitTo=="Kelvin":
        T = T+273.15
    elif unitFrom=="Celsius" and unitTo=="Fahrenheit":
        T = 1.8*T+32
    elif unitFrom=="Kelvin" and unitTo=="Fahrenheit":
        T = 1.8*T-459.67
    elif unitFrom=="Kelvin" and unitTo=="Celsius":
        T = T-273.15
    return T

print(convertTemperature(50.0, "Fahrenheit", "Celsius"))
