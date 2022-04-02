import re


correo = input(str('Introduzca su direccion de correo electronico:\n'))
try:
    if(re.search("* @*.*", correo)!=None):
        print('Acceso completado')
    else:
        print(1/0)
except ZeroDivisionError:
    print('**ERROR**\nEso no es una direccion de correo electronico valida')