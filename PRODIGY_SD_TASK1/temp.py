# Task 1
# Pujan Gampa
# Prodigy Infotech 

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def main():
    print("Temperature Unit Converter")
    print("1. Celsius to Fahrenheit and Kelvin")
    print("2. Fahrenheit to Celsius and Kelvin")
    print("3. Kelvin to Celsius and Fahrenheit")

    choice = int(input("Select conversion type (1,2,3): "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
        print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit and {kelvin} Kelvin.")
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius and {kelvin} Kelvin.")
    elif choice == 3:
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        print(f"{kelvin} Kelvin is equal to {celsius} degrees Celsius and {fahrenheit} degrees Fahrenheit.")
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
