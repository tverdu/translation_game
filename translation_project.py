
portuguese_dictionary = {"blue":"azul" , "red":"vermelho" , "yellow":"amarelo" , "green":"verde" , "white":"branco" , "black":"preto" , "brown":"marrom" , "pink":"rosa" , "purple":"roxo" , "hot pink":"rosa choque" , "gray":"cinza", "silver":"prata" , "golden":"dourado" , "beige":"bege" , "navy-blue":"azul marinho" , "orange":"laranja"}
spanish_dictionary = {"blue":"azul" , "red":"rojo" , "yellow":"amarillo" , "green":"verde" , "white":"blanco" , "black":"negro" , "brown":"cafe" , "pink":"rosado" , "purple":"morado" , "hot pink":"rosado fuschia" , "gray":"gris", "silver":"prateado" , "golden":"dorado" , "beige":"beis" , "navy-blue":"azul marino" , "orange":"anaranjado"}
french_dictionary = {"blue":"bleu" , "red":"rouge" , "yellow":"jaune" , "green":"vert" , "white":"blanc" , "black":"noir" , "brown":"brun" , "pink":"rose" , "purple":"pourpre" , "hot pink":"rosa choque" , "gray":"gris", "silver":"prata" , "golden":"dourado" , "beige":"bege" , "navy-blue":"azul marinho" , "orange":"orange"}
italian_dictionary = {"blue":"blu" , "red":"rosso" , "yellow":"giallo" , "green":"verde" , "white":"bianco" , "black":"nero" , "brown":"marrone" , "pink":"rosa" , "purple":"porpora" , "hot pink":"rosa choque" , "gray":"grigio", "silver":"prata" , "golden":"dourado" , "beige":"bege" , "navy-blue":"azul marinho", "orange":"arrancione"}
print "Let's play a translation game!"
# print "Are you ready? Enter YES or NO:" 

user_choice = raw_input("Are you ready? Enter YES or NO:") 
user_choice = user_choice.lower()
if (user_choice == "yes"):

    print "Select the language:"
    print "Enter 1 for Portuguese"
    print "Enter 2 for Spanish"
    print "Enter 3 for French"
    print "Enter 4 for Italian"
    user_language = raw_input("Enter 1, 2, 3 or 4.")

    if user_language == "1":
        #do stuff
        print "OK, I'll teach you Portuguese!"

        name = raw_input("What is your name?")
        print "Meu nome e {}.".format(name)
        
        live = raw_input("Where do you live?")
        print "Eu moro em {}".format(live)
        
        work = raw_input("Where do you work?")
        print "Eu trabalho em {}.".format(work)

        age = raw_input("How old are you?")
        print "Eu tenho {} anos.".format(age)

        color = raw_input("What is your favorite color?")
        if color in portuguese_dictionary:
            color = portuguese_dictionary[color]
        print "Minha cor favorita e {} .".format(color)


    if user_language == "2":
       #do stuff
       print "Ok, Now I'll teach you Spanish!"

       name = raw_input("What is your name?")
       print "Hola, Me llamo {}.".format(color)

       live = raw_input("Where do you live?")
       print "Yo vivo en {}.".format(live)

       work = raw_input("Where do you work?")
       print "Trabajo en {}.".format(work)

       age = raw_input("How old are you?")
       print "Tengo {} anos.".format(age)

       color = raw_input("What is your favorite color?")
       if color in spanish_dictionary:
            color = spanish_dictionary[color]
       print "Mi color favorito es {}.".format(color)


    if user_language == "3":
       #do stuff
       print "Ok, Now I'll teach you French."

       name = raw_input("What is your name?")
       print "Ca va, Je m'apelle {}.".format(name)

       live = raw_input("Where do you live?")
       print "J'habite a {}.".format(live)

       work = raw_input("Where do you work?")
       print "Je travaille a {}.".format(work)
       
       age = raw_input("How old are you?")
       print "J'ai {} ans.".format(age)

       color = raw_input("What is your favorite color?")
       if color in french_dictionary:
            color = french_dictionary[ color]
       print "Ma coleur favorite est le {}.".format(color)


    if user_language == "4":
       #do stuff
       print "Ok, Now I'll teach you Italian."

       name = raw_input("What is your name?")
       print "Ciao, Me chiamo {}.".format(name)

       live = raw_input("Where do you live?")
       print "Habito a {}.".format(live)

       work = raw_input("Where do you work?")
       print "Lavoro a {}.".format(work)

       age = raw_input("How old are you?")
       print "Ho {} anni.".format(age)

       color = raw_input("What is your favorite color?")
       if color in italian_dictionary:
            color = italian_dictionary[color]
       print "Il mio colore favorite e {}.".format(color)

















    # if user_language == "3":
    #     #do stuff

    # if user_language == "4":
    #     #do stuff



    # #Portuguese = ["Ola! Meu nome e ." , "Eu moro em ." , "Eu trabalho em ." , "Minha cor favorita e ."]
    





    # if (int (language) == 1) :
    #     for index in range (4):
    #         print portuguese [index] , my_info [index]


        
        


else: 
    print  "Good-bye!" 
    print  "Tchau!"
    print  "Adios!"
    print  "Au Revoir!"
    print  "Arrivederci!"
               
