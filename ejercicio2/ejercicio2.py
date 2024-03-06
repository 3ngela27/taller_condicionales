

# programa para solicitar un prestamo

#input
print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")

sueldo = int(input("Digite la cantida de sueldo que gana: "))
 
deudas = input("diga si tine o no tiene deudas: ")

#proceso
if sueldo >= 945200:

   if deudas == "no":
     rta =   "APROBADO"
   
   else:
      rta = "DENEGADO"
else:
  rta =  "DENEGADO"
#output
print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
print("Su prestamo ha sido" + rta)

