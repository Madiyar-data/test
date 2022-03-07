import math
import time
import matplotlib.pyplot as plt

def lab_sinus(r):
    if r%2==0:
        r=5
    return (math.sin(r))

def Ploshad_kruga(r):
    if r%2==0:
        r=5
    return (2*(math.pi**2)*r)

def Obyom_cilindra(h):
    if h%2==0:
        h=5
    return Ploshad_kruga(h)*h

def lab_expgens(a):
    if a%2==0:
        a=5
    return math.exp(a)

k=int(input("Range: "));n=1
fact=[]
expec=[]

fact2=[]
expec2=[]

fact3=[]
expec3=[]

fact4=[]
expec4=[]

x1=[];x2=[];x3=[];x4=[]
y1=[];y2=[];y3=[];y4=[]
print("Регрессионное тестирование")
print("\n\nТаблица тестирования функции lab_sinus")
print("\nВходные данные | Фактический результат  | Ожидаемый результат  | Вывод тестирования")
print("-----------------------------------------------------------------------------------")
#def test_answer():
for i in range(n,k):
    print(i,"             | ",lab_sinus(i),"   | ", math.sin(i)," | ",lab_sinus(i) == math.sin(i))
    fact.append(lab_sinus(i))
    expec.append(math.sin(i))
    if (lab_sinus(i) == math.sin(i))==False:
        x1.append(i)
        y1.append(lab_sinus(i))

print("\n\n\n\n\nТаблица тестирования функции Ploshad_kruga")
print("\nВходные данные | Фактический результат  | Ожидаемый результат  | Вывод тестирования")
print("-----------------------------------------------------------------------------------")
for i in range(n,k):
    print(i,"             | ",Ploshad_kruga(i),"   | ", (2*(math.pi**2)*i)," | ",Ploshad_kruga(i) == 2*(math.pi**2)*i)
    fact2.append(Ploshad_kruga(i))
    expec2.append(2*(math.pi**2)*i)
    if (Ploshad_kruga(i) == 2*(math.pi**2)*i)==False:
        x2.append(i)
        y2.append(Ploshad_kruga(i))
    
print("\n\n\n\n\nТаблица тестирования функции Obyom_cilindra")
print("\nВходные данные | Фактический результат  | Ожидаемый результат  | Вывод тестирования")
print("-----------------------------------------------------------------------------------")
for i in range(n,k):
    print(i,"             | ",Obyom_cilindra(i),"   | ", 2*(math.pi**2)*i*i," | ",Obyom_cilindra(i) == 2*(math.pi**2)*i*i)
    fact3.append(Obyom_cilindra(i))
    expec3.append(2*(math.pi**2)*i*i)
    if (Obyom_cilindra(i) == 2*(math.pi**2)*i*i)==False:
        x3.append(i)
        y3.append(Obyom_cilindra(i))

print("\n\n\n\n\nТаблица тестирования функции lab_expgens")
print("\nВходные данные | Фактический результат  | Ожидаемый результат             | Вывод тестирования")
print("-----------------------------------------------------------------------------------")
for i in range(n,k):
    print(i,"             | ",lab_expgens(i),"    | ", math.exp(i),"                 | ",lab_expgens(i) == math.exp(i))
    fact4.append(lab_expgens(i))
    expec4.append(math.exp(i))
    if (lab_expgens(i) == math.exp(i))==False:
        x4.append(i)
        y4.append(lab_expgens(i))
    



data=range(n,k)
plt.style.use('dark_background')

plt.axes([0.05,.055,0.42,0.38])
plt.plot(data,fact,"--", color='blue',label='Фактический результат')
plt.plot(data,expec,'.', color='lime',label='Ожидаемый результат')
if x1!=[]:
    plt.plot(x1,y1,'.',color='r',label='Регрессионная ошибка')
plt.xlabel('Входные данные')
plt.ylabel('Выходные данные')
plt.title('Тестирование функции lab_sinus')
plt.legend(loc='upper left')

plt.axes([0.55,.055,0.42,0.38])
plt.plot(data,fact2,"--",color='blue',label='Фактический результат')
plt.plot(data,expec2,'.',color='lime',label='Ожидаемый результат')
if x2!=[]:
    plt.plot(x2,y2,'.',color='r',label='Регрессионная ошибка')
plt.xlabel('Входные данные')
plt.ylabel('Выходные данные')
plt.title('Тестирование функции Ploshad_kruga')
plt.legend(loc='upper left')


plt.axes([0.05,.57,0.42,0.38])
plt.plot(data,fact3,"--",color='blue',label='Фактический результат')
plt.plot(data,expec3,'.', color='lime',label='Ожидаемый результат')
if x3!=[]:
    plt.plot(x3,y3,'.',color='r',label='Регрессионная ошибка')
plt.xlabel('Входные данные')
plt.ylabel('Выходные данные')
plt.title('Тестирование функции Obyom_cilindra')
plt.legend(loc='upper left')


plt.axes([0.55,.57,0.42,0.38])
plt.plot(data,fact4,"--", color='blue',label='Фактический результат')
plt.plot(data,expec4,'.', color='lime',label='Ожидаемый результат')
if x4!=[]:
    plt.plot(x4,y4,'.',color='r',label='Регрессионная ошибка')
plt.xlabel('Входные данные')
plt.ylabel('Выходные данные')
plt.title('Тестирование функции lab_expgens')
plt.legend(loc='upper left')

plt.show()
time.sleep(222)
