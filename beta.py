#definindo função de validar respota
#a função lê o input em minúsculo e se a resposta não estiver dentre as opções redireciona ao algoritmo
def validar_resposta(mensagem,opcoes):
    resposta = input(mensagem).strip().lower()
    while resposta not in opcoes:
        resposta = input("Por favor, responda com {} : " .format(" ou ".join(opcoes))).strip().lower()
    return resposta

passo1 = validar_resposta("Acordou cedo? (Sim/Não) ", ["sim", "não"])

if passo1 == "sim":
    print("Vá treinar em jejum!")
    passo3 = validar_resposta("Qual seu treino de hoje? ", ["a", "b", "c"])
    if passo3 == "a":
        print("Peito, Costas, Ombro")
    elif passo3 == "b":
        print("Biceps, Triceps, Antebraço")
    elif passo3 == "c":
        print("Quadriceps, Femural, Panturrilha, Abdomen")

    print()
    print("Após o treino, tome uma ducha, café da manhã e suplemente.")
    print()
    passo4 = validar_resposta("O que você fará depois do treino? ", ["estudar", "trabalhar", "afazeres domésticos"])
    if passo4 == "estudar":
        print("Estude sem distrações até o almoço!")
    elif passo4 == "trabalhar":
        print("Trabalhe bem até o almoço!")
    elif passo4 == "afazeres domésticos":
        print("Mãos à obra até o almoço!")
    
    print()
    passo5 = validar_resposta("O que fará após o almoço? ", ["descansar", "trabalhar", "estudar", "afazeres domésticos"])
    if passo5 == "descansar":
        print("Descanse por 40min.")
    elif passo5 == "trabalhar":
        print("Continue a labuta!")
    elif passo5 == "estudar":
        print("Estude sem distrações até o lanche.")
    elif passo5 == "afazeres domésticos":
        print("Mãos à obra até o lanche.")

elif passo1 == "não":
    passo2 = validar_resposta("Que horas você acordou? ", ["6h", "7h", "8h", "outro"])
    if passo2 in ["6h", "7h"]:
        print("Considere treinar em jejum ou tomar café da manhã.")
    elif passo2 == "8h":
        print("Tome café da manhã!")
    else:
        print("Está muito tarde, siga com outros afazeres do dia.")

    print()
    passo4 =  validar_resposta("O que você fará agora? ", ["estudar", "trabalhar", "afazeres domésticos"])
    if passo4 == "estudar":
        print("Estude sem distrações até o almoço!")
    elif passo4 == "trabalhar":
        print("Trabalhe bem até o almoço!")
    elif passo4 == "afazeres domésticos":
        print("Mãos à obra até o almoço!")

    print()
    passo5 = validar_resposta("O que fará após o almoço? ", ["descansar", "trabalhar", "estudar", "afazeres domésticos"])
    if passo5 == "descansar":
        print("Descanse por 40min.")
    elif passo5 == "trabalhar":
        print("Continue a labuta!")
    elif passo5 == "estudar":
        print("Estude sem distrações até o lanche.")
    elif passo5 == "afazeres domésticos":
        print("Mãos à obra até o lanche.")