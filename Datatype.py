def datatype():
    various_data_types = [511,112.49,True,"meow",("Security","Blue","Team"),{"apple":1,"pear":5}]
    #determining the datatypes of the values in the array
    detdata=int(input('Enter the index of the what you want to know the datatype: '))
    results=type(various_data_types[detdata])
    print(f"Element {detdata}: {results}")

datatype()