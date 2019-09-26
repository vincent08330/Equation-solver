a = 2                                                                                       # give a b and c
b = 8
c = 8

print ("f(x) =",a,"x²","+",b,"x","+",c)                                                     #print it
print ()

alpha = -1*(b/2*a)                                                                          #calcul de alpha et beta
beta = a*(alpha*alpha) + b*alpha + c

print ("Forme canonique =",a,"( x -",alpha,")²","+",beta)                                   #forme canonique
print()


delta = b*b-4*a*c                                                                           #calcul de delta


print ("Delta =",delta)                                                                     #il donne delta
print ()


if (delta>0):                                                                               #posibilité  1

    print ("Il y a 2 racines à cette équation :")

    x1 = (-1*b - delta**0.5)/(2*a)                                                          #calcul x1 et x2

    x2 = (-1*b + delta**0.5)/(2*a)

    print ("x1 =",x1)                                                                       #print x1 et x2
    print ("x2 =",x2)
    print ("x1(non simplifié) =",-1*b,"- racine de",delta,"/",2*a)                          #sil tombe pas juste se fier à la valeur non simplifiée
    print ("x2(non simplifié) =",-1*b,"+ racine de",delta,"/",2*a)
    print ("Forme factorisée =",a,"( x -",x1,") ( x -",x2,")")                              # forme factorisée de l'équation

    if (a<0):
        print ("équation toujours négative")                                                # check du signe de a

    else:
        print ("équation toujours positive")

    print ("à l'extérieur de",x1,"et",x2)                                                   #signe àa l'exterieur des racines

elif (delta==0):                                                                            # cas 2

    print ("Il y a une double racine :")
    x1et2 = (-1*b)/(2*a)                                                                    #calcul double racine
    print ("x1et2 =",x1et2)
    print ("x1et2(non simplifié) =",(-1*b),"/",2*a)                                         # non simplifié si pas juste
    print ("Forme fectorisée =",a,"( x -",x1et2,")²")

    if (a<0):
        print ("équation toujours négative")

    else:
        print ("équation toujours positive")

    print ("S'annule en x =",(-1*b)/(2*a),"soit",-1*b,"/",2*a)                              # etude du signe

else :

    print ("Il n'y a aucune solution")                                                      #aucun calculs juste citation des propriétés
    print ("Pas de forme factorisée")

    if (a<0):
        print ("équation toujours négative")

    else:
        print ("équation toujours positive")




