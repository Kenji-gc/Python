barras = int(input("Introduce el número de barras que no son del dia"+"\n"))
sindescuento = barras*3.49
descuento = (sindescuento)*0.6
total = sindescuento-descuento
print("Precio sin descuento:"+str(round(sindescuento, 2))+"€"+"\n"+"Descuento:"+str(round(descuento, 2))+"€"+"\n"+"Precio total:"+str(round(total, 2))+"€")