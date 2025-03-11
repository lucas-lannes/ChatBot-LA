from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot2 = ChatBot('Export Example Bot')
trainer = ChatterBotCorpusTrainer(chatbot2)
trainer.train('chatterbot.corpus.portuguese')
trainer.export_for_training('./my_export.json')

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
