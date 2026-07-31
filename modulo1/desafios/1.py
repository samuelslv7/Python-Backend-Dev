# Recebe a entrada e armazena na variável "entrada"
entrada = input()


# Função reponsável por extrair os domínios dos emails
def extrair_dominios(emails):
    # Separa os emails por ponto e vírgula
    lista_emails = emails.split(";")

    # TODO: Implemente a lógica necessária para extrair os domínios
    dominios = []
    for email in lista_emails:
        posicao = email.find("@")
        final = email[posicao + 1 :]
        dominios.append(final)

    return dominios


# Imprime a lista de strings com os domínios
print(extrair_dominios(entrada))
