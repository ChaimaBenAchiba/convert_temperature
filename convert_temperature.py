def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(value, unit, language):
    if unit.lower() == 'c':
        fahrenheit = celsius_to_fahrenheit(value)
        kelvin = celsius_to_kelvin(value)
        if language == 'en':
            return f"{value}°C is {fahrenheit:.2f}°F and {kelvin:.2f}K"
        else:
            return f"{value}°C est {fahrenheit:.2f}°F et {kelvin:.2f}K"
    elif unit.lower() == 'f':
        celsius = fahrenheit_to_celsius(value)
        kelvin = fahrenheit_to_kelvin(value)
        if language == 'en':
            return f"{value}°F is {celsius:.2f}°C and {kelvin:.2f}K"
        else:
            return f"{value}°F est {celsius:.2f}°C et {kelvin:.2f}K"
    elif unit.lower() == 'k':
        celsius = kelvin_to_celsius(value)
        fahrenheit = kelvin_to_fahrenheit(value)
        if language == 'en':
            return f"{value}K is {celsius:.2f}°C and {fahrenheit:.2f}°F"
        else:
            return f"{value}K est {celsius:.2f}°C et {fahrenheit:.2f}°F"
    else:
        if language == 'en':
            return "Invalid unit of measurement. Please use 'C', 'F', or 'K'."
        else:
            return "Unité de mesure invalide. Veuillez utiliser 'C', 'F' ou 'K'."

def main():
    language = input("Select language (en for English, fr for French): ").lower()
    if language not in ['en', 'fr']:
        print("Invalid language selection.")
        return

    try:
        value = float(input("Enter the temperature value: " if language == 'en' else "Entrez la valeur de la température : "))
        unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit, K for Kelvin): " if language == 'en' else "Entrez l'unité de mesure (C pour Celsius, F pour Fahrenheit, K pour Kelvin) : ")
        result = convert_temperature(value, unit, language)
        print(result)
    except ValueError:
        if language == 'en':
            print("Invalid input. Please enter a numeric temperature value.")
        else:
            print("Entrée invalide. Veuillez entrer une valeur de température numérique.")

if __name__ == "__main__":
    main()
