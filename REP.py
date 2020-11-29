# Petite enquête/Intro
print("C'est une petite question, nous vous poserons quelques questions, lorsque vous serez prêt à taper le chiffre 12 ?")
reply = input()
print("Ok, commençons ")
#Petit apprentissage de votre question
print("Vous voyagez en avion, en train ou en voiture ?")
opinion = input()
print("Moi aussi j'aime voyager par "+ opinion)
print()
#Petit problème de mathématiques
answer = round(12.2 + 14.6, 1)

Reponse = input("Qu'est-ce que 12.2 + 14.6?")

if float(Reponse) == answer:
	print("Correct !")
else:
	print("La bonne réponse à 12.2 + 14.6 is", answer,)
#Fin