#testing:
Cvalues=[-40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Fvalues=[-40.0, -22.0, -4.0, 14.0, 32.0, 50.0, 68.0, 86.0, 104.0, 122.0, 140.0, 158.0, 176.0, 194.0, 212.0]

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def print_menu():
    print("\nTemperature Conversion Menu:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

def main():
    while True:
        print_menu()
        choice = input("Select an option (1-3): ")
        if choice == "1":
            temp = float(input("Enter temperature in Celsius: "))
            print(f"{temp}°C = {celsius_to_fahrenheit(temp):.2f}°F")
        elif choice == "2":
            temp = float(input("Enter temperature in Fahrenheit: "))
            print(f"{temp}°F = {fahrenheit_to_celsius(temp):.2f}°C")
        elif choice == "3":
            print("Goodbye")
            break
       
       
        else:
            print("Invalid choice. Please select a number from 1 to 5.")


main()