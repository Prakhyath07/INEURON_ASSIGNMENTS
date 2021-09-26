def divby0():
    try:
        5/0
    except Exception as e:
        return e
    
print(divby0())