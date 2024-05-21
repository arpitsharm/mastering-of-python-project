name = input("Enter the name of the metro :- ")
to_go= input("Enter the to go location of the metro :- ")

with open(f"metro/{name}.txt", "w")as f:
    f.write(to_go)