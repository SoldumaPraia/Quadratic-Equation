while True:
    print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
    print("          Quadratic Equation Solver")
    while True:
        print("\nax²+ bx + c\n")                                            #informar que estamos referindo a uma equação de segundo grau
        print("(To exit enter 0 for a, b, and c.)") 
        try:                                                                #checar se usuário entrar um valor inválido
            a = float(input("\nEnter the value of 'a': "))
            b = float(input("Enter the value of 'b': "))
            c = float(input("Enter the value of 'c': "))
            if a==0 and b==0 and c==0:                                      #condição de parada
                raise SystemExit                                            #parar o programa
            break                                                           #sair do 'while' se nunhum erro acontecer
        except ValueError:                                                  #tipos de erros que são capturados
            print("\n\nInvalid entry. Please enter numbers.\n")
            x = input("Press <Enter> to try again or 'x' to exit\t")        #pausar antes de voltar para o segundo 'while' o digitar x para parar
            if x == 'x': raise SystemExit                                   #condição de parada


    delta = (b**2 - 4*a*c)                                                  #declarando o variável 'delta'

    print("\ndiscriminant (delta) = ",delta,"\n")


    if delta<0:                                                             #nesse contexto não pode calcular a raiz quadrada de um número negativo    
        print("The square root of a negative number yields no real roots.")
        print("Try other values...\n")
        
    elif delta>0:
        x1 = float((-b + delta**(1/2))/2*a)
        x2 = float((-b - delta**(1/2))/2*a)
        print("x1 = ",x1,"\n")
        print("x2 = ",x2)
        
    elif delta==0:
        x = float(-b/2*a)
        print("The single root of the equation is ",x)

                                                                            #depois de qualquer resultado vai vir aqui
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
    x = input("Press <Enter> to try again or 'x' to exit\t")                #para pausar antes de voltar do começo ou digitar x para parar
    if x == 'x': raise SystemExit                                           #condição de parada
    print("\n")
