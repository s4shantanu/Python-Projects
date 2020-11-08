# Create a dictionary and take input from the user and return the meaning of the
# word from the dictionary

Dict = {"ignore":"refuse to take notice of or acknowledge",
        "abandon":"cease to support or look after",
        "exaggerate":"enlarged or altered beyond normal proportions",
        "prejudice":"preconceived opinion that is not based on reason or actual experience",
        "Shantanu":"In past century he is a king of Hastinapur"}
print("Enter the Word")
Data = input()
print(Data +"means" + Dict[Data])
