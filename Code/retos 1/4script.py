# Juan tiene N cantidad de pesos, Camila tiene la mitad de lo que posee Juan y Ricardo tiene la mitad de lo que poseen Camila y Juan Juntos. ¿Puede PYTHON ayudarme a calcular la cantidad de dinero de los 3?

pesosJuan = int(input("Digite la cantidad de pesos que tiene Juan para calcular: "))
pesosCamila = pesosJuan * 0.5
pesosRicardo = (pesosCamila * 0.5) +  (pesosJuan * 0.5)

print(f"Juan tiene: {pesosJuan}, por ende Camila tiene {pesosCamila} y Ricardo tiene {pesosRicardo}")
