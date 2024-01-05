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
elif passo1 == "não":
    passo2 = validar_resposta("Que horas você acordou? ", ["6h", "7h", "8h", "outro"])
    if passo2 in ["6h", "7h"]:
        print("Considere treinar em jejum ou tomar café da manhã.")
    elif passo2 == "8h":
        print("Tome café da manhã!")
    else:
        print("Está muito tarde, siga com outros afazeres do dia.")