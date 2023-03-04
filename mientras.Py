controladora=100

print('***Empanadas el machetico***')
print('***************')
print('1.Agregar sabor de empanada')
print('2.Mostrar sabor de empanada')
print('3.cambiar sabor de empanada')
print('0.SALIR')

while(controladora!=0):
    empanada=none
    controladora=int (input('Digita una opcion: '))
    if controladora==1:
        empanada=input('Cual es el sabor: ')    #pass salto de linea
    elif controladora==2:
        print('El sabor de la empanada ',empanada)
    elif controladora==3:
        empanada=input('Cual es el sabor: ')   
    elif controladora==0:
        print(' vuelve pronto')
    else:
        print('Opcion invalida')