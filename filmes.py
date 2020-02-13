filmes = {
     "Drama": ["Titanic","O Poderoso Chefão","Como eu era antes de você"],
     "Comédia": ["Deadpool","American Pie","Todo Mundo em Panico"],
     "Policial": ["Tropa de Elite","Desejo de Matar","Bads Boy"],
     "Guerra": ["Rambo","O Resgate do Solgado Ryan","Pearl Harbor"],
     "Lançamentos": ["Coringa", "Projeto Gemini", "Velozes e Furiosos: Hobbs & Shaw"],
     "Terror": ["Inovacação do Mal", "O Exorcista", "IT: A Coisa", "Jogos Mortais"]
     }
pagina = open("filmes.html","w", encoding = "utf-8")
pagina.write("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Filmes</title>
</head>
<body>
""")
for c, v in filmes.items():
     pagina.write("<h1>%s</h1>" % c)
     for e in v:
         pagina.write("<h2>%s</h2>" % e)
pagina.write("""
</body>
</html>
""")
pagina.close()
print ("Arquivo filmes.html criado com sucesso!")
