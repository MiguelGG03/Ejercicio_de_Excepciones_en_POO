import re

acabar=False
i=0
while(acabar==False):
    if(i<3):    
        correo = input(str('Introduzca su direccion de correo electronico:\n'))
        try:
            if(re.search(".*@.*..*", correo)!=None):
                lista=re.split("@",correo)
                print('Acceso completado\n¡Bienvenido '+str(lista[0])+'!')
                acabar=True
            else:
                print(1/0)
        except ZeroDivisionError:
            print('**ERROR**\n'+str(correo)+'no es una direccion de correo electronico valida.')
    else:
        print('**ERROR**\nCuenta bloqueada a causa de un ataque.')
        acabar=True
    i=i+1
