def validityCheck(a,b):
    while True:
        try:
            inputA = float(a)
            inputB = float(b)
            return True
        except:
            return ('Invalid Input. Please only enter numeric values.')
    
def performSub(a,b):
    return a - b 

def performAdd(a,b):
    return a + b

def performMult(a,b):
    return a * b

def performDiv(a,b):
    if b == 0:
        return ('ILLEGAL OPERATION. Cannot divide by 0.')
    else:
        return a / b

    