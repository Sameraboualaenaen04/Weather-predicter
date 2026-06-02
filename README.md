# نريد بناء تطبيق يتنبأ بامكانية هطول الأمطار في مدينة ما اعتمادا على

درجة الحرارة
الرطوبة
سرعة الرياح
معدل الأمطار السنوي السابق
لمحة تاريخية عن هطول الأمطار في المدينة


# We have a files contains the data we need to read it and extract it to use it in our application

# Climate folder, contains:
 Humidity data
 Temperature data
 Wind speed data 
 Rainfall data

# 1. function LoadDataFromFilePath(path) to read the data and return it as a Two dimensional list, the numbers must be float not integers, use Exeptions, stored in data.py: 
 first list for Temperature 
 second list for Humidity
 third list for annualrainful
 fourth list for windspeed


 # 2. function convert the temperature to Fahrenheit, ToFah()

 # 3. function to get the convert it temprature from ToFah() and return it as a Two dimensional list the numbers must be float not integers, use Exeptions, stored in data.py


 # 4.function getHgt60(Humidity) return a list called getHgt60 that include the heighest Humidity values (more than 60), using filter on HumidityData inside data.py.

 # 5.function getTlt60(temperature) return a list called getTlt60 that include the lowest temperature values (less than 60), using filter on TemperatureFahrenheitData inside data.py.

 # 6.function getRaingt100(AnnualRainfull) return a list called getRaingt100 that include the heighest Annual Rainfull values (more than 100), using filter on AnnualRainfulData inside data.py.

  # 7.function getWindSpeedlt12(WindSpeed) return a list called getWindSpeedlt12 that include the lowest wind speed values (less than 12), using filter on WindSpeedData inside data.py.


  #Now we will create a role that predicet if the rain will fall or not, 

  the role is: the rain will fall if (temp < 60 , Humidity < 60, annual rainfall > 100 and windspeed < 12>)


  # the function that will prediect the weather called PossibilityOfRain(getTlt60, getHgt60, getRaingt100, getWindSpeedlt12), the function will return a dictinory called rainy includes just the values that rainfall conditions were met, (keys: city name, values:(list includes the values ) )
 

 # 8.function called getRainy get the dict and show it in cmd like this way:

 City  Humidity Temperature Rainfall

 ----  -------  ----------- ---------


 