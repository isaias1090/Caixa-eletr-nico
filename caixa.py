print ("Phytonlink\n")

total=0
print ("____Caixa Eletronico____ \n")
while True:
  valor= float (input ("Digite o valor da compra (ou 0 para encerrar):"))
  
  if valor ==0:
    break
  else:
    total+=valor

print (" Sua compra foi finalizada! \n")
print (f"O valor da sua compra foi {total: .2f}")
divi= input ("Quer dividir? (s/n):")
if divi== 's':
    parcelas= int(input("Digite o numero de parcelas:\n"))
    totalp= total/parcelas
print (f"Suas compras parceladas derão:{totalp: .2f}")
