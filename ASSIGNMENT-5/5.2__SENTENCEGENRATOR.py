## using function but output is list
def sent():
    subjects=["Americans ","Indians"]
    verbs=["play","watch"]
    objects=["Baseball","Cricket"]

    sentences=[]

    for s in subjects:
        for v in verbs:
            for o in objects:
                 sentences.append(s+" "+ v + " " + o +".")
                 
    return sentences
             
### if defining a function is not required:

subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]

sentences=[]

for s in subjects:
    for v in verbs:
        for o in objects:
                a=s+" "+ v + " " + o +"."
                print(a)
                
