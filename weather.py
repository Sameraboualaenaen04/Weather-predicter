import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # Get the directory of the current file, which is weather.py. 
#This is useful for constructing paths to other files in the same directory or subdirectories.

#functions

def LoadDataFromFilePath(path):
    data = []

    try:
        with open(path, "r", encoding="utf-8") as file: # "r" means read mode, "utf-8" is the encoding

            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split()

                city = " ".join(parts[:-1])
                value = float(parts[-1])

                data.append([city, value])

        return data

    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")

    except PermissionError:
        print(f"Error: Permission denied for '{path}'.")

    except ValueError:
        print(f"Error: Invalid numeric value in '{path}'.")

    except IndexError:
        print(f"Error: Invalid data format in '{path}'.")

    except Exception as ex:
        print(f"Unexpected Error: {ex}")

    return []

def ToFah(celsius):
    try:
        return float((celsius * 9 / 5) + 32)
    except Exception:
        return None
    
def ConvertTemperatureToFahrenheit(temp_data):
    result = []

    try:
        for city, temp in temp_data:
            fah = ToFah(temp)
            result.append([city, float(fah)])

        return result

    except Exception as e:
        print("Error converting temperature:", e)
        return []

def getHgt60(Humidity):
    try:
        result = list(
            filter(lambda item: item[1] > 60, Humidity)
        )
        return result

    except Exception as e:
        print("Error filtering humidity:", e)
        return []

def getTlt60(temperature):
    try:
        result = list(
            filter(lambda item: item[1] < 60, temperature)
        )
        return result

    except Exception as e:
        print("Error filtering temperature:", e)
        return []
 
def getRaingt100(AnnualRainfull):
    try:
        result = list(
            filter(lambda item: item[1] > 100, AnnualRainfull)
        )
        return result

    except Exception as e:
        print("Error filtering rainfall:", e)
        return []
    
def getWindSpeedlt12(WindSpeed):
    try:
        result = list(
            filter(lambda item: item[1] < 12, WindSpeed)
        )
        return result

    except Exception as e:
        print("Error filtering wind speed:", e)
        return []
    
def PossibilityOfRain(getTlt60, getHgt60, getRaingt100, getWindSpeedlt12):
    try:
        rainy = {}

        for city_t, temp in getTlt60:
            for city_h, hum in getHgt60:
                for city_r, rain in getRaingt100:
                    for city_w, wind in getWindSpeedlt12:

                        if (city_t == city_h == city_r == city_w):

                            rainy[city_t] = [temp, hum, rain, wind]

        return rainy

    except Exception as e:
        print("Error in prediction:", e)
        return {}

def getRainy(rainy_dict):
    try:
        print("-" * 60)
        print("Cities with a high possibility of rain:")
        print("-" * 60)
        print(" ")
        print(f"{'City':<12}{'Humidity':<12}{'Temperature':<15}{'Rainfall':<10}{'Wind Speed':<10}")
        print("-" * 60)

        for city, values in rainy_dict.items():
            temp, hum, rain, wind = values

            print(f"{city:<12}{hum:<12}{temp:<15}{rain:<10}{wind:<10}")

    except Exception as e:
        print("Error displaying rainy data:", e)

# Load all datasets

TemperatureData = LoadDataFromFilePath(
    os.path.join(BASE_DIR, "Climate", "Temperature.txt")
)
HumidityData = LoadDataFromFilePath(
    os.path.join(BASE_DIR, "Climate", "Humidity.txt")
)
AnnualRainfulData = LoadDataFromFilePath(
    os.path.join(BASE_DIR, "Climate", "AnnualRainful.txt")
)
WindSpeedData = LoadDataFromFilePath(
    os.path.join(BASE_DIR, "Climate", "WindSpeed.txt")
)
TemperatureFahrenheitData = ConvertTemperatureToFahrenheit(TemperatureData)
high_humidity = getHgt60(HumidityData)
cold_cities = getTlt60(TemperatureFahrenheitData)
high_rainfall = getRaingt100(AnnualRainfulData)
lowest_windSpeed = getWindSpeedlt12(WindSpeedData)
rainy_result = PossibilityOfRain(cold_cities, high_humidity, high_rainfall, lowest_windSpeed)


# Save everything into data.py

with open("data.py", "w", encoding="utf-8") as file: # "w" means write mode
    file.write("TemperatureData = ")
    file.write(repr(TemperatureData)) #repsentation of the data, which can be used to recreate the object
    file.write("\n\n")

    file.write("HumidityData = ")
    file.write(repr(HumidityData))
    file.write("\n\n")

    file.write("AnnualRainfulData = ")
    file.write(repr(AnnualRainfulData))
    file.write("\n\n")

    file.write("WindSpeedData = ")
    file.write(repr(WindSpeedData))
    file.write("\n")

    file.write("TemperatureFahrenheitData = " + repr(TemperatureFahrenheitData) + "\n\n")
    
    file.write("high_humidity  = " + repr(high_humidity) + "\n\n")

    file.write("cold_cities  = " + repr(cold_cities) + "\n\n")

    file.write("high_rainfall  = " + repr(high_rainfall) + "\n\n")

    file.write("lowest_windSpeed  = " + repr(lowest_windSpeed) + "\n\n")

    file.write("rainy_result  = " + repr(rainy_result) + "\n\n")

#printing the dict

getRainy(rainy_result)





    

