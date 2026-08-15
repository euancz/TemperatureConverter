choices = {1: "Farenheit to Celcius", 
           2: "Celcius To Farenheit", 
        3: "Celcius To Kelvin"}
print(f"=" * 50)

print(f"This is a Temperature Converter pick from the following: ")
print(f"=" * 50)

for key, value in choices.items():
    print(f"{key} = {value}")
print(f"=" * 50)
choice = int(input("Enter choice: "))
print(f"=" * 50)

if(choice == 1):
    Farenheit = int(input("Enter Farenheit"))
    Celcius = int(input("Enter Celcius"))
    print(f"=" * 50)
    
elif (choice == 2):
    Celcius = int(input("Enter Celcius"))
    Farenheit = int(input("Enter Farenheit"))
    print(f"=" * 50)
    
elif (choice == 3):
    Celcius = int(input("Enter Celcius: "))

    celsius_kelvin = Celcius + 273.15

    print(f"{celsius_kelvin:.2f}K")
    print(f"=" * 50)

else:
    print("Invalid Choice")
    print(f"=" * 50)