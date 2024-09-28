"""# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
CELSIUS_TO_FAHRENHEIT_BASE = 32


# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - CELSIUS_TO_FAHRENHEIT_BASE) * FAHRENHEIT_TO_CELSIUS_FACTOR


# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit (celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + CELSIUS_TO_FAHRENHEIT_BASE


# Main function for user interaction and input validation
def main():
    try:
        temp_input = input('Enter the temperature to convert: ')
        temperature = float(temp_input)
        unit = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').strip().upper()

        if unit == 'F':
            celsius = convert_to_celsius(temperature)
            print(f"{temperature} ْF is {celsius} ْC")
        elif unit == 'C':
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature} ْC is {fahrenheit} ْF")
        else:
            print("Invald unit. Please enter 'C' for Clesius or 'F' for Fahrenheit")
    except ValueError:
            print('Invald temperature. Please enter a numeric value.')


if __name__ == '__main__':
     main()
     """

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global factor"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global factor"""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Prompt the user to enter a temperature
        temperature = float(input("Enter the temperature to convert: "))
        
        # Prompt the user to specify the unit (Celsius or Fahrenheit)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            # Convert Fahrenheit to Celsius
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is {result}°C")
        
        elif unit == "C":
            # Convert Celsius to Fahrenheit
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result}°F")
        
        else:
            print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global factor"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global factor"""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Prompt the user to enter a temperature
        temperature = float(input("Enter the temperature to convert: "))
        
        # Prompt the user to specify the unit (Celsius or Fahrenheit)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            # Convert Fahrenheit to Celsius
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is {result}°C")
        
        elif unit == "C":
            # Convert Celsius to Fahrenheit
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result}°F")
        
        else:
            print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
