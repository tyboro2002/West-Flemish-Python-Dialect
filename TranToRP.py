#this project translate WestFlemishPython to regular Python code
import re
start = '(?<![A-Za-z])( ?\(? ?)'
end = '( ?[(\[]? ?)(?![A-Za-z])'

def translToRP(prog):
    with open("translatore.txt","r") as translatore:
        lines = translatore.readlines()
        for line in lines:
            line = line.strip().split(",")
            prog = change(line[0],line[1],prog)
    return prog

def change(van,naar,prog):
    return re.sub(start + van + end, r'\1'+naar+r'\2', prog)
