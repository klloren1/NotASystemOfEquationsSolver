from numpy import matrix
from numpy import linalg


def main():
    inputFile = file("equation.txt").read()
    equations = inputFile.split('\n')
    sides = list()
    variables = list()
    for equation in equations:
        print equation
        equation.replace(" ", "")
        sides.append([equation.split('='), dict()])

    temp = ""
    for equation in sides:
        flag = False
        for s in equation[0][0]:
            if s.isalpha():
                if temp is "":
                    temp = "1"
                if temp is "-":
                    temp = "-1"
                if equation[1].has_key(s):
                    equation[1][s] += " " + temp
                else:
                    equation[1][s] = "" + temp
                temp = ""
                flag = False
                if s not in variables:
                    variables.append(s)
            elif s.isdigit() or s is '/' or s is '*':
                temp += "" + s
                flag = True
            elif s is "-":
                if not flag:
                    temp += "" + s
                    flag = True
                else:
                    if equation[1].has_key("constant"):
                        if temp[0] is not "-":
                            equation[1]["constant"] += " -" + temp
                        else:
                            equation[1]["constant"] += " " + temp[1:]
                    else:
                        if temp[0] is not "-":
                            equation[1]["constant"] = "-" + temp
                        else:
                            equation[1]["constant"] = "" + temp[1:]
                    temp = "-"
                    flag = False
            elif s is "+":
                if flag:
                    if equation[1].has_key("constant"):
                        if temp[0] is not "-":
                            equation[1]["constant"] += " -" + temp
                        else:
                            equation[1]["constant"] += " " + temp[1:]
                    else:
                        if temp[0] is not "-":
                            equation[1]["constant"] = "-" + temp
                        else:
                            equation[1]["constant"] = "" + temp[1:]
                    temp = ""
                    flag = False

        if temp is not "":
            if equation[1].has_key("constant"):
                if temp[0] is not "-":
                    equation[1]["constant"] += " -" + temp
                else:
                    equation[1]["constant"] += " " + temp[1:]
            else:
                if temp[0] is not "-":
                    equation[1]["constant"] = "-" + temp
                else:
                    equation[1]["constant"] = "" + temp[1:]
        temp = ""
        flag = False

        for s in equation[0][1]:
            if s.isalpha():
                if temp is "":
                    temp = "1"
                if temp is "-":
                    temp = "-1"
                if equation[1].has_key(s):
                    if temp[0] is not "-":
                        equation[1][s] += " -" + temp
                    else:
                        equation[1][s] += " " + temp[1:]
                else:
                    if temp[0] is not "-":
                        equation[1][s] = "-" + temp
                    else:
                        equation[1][s] = "" + temp[1:]
                temp = ""
                flag = False
                if s not in variables:
                    variables.append(s)
            elif s.isdigit() or s is '/' or s is '*':
                temp += "" + s
                flag = True
            elif s is "-":
                if not flag:
                    temp += "" + s
                    flag = True
                else:
                    if equation[1].has_key("constant"):
                        equation[1]["constant"] += " " + temp
                    else:
                        equation[1]["constant"] = "" + temp
                    temp = "-"
                    flag = False
            elif s is "+":
                if flag:
                    if equation[1].has_key("constant"):
                        equation[1]["constant"] += " " + temp
                    else:
                        equation[1]["constant"] = "" + temp
                    temp = ""
                    flag = False

        if temp is not "":
            if equation[1].has_key("constant"):
                equation[1]["constant"] += " " + temp
            else:
                equation[1]["constant"] = "" + temp
            temp = ""
            flag = False

        if not equation[1].has_key("constant"):
            equation[1]["constant"] = "0"

    for equation in sides:
        for variable in variables:
            if not equation[1].has_key(variable):
                equation[1][variable] = "0"
    print sides

    mat1 = list()
    mat2 = list()
    for equation in sides:
        temp = list()
        for variable in variables:
            tmp = 0
            for value in equation[1][variable].split():
                tmp += stringToValue(value)
            temp.append(tmp)
        mat1.append(temp)
        tmp = 0
        for value in equation[1]["constant"].split():
            tmp += stringToValue(value)
        mat2.append([tmp])

    A = matrix(mat1)
    x = matrix(mat2)
    solution =  linalg.solve(A, x)

    for index in range(len(variables)):
        print("{} = {}".format(variables[index], solution[index, 0]))


def stringToValue(s):
    try:
        result = int(s)
    except:
        tmp = ""
        result = 0
        for c in s:
            if c.isdigit() or c is "-":
                tmp += c
            if c is "*" or c is "/":
                if tmp[0] is "*":
                    result *= int(tmp[1:])
                elif tmp[0] is "/":
                    result /= int(tmp[1:])
                else:
                    result += int(tmp)
                tmp = "" + c

        if tmp[0] is "*":
            result *= int(tmp[1:])
        elif tmp[0] is "/":
            result /= int(tmp[1:])
        else:
            result += int(tmp)
    return result

main()