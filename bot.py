from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
chatterbot = ChatBot("Ana Clara")
chatterbot.set_trainer(ChatterBotCorpusTrainer)
chatterbot.train("chatterbot.corpus.portuguese")

#conv_inicial = ["Olá","Olá, como vai?!", "Como voce está?", "Eu estou ótimo", "Que bom voce por aqui", "Obrigado", "De nada"]
#conv_dia_dia = ['Qual é o seu nome?','Meu nome é Ana Clara','O que tem feito?','Tenho caminhado as vezes']
#chatbot = ChatBot("Ana Clara")
#chatbot.train(conv_inicial)
#chatbot.train(conv_dia_dia)

while True:
    quest = input('Voce:')
    response = chatterbot.get_response(quest)
    #print('ChatBot:', response)
    if float(response.confidence) > 0.5:
        print('Ana Clara:', response)
    else:
        print('Ana Clara: Não entendi')