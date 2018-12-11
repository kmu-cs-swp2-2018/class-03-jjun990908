from keypad import functionList
import calcFunctions

def function(key, txt):
    try:
        if key == functionList[0]:
            val = calcFunctions.factorial(txt)
        elif key == functionList[1]:
            val = calcFunctions.decToBin(txt)
        elif key == functionList[2]:
            val = calcFunctions.binToDec(txt)
        elif key == functionList[3]:
            val = calcFunctions.decToRoman(txt)
        elif key == functionList[4]:
            val = calcFunctions.romanToDec(txt)
    except:
        val = 'E'
    return val
