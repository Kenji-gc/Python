depositado = float(input("Introduce el dinero depositado en la cuenta de ahorros:"+"\n"))
primero = depositado+(depositado*0.04)
segundo = primero+(primero*0.04)
tercero = segundo+(segundo*0.04)
print("Tus ahorros tras el primer año son "+str(round(primero, 2))+"\n"+"Tus ahorros tras el segundo año son "+str(round(segundo, 2))+"\n"+"Tus ahorros tras el tercer año son "+str(round(tercero, 2))+"\n")