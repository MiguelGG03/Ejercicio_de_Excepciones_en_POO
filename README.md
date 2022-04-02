# Ejercicio_de_Excepciones_en_POO

El enlace al repositorio de GitHub de este proyecto es el siguiente: [GitHub](https://github.com/migueliiin/Ejercicio_de_Excepciones_en_POO.git)

En el enunciado que se proporcionaba en la tarea de Ejercicio de Excepciones en POO, era necesario corregir 
el partonón |re.search(". * @. * \ .. *", s)| por uno como por ejemplo |re.search(".*@.*.. *", s)| siendo s 
la cadena de caracteres que recoge el correo electronico.

El primer patrón no es correcto ya que para que nos devuelva un None por respuesta necesitaríamos introducir
una dirección de correo como la siguiente (xx @\xx.x), y esto no sería una dirección correcta.

En cambio el patrón corregido de este patrón, |re.search(".*@.*.. *", s)|,permite que la dirección si que sea 
una correcta. Aunque sigue habiendo un problema con este patrón y es que este patrón nos permite introducir blancos
en vez de caracteres, con esto quiero decir que no hay un mínimo de caracteres a introducir y el patrón te
podría detectar como válido lo siguiente: ( @ . , @. , @h.com, etc).

Para corregir este fallo es tan simple como cambiar los asteríscos del patrón por signos matemáticos de la suma,
de manera que el patrón cambiaría a ser algo así |re.search(".+@.+..+", correo)|.

Código utilizado para el funcionamiento del programa:

    import re

    acabar=False
    i=0
    while(acabar==False):
        if(i<3):    
            correo = input(str('Introduzca su direccion de correo electronico:\n'))
            try:
                if(re.search(".+@.+..+", correo)!=None):
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