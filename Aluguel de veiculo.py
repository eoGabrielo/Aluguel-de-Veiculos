
print(" ") # STYLE
print("ALUGUEL DE VEICULOS")
print(" ") # STYLE

tipoDoVeiculo= str(input("O veiculo é carro ou moto? ")) # Dependendo da escolha o valor por KM é alterado.

tipoDoVeiculoConta= 0 #Para fazer o calculo P/Km, começa valendo 0.

if tipoDoVeiculo == "moto": #Se for moto tipoDoVeiculoConta recebe 0.15 P/KM;
    tipoDoVeiculoConta= 0.15
elif tipoDoVeiculo == "carro":
    tipoDoVeiculoConta= 2.15 #Se for carro tipoDoVeiculoConta recebe 2.15 P/KM;
else: #Se for escrito algo sem ser carro ou moto, informa esse erro.
    print(" ")
    print(f"ERRO:.!!! {tipoDoVeiculo} !!! Não é uma opção, escolha somente carro ou moto!")
    print("REINICIE O PROGRAMA...")
    print(" ")


diasAlugado= int(input("Quantos dias foi alugado o veiculo? ")) 
kmRodados= int(input("Quantos km o veículo rodou? "))
diariaDoVeiculo= int(input("Quanto é a diaria do veiculo? "))


diasAlugadoConta= diasAlugado * diariaDoVeiculo #Calcula os dias alugados pelo o valor escolhido;
kmRodadosConta= kmRodados * tipoDoVeiculoConta#Calcula Km rodados por quanto vale o Km (Moto 0.15 P/Km, Carro 2.15 P/Km);
total= diasAlugadoConta + kmRodadosConta #Soma o valores de Km e diaria.

print(" ")
print(f"Você rodou {kmRodados}Km e ficou {diasAlugado} dias com o veiculo;")
print(f"Tipo do veiculo: {tipoDoVeiculo}")
print(f"P/Dia: R${diariaDoVeiculo}")
print(f"P/Km: R${tipoDoVeiculoConta}")
print(f"Total a pagar: R${total:.2f}")
print(" ")
