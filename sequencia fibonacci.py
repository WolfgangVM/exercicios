def main():
    for n in range (0 ,11):
        result = fib_it(n)
    
    
    valor_digitado = int(input("Digite o valor entre 0 e 40: "))
    if valor_digitado in result:
        print("O valor pertence a sequencia de Fibonacci")
    else:
        print("O valor não pertence a sequencia de FIbonacci")
    
def fib_it(n):
    if n < 0:
        return []
    elif n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    
    lista_fib = [0, 1] 
    for k in range(2, n + 1):
       prox_n = lista_fib[-1] + lista_fib[-2]
       lista_fib.append(prox_n)

    return lista_fib


if __name__=="__main__":
    main()