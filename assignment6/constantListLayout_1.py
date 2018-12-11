from keypad import constantDic

def constant(k):
    try:
        keys = list(constantDic.keys())
        values = []
        
        for i in range(4):
            value = str(constantDic.get(keys[i]))
            values.append(value)
        for j in range(4):
            if k == keys[j]:
                text = values[j]
    except:
        text = 'Error!'
    return text
