import openai
         
# Transform
def gerar_mensagem(lista_mensagens):

    openai.api_key = "************************"
    # Requisição para a API do chatgpt
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = lista_mensagens 
    )
    respostaChatgpt = completion.choices[0].message.content.strip('\"')
    return respostaChatgpt  # Retornar a mensagem gerada em formato de string remove as aspas duplas


if __name__ == "__main__":
    lista_mensagens = []
    while True:
                
        conteudo = input("Pergunte: ")
        mensagem = {
            "role": "system",
            "content": conteudo
        }
        lista_mensagens.append(mensagem)

        respostaDoChat = gerar_mensagem(lista_mensagens)

        print(respostaDoChat)
       # time.sleep(21) # ("Esperando 21 segundos para não exceder o limite de requisições da API -> 3 / min")




