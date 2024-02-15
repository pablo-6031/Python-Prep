class Funciones:
    def __init__(self,lista_num):
        self.lista=lista_num

    def primo(self):
        cont=0
        for i in self.lista:
            for j in range(0,i):
                if j%i == 0:
                    cont+=1
            if cont <2:
                print(j,"es un numero primo")
            else:
                print(j,"no es un numero primo")
    
    def modal(self):
        cont=0
        valor=0
        max=0
        for i in self.lista:
            for j in self.lista:
                if i == j:
                    cont+=1
            if cont>max:
                valor=i
                max=cont
            cont=0
        print("El numero",valor,"de la lista es el mas repetido y se repite",max,"veces")
    
    def conversor_grados(self,escala1,escala2):
        for i in self.lista:
            if escala1 == "C"  and escala2 == "C":
                valor = i 
            if escala1 == "C"  and escala2 == "F":
                valor = i * 9/5 + 32
            elif escala1 == "C"  and escala2 == "K":
                valor = i + 273.15
            elif escala1 == "F"  and escala2 == "F":
                valor = i
            elif escala1 == "F"  and escala2 == "C":
                valor = (i + 32)*5/9
            elif escala1 == "F"  and escala2 == "K":
                valor = (i + 32)*5/9 +273.15
            elif escala1 == "K"  and escala2 == "K":
                valor = i
            elif escala1 == "K"  and escala2 == "C":
                valor = i - 273.15
            elif escala1 == "K"  and escala2 == "F":
                valor = (i - 273.15) * 9/5 + 32
            print(i,escala1,"equivale a",valor,escala2)
    
    def factorial(self,num):
        if num >=0:
            if type(num)== int:
                if(num>1):
                    num=num*self.factorial(num-1)
                return num
            else:
                return "Solo se permite numeros enteros"
        else:
            return "No se permite numeros negativos"
    def fact(self):
        for i in self.lista:
            print("El factorial de",i,"es:",self.factorial(i))