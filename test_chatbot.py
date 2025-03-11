from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

#chatbot = ChatBot("Johnny Five", read_only=True) se ele já estiver treinado

bot = ChatBot('LA', storage_adapter='chatterbot.storage.SQLStorageAdapter', 
              logic_adapters=[
            'chatterbot.logic.BestMatch'],
            database_uri='sqlite:///database.sqlite3')

conversa = ListTrainer(bot)
conversa.train([
    'Oi?',
    'Eae',
    'Qual o seu nome?',
    'Irineu, você não sabe e nem eu',
    'Prazer em te conhecer',
    'Igualmente meu patrão',
])

print("Seja bem vindo!")
while True:
    try:
        resposta = bot.get_response(input("Usuário: "))
        if float(resposta.confidence) > 0.5:
            print("Irineu: ", resposta)
        else:
            print("Eu não entendi :(")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
