# Define Global Conversion Factors
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
