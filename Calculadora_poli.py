
def limpvetor(num):
    cont  = 0
    for i in range(len(num)):
        if num[i] != 0:
            cont += 1

    vetnovo = [0]*cont
    for i in range(cont):
        vetnovo[i] = num[i]

    return vetnovo


def imppoli(num):


    
    j = 0
    exp = 'P(x) = '
    sinal = 0
    for i in range(len(num)-1,0,-1):
        if num[j] == 0:
            j+= 1
        else:
            if num[j] < 0: 
                exp += "- (" +str(num[j]*-1)+"x^"+str(i) + ") "
                sinal = 2
            else:
                exp += "+ (" + str(num[j])+"x^"+str(i)+ ") "
                sinal = 1
            j += 1
    if sinal == 1:
        exp +="+ (" + str(num[j]) + ")"
    else:
         exp +="- (" + str(num[j]*-1) + ")"
        
        
    return exp
    
def resolver(num,x):
    j = 0
    soma = 0
    
    exp = "P("+str(x)+") = "
    
    for i in range(len(num)-1,0,-1):

     
 
        soma += x**i * num[j]
        exp +="("+ str(x**i * num[j]) +") + "
        
        j += 1
        
    exp += "("+str(num[j])+")"
    soma +=  num[j]
        
    exp += " ="
        
    print(exp,soma)


def somapoli(num1,num2):
    maior = num1
    menor = num2
    if len(num2) > len(num1):
        maior = num2
        menor = num1

    soma = [0]*len(maior)
    

    for i in range(len(menor)):
        soma[i] = maior[i] + menor[i]
        
    for i in range(len(menor),len(maior),1):
        soma[i] = maior[i]
        
        

    return soma


def multpoli(num1,num2):


    soma = 0
    maior = num1
    menor = num2
    if len(num2) > len(num1):
        maior = num2
        menor = num1


    numr = [0]*(len(maior) * len(menor))
   
    
    if menor != maior:
        for i in range(len(maior)):
            for j in range(len(menor)):
                numr[i+j] += maior[i] * menor[j]
    else:
        x = 0
        for i in range(len(maior)):
            for j in range(len(menor)):
                numr[x] = maior[i] * menor[j]
                x += 1
            

  
    return  numr

    


'''        
vetor1 = [5,2]
vetor2 = [3,-1]
vetorm = multpoli(vetor1,vetor2)
print(resolver(vetorm,20))
print(imppoli(vetorm))
'''




    


def menu():
    
    #Vetores testes
    num1 = [2,1,1]
    num2 = [5,-2]
    num3 = [2,-4]
    num4 = [-2,2]
    num5 = [-3]

    
    while True:
        #Menu
        print("""
╔═╗──────────────╔╗────────╔╗──╔═╗───╔╗───────╔╗─╔═╗
║╔╬═╗╔╗╔═╦╦╦╗╔═╗╔╝╠═╦╦╦═╗─╔╝╠═╗║╬╠═╦╗╠╬═╦╦═╦══╬╬═╣═╣
║╚╣╬╚╣╚╣═╣║║╚╣╬╚╣╬║╬║╔╣╬╚╗║╬║╩╣║╔╣╬║╚╣║║║║╬║║║║║╬╠═║
╚═╩══╩═╩═╩═╩═╩══╩═╩═╩╝╚══╝╚═╩═╝╚╝╚═╩═╩╩╩═╩═╩╩╩╩╩═╩═╝""")
        print()
 
        
        print("➊ Imprimir polinômio")
        print("➋ Resolver polinômio")
        print("➌ Somar polinômios")
        print("➍ Mutiplicar polinômios")
        print("⓿ Sair")
        
        #Escolha de função do programa 
        opc = int(input("Escolha uma opção: "))

        #Teste de erro 
        while opc > 4 or opc < 0:
            opc = int(input("ESCOLHA uma opção valida!: "))
            
        #Exibir poli
        if opc == 1:
            
            print("\n"+" "*28+"Imprimir Polinômios"+" "*29+"\n")

            print("*Tabela de Polinômios")
            print("\n1){}\n2){}\n3){}\n4){}\n5){}".format(num1,num2,num3,num4,num5))

            
            x = int(input("ESCOLHA uma opção: "))
            while x > 5 or x < 1:
                    print("1){}\n2){}\n3){}\n4){}\n5){}".format(num1,num2,num3,num4,num5))
                    x = int(input("ESCOLHA uma opção valida!: "))


            print("\npolinômio\n")
                    
            if x == 1:
                            print(imppoli(num1))
            elif x == 2:
                            print(imppoli(num2))
            elif x == 3:
                            print(imppoli(num3))
            elif x == 4:
                            print(imppoli(num4))
            else:
                            print(imppoli(num5))
            
                            
                  
            input("\nAperte ENTER para voltar para o MENU\n")


        #Resolver poli        
        elif opc == 2:

            print("\n"+" "*30+"Resolver Polinômios"+" "*30+"\n")
            
            print("*Tabela de Polinômios")
            print("\n1){}\n2){}\n3){}\n4){}\n5){}".format(imppoli(num1),imppoli(num2),imppoli(num3),imppoli(num4),imppoli(num5)))

            
            x = int(input("ESCOLHA uma opção: "))
            while x > 5 or x < 1:
                    print("1){}\n2){}\n3){}\n4){}\n5){}".format(imppoli(num1),imppoli(num2),imppoli(num3),imppoli(num4),imppoli(num5)))
                    x = int(input("ESCOLHA uma opção valida!: "))


            print("\npolinômio\n")
                    
            if x == 1:
                            esc = num1
            elif x == 2:
                            esc = num2
            elif x == 3:
                            esc = num3
            elif x == 4:
                            esc = num4
            else:
                            esc = num5
            
            print("Escolhido {}".format(imppoli(esc)))

            x = int(input("\nDefina o valor de X que desejá: "))

            print("\n*Resultado\n")

            resolver(esc,x)
                  
            input("\nAperte ENTER para voltar para o MENU\n")
            

        #Somar dois polis
        elif opc == 3:
            print("\n"+" "*32+"Somar Polinômios"+" "*32+"\n")
           
            print("*Tabela de Polinômios")
            print("\n1){}\n2){}\n3){}\n4){}\n5){}".format(imppoli(num1),imppoli(num2),imppoli(num3),imppoli(num4),imppoli(num5)))

            
            x = int(input("ESCOLHA uma opção: "))
            while x > 5 or x < 1:
                    print("1){}\n2){}\n3){}\n4){}\n5){}".format(imppoli(num1),imppoli(num2),imppoli(num3),imppoli(num4),imppoli(num5)))
                    x = int(input("ESCOLHA uma opção valida!: "))


                    
            if x == 1:
                            esc1 = num1
            elif x == 2:
                            esc1 = num2
            elif x == 3:
                            esc1 = num3
            elif x == 4:
                            esc1 = num4
            else:
                            esc1 = num5
            
            print("\nPrimeiro polinômio escolhido {}\n".format(imppoli(esc1)))

            print("*Tabela de Polinômios")
            print("\n1){}\n2){}\n3){}\n4){}\n5){}".format(imppoli(num1),imppoli(num2),imppoli(num3),imppoli(num4),imppoli(num5)))

            
            x = int(input("ESCOLHA uma opção: "))
            while x > 5 or x < 1:
                    print("1){}\n2){}\n3){}\n4){}\n5){}".format(imppoli(num1),imppoli(num2),imppoli(num3),imppoli(num4),imppoli(num5)))
                    x = int(input("ESCOLHA uma opção valida!: "))


                    
            if x == 1:
                            esc2 = num1
            elif x == 2:
                            esc2 = num2
            elif x == 3:
                            esc2 = num3
            elif x == 4:
                            esc2 = num4
            else:
                            esc2 = num5
            
            print("\nSegundo polinômio escolhido {}\n".format(imppoli(esc2)))

            print("\n*Resultado\n")

            vets = somapoli(esc1,esc2)
            
          
            

            print(" {}\n {}\n----------".format(imppoli(esc1),imppoli(esc2))+"----"*len(vets)+" +")
           
            print(" {}".format(imppoli(vets)))

            input("\nAperte ENTER para voltar para o MENU\n")
            
           



        #multiplicar poli     
        elif opc == 4:
            print("\n"+" "*29+"Multiplicar Polinômios"+" "*29+"\n")

            
            print("*Tabela de Polinômios")
            print("\n1){}\n2){}\n3){}\n4){}\n5){}".format(imppoli(num1),imppoli(num2),imppoli(num3),imppoli(num4),imppoli(num5)))

            
            x = int(input("ESCOLHA uma opção: "))
            while x > 5 or x < 1:
                    print("1){}\n2){}\n3){}\n4){}\n5){}".format(imppoli(num1),imppoli(num2),imppoli(num3),imppoli(num4),imppoli(num5)))
                    x = int(input("ESCOLHA uma opção valida!: "))

                    
            if x == 1:
                            esc1 = num1
            elif x == 2:
                            esc1 = num2
            elif x == 3:
                            esc1 = num3
            elif x == 4:
                            esc1 = num4
            else:
                            esc1 = num5
            
            print("\n\nPrimeiro polinômio escolhido {}\n\n".format(imppoli(esc1)))
            
            print("*Tabela de Polinômios")

            print("\n1){}\n2){}\n3){}\n4){}\n5){}".format(imppoli(num1),imppoli(num2),imppoli(num3),imppoli(num4),imppoli(num5)))

            
            x = int(input("ESCOLHA uma opção: "))
            while x > 5 or x < 1:
                    print("1){}\n2){}\n3){}\n4){}\n5){}".format(imppoli(num1),imppoli(num2),imppoli(num3),imppoli(num4),imppoli(num5)))
                    x = int(input("ESCOLHA uma opção valida!: "))


            
                    
            if x == 1:
                            esc2 = num1
            elif x == 2:
                            esc2 = num2
            elif x == 3:
                            esc2 = num3
            elif x == 4:
                            esc2 = num4
            else:
                            esc2 = num5
                            
            print("\n\nSegundo polinômio escolhido {}\n".format(imppoli(esc2)))
            
            polir = multpoli(esc1,esc2)
            polir = limpvetor(polir)

            print("\n*Resultado\n")
            
            

            print(" {}\n {}\n----------".format(imppoli(esc1),imppoli(esc2))+"----"*len(polir)*2+" X")
            print(" {}".format(imppoli(polir)))
        
            input("\nAperte ENTER para voltar para o MENU\n")

           


menu()


    
