import sum
import sub

def calcul(formula):

    a = int(formula[0])
    answer = 0

    for i in range(1, len(formula)):
        n = formula[i]
        if n == "+":
            a = int(formula[i-1])
            b = int(formula[i+1])
            sumab = str(a) + str(b)
            answer += sum.add(sumab)

        elif n == "-":
            a = int(formula[i-1])
            b = int(formula[i+1])
            answer -= sub.sub([a,b])

    return answer