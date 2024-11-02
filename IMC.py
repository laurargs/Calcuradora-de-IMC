def Menu():
    print("\n----------------------------------------------------------------------")
    print("                          Calculadora de IMC                            ")
    print("----------------------------------------------------------------------")
    print("1. Calcular IMC")
    print("2. Sair")

def Calculo_IMC(peso, altura):
    print("Calculando IMC...")
    return (peso / (altura*altura))

def Classificar_IMC(imc):
    if imc < 18.5:
        return "Abaixo do peso!", "Aumentar a ingestão de calorias saudáveis e procurar orientação nutricional."
    elif 18.5 <= imc < 24.9:
        return "Peso normal!", "Manter uma alimentação balanceada e praticar atividades físicas regularmente."
    elif 25 <= imc < 29.9:
        return "Sobrepeso!", "Reduzir o consumo de alimentos ricos em açucar e gordura, além de aumentar a prática de exercícios."
    elif 30 <= imc < 34.9:
        return "Obesidade Grau I", "Consultar um médico ou nutricionista para desenvolver um plano alimentar e de atividades físicas."
    elif 35 <= imc < 39.9:
        return "Obesidade Grau II", "É importânte buscar orientação médica e adotar mudanças significativas no estilo de vida."
    else:
        return "Obesidade Grau III", "Acompanhamento médico é essencial para ajudar na perda de peso e previnir complicações."
def main(): 
    while True:
        Menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            peso = float(input(f"Digite o seu peso em kg: "))
            altura = float(input(f"Digite a sua altura em metros (ex: 1.65): "))
            
            imc = Calculo_IMC(peso, altura)
            classificacao_imc = Classificar_IMC(imc)

            print(f"\nO seu IMC é: {imc:.2f}")
            print(f"Classificação: {classificacao_imc[0]}\n")
            print(classificacao_imc[1])
        
        elif opcao == '2':
            print("Obrigada por usar a calculadora de IMC. Até mais!")
            break
       
        else:
            print("Opção inválida! Tente novamente.")

# Verificando se o script está sendo executado diretamente
if __name__ == "__main__":
    main()
    
