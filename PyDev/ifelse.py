a=2
b=1
if a>b:
    print(True)
else:
    print(False)

prototype="A"
subtype="CX"
cost=400

if prototype == "A" and subtype == "CX" and not (cost < 500 or cost > 1000):
    print ("Excellent")
    
else:
    print (False)