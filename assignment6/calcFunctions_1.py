from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    try:
        n = int(numStr)
    except:
        return 'Error!'
    
    if n>= 4000:
        return 'Error!'

    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
         (100, 'C'),  (90, 'XC'),  (50, 'L'),  (40, 'XL'),
          (10, 'X'),   (9, 'IX'),   (5, 'V'),   (4, 'IV'),
           (1, 'I')
    ]

    result = ''
    for value, letters in romans:
        while n >= value:
            result += letters
            n -= value
    
    return result

def romanToDec(numStr):
    try:
        n = str(numStr)
    except:
        return "Error"

    romans = [
        ('M', 1000), ('D', 500,),
        ('C', 100),  ('L', 50),
        ('X', 10),   ('V', 5),
        ('I', 1)
    ]
    romansDic = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    result = 0
    for i in range(len(n)):
        if len(n) > i + 3:
            if n[i] == n[i+1] == n[i+2] == n[i+3]:
                result = 'Error!'
                break
        if len(n) > i + 1:
            if romansDic[n[i]] == 500 or 50 or 5:
                if romansDic[n[i]] == romansDic[n[i+1]]:
                    result = 'Error!'
                    break

        for letters, value in romans:
            if n[i] == letters:
                if i == len(n)-1:
                    result += value
                    break
                else:
                    if romansDic[n[i]] < romansDic[n[i+1]]:
                        result -= value
                        break
                    else:
                        result += value
                        break
    return result





def funcpi(numStr):
    try:
        n = float(numStr)
    except:
        return str(3.141592)
    return n*3.14

def funcls(numStr):
    try:
        n = float(numStr)
    except:
        return 'Error!'
    return n * 3E+8

def funcss(numStr):
    try:
        n = float(numStr)
    except:
        return 'Error!'
    return n*340

def funcau(numStr):
    try:
        n = float(numStr)
    except:
        return 'Error!'
    return n * 1.5E+8
