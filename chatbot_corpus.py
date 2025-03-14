from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot2 = ChatBot('Export Example Bot')

conversa = ListTrainer(chatbot2)
conversa.export_for_training('./expec_la.json')
#trainer = ChatterBotCorpusTrainer(chatbot2)
#trainer.train('chatterbot.corpus.portuguese')
#trainer.export_for_training('./expec_la.json')

print("Seja bem vindo!")
while True:
    try:
        resposta = chatbot2.get_response(input("Usuário: "))
        if float(resposta.confidence) > 0.5:
            print("Irineu: ", resposta)
        else:
            print("Eu não entendi :(")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break