choices = {1: "Fahrenheit to Celcius", 
           2: "Celcius To Fahrenheit", 
           3: "Celcius To Kelvin",
           4: "Exit"}

print(f"=" * 50)
while True:
    print(f"This is a Temperature Converter pick from the following: ")

    print(f"=" * 50)

    for key, value in choices.items():
        print(f"{key} = {value}")

    print(f"=" * 50)

    choice = int(input("Enter choice: "))

    print(f"=" * 50)

    if (choice == 1):
        Fahrenheit = float(input("Enter Fahrenheit: "))
        Celsius = (Fahrenheit - 32) * 5 / 9
        print(f"Celsius: {Celsius:.2f}")
        print("=" * 50)
        

    elif (choice == 2):
        Celcius = int(input("Enter Celcius: "))
        Fahrenheit = (Celcius * 9/5) + 32
        print(f"Fahrenheit: {Fahrenheit:.2f}")
        print(f"=" * 50) 
        
    
    elif (choice == 3):
        Celcius = int(input("Enter Celcius: "))
        celsius_kelvin = Celcius + 273.15
        print(f"{celsius_kelvin:.2f}K")
        print(f"=" * 50)
        

    elif (choice == 4):
        print("You have exited the program.")
        print(f"=" * 50)
        break

    else:
        print("Invalid Choice")
        print(f"=" * 50) 
