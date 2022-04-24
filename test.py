# this project translate WestFlemishPython to regular Python code
import re

start = '(?<![A-Za-z])( ?\(? ?)'
end = '( ?[(\[]? ?)(?![A-Za-z])'


def translToRP(prog):
    prog = re.sub(start + r'voe ([A-Za-z]*) i' + end, r'\1for \2 in\3', prog)
    with open("translatore.txt", "r") as translatore:
        lines = translatore.readlines()
        for line in lines:
            line = line.strip().split(",")
            prog = change(line[0], line[1], prog)
    return prog


def translToWFP(prog):
    prog = re.sub(start + r'for ([A-Za-z]*) in' + end, r'\1voe \2 i\3', prog)
    with open("translatore.txt", "r") as translatore:
        lines = translatore.readlines()
        for line in lines:
            line = line.strip().split(",")
            prog = change(line[1], line[0], prog)
    return prog


def change(van, naar, prog):
    return re.sub(start + van + end, r'\1' + naar + r'\2', prog)


# inp = input("want to load the program? y/n\n")
inp = "y"
if inp == "y":
    with open("totrans", "r") as file:
        prog = file.read()
elif inp == "n":
    prog = input("put in your program here\n")

inp = input("to what you want to translate  WFP/RP\n")
if inp == "WFP":
    prog = translToWFP(prog)
    print("WFP prog:\n" + prog)
if inp == "RP":
    print("WFP prog:\n" + prog)
    prog = translToRP(prog)
    print("RP prog:\n" + prog)
    exec(prog)