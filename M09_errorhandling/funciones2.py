class Funciones2:
    def __init__(self,lista_num):
        if (type(lista_num) != list):
            self.lista = []
            raise ValueError('Se ha creado una lista vacía. Se esperaba una lista de núemeros enteros')  
        else:
            self.lista = lista_num

    def primo(self):
        lista2=[]
        for i in self.lista:
            cont=0
            for j in range(1,i+1):
                if i%j == 0:
                    cont+=1
            if cont <= 2:
                lista2.append(True)
            else:
                lista2.append(False)
          
        return lista2
    
    def modal2(self):
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
        return valor,max
    
    def conversor_grados(self,escala1,escala2):
        lista2=[]
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
            lista2.append(valor)
        return lista2
    
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
        lista2=[]
        for i in self.lista:
            lista2.append(self.factorial(i))
        return lista2