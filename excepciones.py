import re


correo = input(str('Introduzca su direccion de correo electronico:\n'))
try:
    if(re.search("* @*.*", correo)!=None):
        print('Acceso completado')
    else:
        print(1/0)
