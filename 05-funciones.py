def funcion1():
    print("hola mundo")
    
def funcion2(a,b):
    suma=a+b
    print("La suma de {} + {} = {}".format(a,b,suma))
    
def funcion3(a,b):
    return a+b

def main():
    funcion1()
    funcion2(5,3)
    resultado=funcion3(2,4)
    print("el resultado de la funcion es: {}".format(resultado))
    print(funcion3(5,3))
    
if __name__=="__main__":
    main()