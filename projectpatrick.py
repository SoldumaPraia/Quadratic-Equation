while True:
    print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
    print("          Quadratic Equation Solver")
    while True:
        print("")
        print("ax²+ bx + c")                                                #informar que estamos referindo a uma equação de 2a grau
        print("")
        print("(To exit enter 0 for a, b, and c.)") 
        try:                                                                #para checkar se usuário entrar um valor inválido
            print("")
            a = float(input("Enter the value of 'a': "))
            b = float(input("Enter the value of 'b': "))
            c = float(input("Enter the value of 'c': "))
            if a==0 and b==0 and c==0:                                      #condição de parada
                raise SystemExit                                            #para parar o programa
            break                                                           #para sair do 'while' se nunhum error acontece
        except ValueError:                                                  #tipos de erros que são capturados
            print("")
            print("")
            print("Invalid entry. Please enter numbers.")
            print("")                           
            x = input("Press <Enter> to try again or 'x' to exit\t")        #para pausar antes de voltar para o segundo 'while' o digitar x para parar
            if x == 'x': raise SystemExit                                   #condição de parada


    delta = (b**2 - 4*a*c)                                                  #declarando o variável 'delta'

    print("")
    print("discriminant (delta) = ",delta)
    print("")


    if delta<0:                                                             #nesse contexto não pode pegar o raiz quadrado de um número negativo    
        print("The square root of a negative number yields no real roots.")
        print("Try other values...")                                        
        print("")                                      
        
    elif delta>0:
        x1 = float((-b + delta**(1/2))/2*a)
        x2 = float((-b - delta**(1/2))/2*a)
        print("x1 = ",x1)
        print("")
        print("x2 = ",x2)
        
    elif delta==0:
        x = float(-b/2*a)
        print("The single root of the equation is ",x)

    print("")                                                               #depois de qualquer resultado vai vir aqui
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("")
    x = input("Press <Enter> to try again or 'x' to exit\t")                #para pausar antes de voltar do começo ou digitar x para parar
    if x == 'x': raise SystemExit                                           #condição de parada
    print("")
    print("")
    
