class GrumpyDict(dict):
    def __repr__(self):
        print("NONE OF YOUR BUSINESS")
        return super().__repr__()
    
    def __missing__(self, key):
        print(f"YOU WANT {key}? WELL IT AIN'T HERE!")
        
    def __setitem__(self, key, value):
        print("YOU WANT TO CHANGE THE DICTIONARY?")
        print("OK FINE...")
        super().__setitem__(key, value)
        
    def __contains__(self, item):
        print("NO IT AIN'T IN HERE!")
        return False
    
data = GrumpyDict({"first":"Tom", "animal": "cat"})
print(data);
data['city'] = "Tokyo"
print(data)
'city' in data