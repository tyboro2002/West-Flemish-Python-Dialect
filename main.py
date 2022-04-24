#this project translate WestFlemishPython to regular Python code
from TranToRP import translToRP
from TranToWFP import translToWFP

#inp = input("want to load the program? y/n\n")
inp = "y"
if inp == "y":
    with open("totrans","r") as file:
        prog = file.read()
elif inp == "n":
    prog = input("put your program here\n")

inp = input("to what you want to translate  WFP/RP\n")
if inp == "WFP":
    prog = translToWFP(prog)
    print("WFP prog:\n" + prog)
if inp == "RP":
    print("WFP prog:\n" + prog)
    prog = translToRP(prog)
    print("RP prog:\n" + prog)
    exec(prog)