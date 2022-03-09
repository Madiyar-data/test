import math
import time

def lab_sinus(r):
    return (math.sin(r))

def Ploshad_kruga(r):
    return (2*(math.pi)*r**2)

def Obyom_cilindra(h):
    return Ploshad_kruga(h)*h

def lab_expgens(a):
    return math.exp(a)

print("\n    Введите число, чтобы высчитать математические значения")
q=int(input("\n    q ="))
print("\n\n    Ваши полученные математические значения:")
print("\n\n    -------------------------------------------")
print("    |   Формула       |       Вывод ")
print("    -------------------------------------------")
print("    | Sin(",q,") =      |",lab_sinus(q))
print("    -------------------------------------------")
print("    | S = 2*П*",q,"^2 = |", Ploshad_kruga(q))
print("    -------------------------------------------")
print("    | V = S*",q,"=      |",Obyom_cilindra(q))
print("    -------------------------------------------")
print("    | Exp(",q,") =      |",lab_expgens(q))
print("    -------------------------------------------")

time.sleep(222)
