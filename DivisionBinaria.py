from bitstring import BitArray

while True:
    n=int(input("Ingrese el tamaño de las cadenas de bits:>>"))
    aux = 2**n
    dividendo = int(input("Ingrese el Dividendo:>>"))
    divisor = int(input("Ingrese el divisor:>>"))
    if dividendo > aux:
        print("El dividendo es muy grande para el tamaño. Ingrese otro.")
    elif divisor > aux:
        print("El divisor es muy grande para el tamaño. Ingrese otro.")
    else:
        break

A = BitArray(uint=0,length=n)
Q = BitArray(uint=dividendo,length=n)
M = BitArray(uint=divisor,length=n)
a = 0
negM = ~M
negM = BitArray(uint=((negM.int &(2**n-1))+1), length=n)                        #Aqui se convierte el divisor en su version negativoa en complemento a 2.

while a<n:
    print("Ciclo=",a+1)
    print("A = ",A.bin," Q = ",Q.bin)
    A <<= 1                                                                     #El simbolo << realiza el desplazamiento a la izquierda
    A[n-1]=Q[0]
    Q <<= 1
    print("Desplazando...")
    print("A = ",A.bin," Q = ",Q.bin)
    resta = BitArray(int=(A.int + negM.int), length=n)                           #Aqui realizamos la resta.
    print("resta = ",resta.bin)

    if resta[0] ==1:
        pass
    elif resta[0] == 0:
        Q[n-1] =1
        A=resta
    a+=1

print("A = ",A.bin," Q = ",Q.bin)
print("Cociente = ",int(Q.bin,2)," Residuo = ",int(A.bin,2))