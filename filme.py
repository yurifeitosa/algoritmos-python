filmes = {
    "Drama": ["Titanic", "O Poderoso Chefão", "Como eu era antes de você"],
    "Comédia": ["Deadpool", "American Pie", "Todo Mundo em Panico"],
    "Policial": ["Tropa de Elite", "Desejo de Matar", "Bads Boys"],
    "Guerra": ["Rambo", "O Resgate do Soldado Ryan", "Pearl Harbor"],
    "Lançamentos": ["Coringa", "Projeto Gemini", "Velozes e Furiosos: Hobbs & Shaw"],
    "Terror": ["Invocação do Mal", "O Exorcista", "IT: A Coisa", "Jogos Mortais"]
}
with open("filmes.html", "w", encoding="utf-8") as página:
    página.write("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Filmes</title>
</head>
<body>
""")
    for c, v in filmes.items():
        página.write(f"<h1>{c}</h1>\n")
        for e in v:
            página.write(f"<h2>{e}</h2>\n")
    página.write("</body></html>")
print ("Funcionou!!!")
print ("Procure o arquivo 'filmes.html' na pasta que você salvou esse código fonte!")
