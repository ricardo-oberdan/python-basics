# help(str)

message = "Meet me Tonight."

print(message)

message2 = 'The clock strikes at midnight'

message3 = "I'm looking for someone to share python knowledge"
message3 = 'I\'m looking for someone to share python knowledge'

movie_quote = """One of my favorite lines from the Godfather is:
"I'm going to make him an offer he can't refuse."
Do you know who said this?"""

print(movie_quote)

print(message.upper())
print(message.lower())
print(message[3:7]) # posicao 3 até a 6
print(message[1:12:2]) # posicao 1 até 12, pulando 1 caractere
print(message[-1:]) # ultimo caractere
print(message[:-1]) # do inicio ate o penultimo caractere
print(message[-8: -2]) # pegando o segundo caractere até o 8 de trás pra frente
print(message[::-1]) # invertendo string
print(sorted(message)) # transformando em uma lista ordenada alfabeticamente