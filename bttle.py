'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''

#bottle of beer

for quant in range (99, 0, -1):
    if quant > 1:
        print (quant, "bottles, ", quant, "bottles f beer")
        if quant > 2:
            suffix = str (quant - 1 ) + " bottles f beer" #suffix is variable, declaring suffix.
        else:
            suffix = ("1 bottle")
    elif quant == 1:
        print("1 bottle of beer, 1 bottle")
        suffix = "no more beer n the wall!"
    print ("take one down, pass", suffix)
    print ("--")
    
