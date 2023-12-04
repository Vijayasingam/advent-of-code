import re

def findCaliberationCode():
  finalCode = 0
  code = 0
  file = open("data.txt", "r")
  for inputEl in file.readlines():
    for char in list(inputEl):
      if (char.isnumeric() == True):
        code = 10 * int(char)
        break
    reversedCharacters = list(inputEl)[::-1]
    for char in reversedCharacters:
      if (char.isnumeric() == True):
        code = int(char) + code
        break
    finalCode = finalCode + code

  return finalCode

def convertStringNumberToValue(numberToConvert):
    if numberToConvert == 'one':
      return '1'
    elif numberToConvert == 'two':
      return '2'
    elif numberToConvert == 'three':
      return '3'
    elif numberToConvert == 'four':
      return '4'
    elif numberToConvert == 'five':
      return '5'
    elif numberToConvert == 'six':
      return '6'
    elif numberToConvert == 'seven':
      return '7'
    elif numberToConvert == 'eight':
      return '8'
    elif numberToConvert == 'nine':
      return '9'
    else:
      return numberToConvert

def findCaliberationCodeWithRegEx():
  finalCode = 0
  code = 0
  count = 0

  file = open("data.txt", "r")
  for inputEl in file.readlines():
    count += 1
    x = re.findall("\d|one|two|three|four|five|six|seven|eight|nine", inputEl)
    code = int(''.join([convertStringNumberToValue(x[0]), convertStringNumberToValue(x[len(x) - 1])]))

    finalCode += code
  
  return finalCode

def main():
  finalCode = findCaliberationCode()
  print('Caliberation Code', finalCode)

  finalCode = findCaliberationCodeWithRegEx()
  print('Caliberation Code with Regex', finalCode) # Code returns 55427 but correct answer is 55429 :(

if __name__ == "__main__":
  main()