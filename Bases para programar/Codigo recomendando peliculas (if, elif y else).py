# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 17:34:43 2025

@author: Wilfredo
"""

print( )
print("Bienvenidos aqui puedes optener recomendaciones de peliculas de loa generos: Accion, Comedia, Terror, Drama y Ciencia Ficcion")
print( )
peliculas = {
"acci ́on": ("""Mad Max : Fury Road, John Wick, Gladiador, Machete, El agente invisible, Sin tiempo para morir, Tren bala, Dredd, Hero, Venganza, """),
"comedia": ("""Superbad, La m ́ascara, Dos tontos en fuga, Borat, Tootsie, Proyecto x,"""),
"terror": ("""El conjuro, IT, Halloween, Anabelle, La noche del demonio"""),
"drama": ("""Forrest Gump , En busca de la felicidad, El padrino, Roma, Parásitos"""),
"ciencia ficci ́on": ("""Interestelar, Blade Runner 2049, Matrix, Iron man, Pantera negra""")
}
print( )
a = input("Digite el genero de pelicula : ").lower()
print( )

match a:
    case "accion":
        print( )
        print("Te recomendamos estas pel ́ıculas de acci ́on: ",peliculas["acci ́on"])
        print( )
        s1 = input("ingrese la pelicula de las recomendaciones de la cual desee la sinopsis : ").lower()
        if(s1 == "mad max" or s1 == "mad max : fury road"):
            print( )
            print("""Sinopsis: Tras un holocausto nuclear, el mundo se ha convertido 
en un desierto y la civilización se ha derrumbado. Max Rockatansky 
(Tom Hardy), un superviviente, es capturado por los War Boys, 
el ejército del tiránico Immortan Joe (Hugh Keays-Byrne) y llevado 
a la Ciudadela de Joe.""")
        elif(s1 == "john wick" or s1 == "john" or s1 == "wick"):
            print( )
            print("""Sinopsis: John Wick es un ex sicario que sufre la pérdida de 
su verdadero amor. Cuando asaltan su casa y matan a su perro, se 
ve obligado a volver a la acción para vengarse..""")
        elif(s1 == "gladiador"):
            print( )
            print("""Sinopsis: Al grito de "¡Roma Invicta!" mientras sus fuerzas atacan, 
el general Maximus Decimus Meridius (Russell Crowe) lidera al ejército romano 
hacia la victoria contra los bárbaros germánicos en el año 180 d. C., poniendo 
fin a una prolongada guerra y ganándose la estima del anciano emperador Marco Aurelio.""")
        elif(s1 == "machete"):
            print( )
            print("""Sinopsis: Un ex federal mexicano fugitivo, es contratado para 
asesinar a un senador corrupto (Robert De Niro) que combate la 
inmigración ilegal con argumentos simplistas.""")
        elif(s1 == "el agente invisible"):
            print( )
            print("""Sinopsis: la película adapta la primera novela de Mark Greaney sobre 
agente de la CIA Court Gentry, alias Sierra Seis, que es sacado de una cárcel 
federal y reclutado para perseguir a criminales. Años después, él mismo se 
convertirá en el objetivo de una persecución a contrarreloj cuando llegue a sus 
manos un valioso objeto.""")
        elif(s1 == "tren bala"):
            print( )
            print("""Sinopsis: Ladybug (Brad Pitt) es un asesino con mala suerte decidido
a llevar a cabo sus cometidos de manera pacífica tras demasiados 
“trabajos” que han descarrilado. El destino, en cualquier caso, 
tiene otros planes para él al colocarle en su última misión en 
una vía de colisión con adversarios letales venidos de alrededor
del planeta en el tren más rápido del mundo.""")
        elif(s1 == "sin tiempo para morir"):
            print( )
            print("""Sinopsis: James Bond ha dejado el servicio activo. Su paz dura poco 
cuando Felix Leiter, un viejo amigo de la CIA, aparece pidiendo ayuda, lo que 
lleva a Bond a seguir la pista de un misterioso villano armado con una nueva y 
peligrosa tecnología.""")
        elif(s1 == "dredd"):
            print( )
            print("""Sinopsis: En el futuro, los policías actúan también como jueces; 
Dredd (Karl Urban, el prota de 'The Boys') es uno de ellos, y junto a la novata 
Anderson (Olivia Thirlby) trata de acabar con Ma-Ma (Lena Headey, de 'Juego de Tronos'),
 la violenta líder de una banda de traficantes. A hostias.""")
        elif(s1 == "hero"):
            print( )
            print("""Sinopsis: Un ambicioso líder que desea llegar a ser el 
primer emperador de China, el rey de Qin, después de un devastador atentado, 
siempre lleva puesta su armadura de batalla y se retira a su palacio reforzado, 
que vacates de todos, pero la mayoría de su asesores de confianza.""")
        elif(s1 == "venganza"):
            print( )
            print("""Sinopsis: La vida de un operador de quitanieves da un vuelco 
cuando su hijo muere en circunstancias extrañas y, para vengarse, comienza una 
matanza contra un cártel de drogas local""")
        else:
            print("La pelicula ingresada no esta dentro de las recomendaciones")
    case "comedia":
        print( )
        print("Te recomendamos estas pel ́ıculas de comedia: ",peliculas["comedia"])
        print( )
        s2 = input("ingrese la pelicula de las recomendaciones de la cual desee la sinopsis : ").lower()
        if(s2 == "superbad"):
            print( )
            print("""Sinopsis: Dos semanas antes de su graduación de secundaria, 
Evan (Michael Cera) y Seth (Jonah Hill), mejores amigos desde hace mucho tiempo,
 están a punto de irse a diferentes universidades. Seth y Evan han estado juntos 
 desde que tenían 8 años y toda la escuela creía que permanecerían así para siempre.""")
        elif(s2 == "la m ́ascara"):
            print( )
            print("""Sinopsis: Stanley Ipkiss ( Jim Carrey ), empleado de un 
banco de Edge City, es un romántico tímido y desafortunado que es acosado 
regularmente por casi todos los que lo rodean, incluido su jefe ( Eamonn Roche ), 
su casera, la Sra. Peenman ( Nancy Fish ), y los mecánicos de automóviles.""")
        elif(s2 == "dos tontos en fuga "):
            print( )
            print("""Sinopsis: Después de que los confundan con terroristas y 
los arrojen a la bahía de Guantánamo, los drogadictos Harold y Kumar escapan y 
regresan a Estados Unidos, donde proceden a huir por todo el paí""")
        elif(s2 == "borat"):
            print( )
            print("""Sinopsis: Borat Sagdiyev, un popular personaje de la televisión 
kazaja, abandona su patria, Kazajstán, para trasladarse al "mayor país del mundo", 
los "Estados Unidos y América", con el fin de realizar un documental a instancias del 
ficticio Ministerio de Información kazajo.""")
        elif(s2 == "tootsie"):
            print( )
            print("""Sinopsis: Michael Dorsey (Dustin Hoffman) es un actor que 
vive y trabaja en la ciudad de Nueva York. La mayor parte de su trabajo parece 
ser sobre el escenario; es experto en disfraces y tiene tendencia a adaptar su 
propio look a la audición en función de lo que cree que quiere el director.""")
        elif(s2 == "proyecto x"):
            print( )
            print("""Sinopsis: Proyecto X sigue a tres anónimos estudiantes del 
último curso del instituto que quieren darse a conocer. Su idea es inocente: vamos 
a montar una fiesta que nadie pueda olvidar... pero nada podía prepararlos para 
esta fiesta.
""")
        else:
            print("La pelicula ingresada no esta dentro de las recomendaciones")
    case "terror":
        print( )
        print("Te recomendamos estas pel ́ıculas de terror: ",peliculas["terror"])
        print( )
        s3 = input("ingrese la pelicula de las recomendaciones de la cual desee la sinopsis : ").lower()
        if(s3 == "el conjuro"):
            print( )
            print("""Sinopsis: Basada en hechos reales, El Conjuro, relata la 
terrorífica historia de dos investigadores paranormales reconocidos mundialmente: 
Ed y Lorraine Warren, quienes son convocados para ayudar a una familia aterrorizada 
por una presencia tenebrosa en una apartada granja de Rhode Island.""")
        elif(s3 == "it"):
            print( )
            print("""Sinopsis: Cuenta la historia, en un juego de correspondencias 
con el pasado y el presente, de un grupo de siete amigos que son perseguidos por 
una entidad sobrenatural, al que llaman «Eso», que es capaz de cambiar de forma y 
se alimenta principalmente del terror que produce en sus víctimas.""")
        elif(s3 == "halloween"):
            print( )
            print("""Sinopsis: Halloween es una saga de películas estadounidenses 
del género slasher. Se centra en el asesino psicópata Michael Myers, quien tras 
pasar quince años en un hospital psiquiátrico por haber matado a su hermana mayor, 
escapa y reincide en sus crímenes. Este asesino mata niños a partir de los 11 años.""")
        elif(s3 == "anabelle"):
            print( )
            print("""Sinopsis: La historia de ANNABELLE tiene lugar antes de 
los eventos de El conjuro, siguiendo a la malvada muñeca protagonista. A finales 
de los años 60, la joven pareja formada por Mia (Annabelle Wallis) y John (Ward Horton) 
espera su primer hijo. Como regalo, John regala a Mia una espeluznante muñeca para su 
colección.""")
        elif(s3 == "la noche del demonio"):
            print( )
            print("""Sinopsis: Una familia descubre que espíritus malignos se 
han apoderado de su nuevo hogar y que su hijo ha caído inexplicablemente en coma. 
Pero cuando vuelven a mudarse, entienden que no era solo la casa la que estaba embrujada.""")
        else:
            print("La pelicula ingresada no esta dentro de las recomendaciones")
    case "drama":
        print( )
        print("Te recomendamos estas pel ́ıculas de drama: ",peliculas["drama"])
        print( )
        s4 = input("ingrese la pelicula de las recomendaciones de la cual desee la sinopsis : ").lower()
        if(s4 == "forrest Gump"):
            print( )
            print("""Sinopsis: La historia describe varias décadas de la vida 
de Forrest Gump, un nativo de Alabama que sufre una leve discapacidad intelectual; 
esto no le impide ser testigo privilegiado, y en algunos casos actor decisivo, 
de muchos de los momentos más transcendentales de la historia de los Estados Unidos""")
        elif(s4 == "en busca de la felicidad"):
            print( )
            print("""Sinopsis: En 1981, en San Francisco, el astuto vendedor y 
hombre de familia Chris Gardner ( Will Smith ) invierte los ahorros de la familia 
en un densitometro Osteo National, un aparato dos veces más caro que un aparato de 
rayos X pero con una imagen ligeramente más nítida.""")
        elif(s4 == "el padrino"):
            print( )
            print("""Sinopsis: El anciano patriarca de una dinastía del crimen 
organizado transfiere el control de su imperio clandestino a su renuente hijo. 
Nueva York, 1945. Don Vito Corleone (interpretado por Marlon Brando) es el padrino 
de una familia mafiosa. Tiene tres hijos: Sonny (James Caan), Fredo (John Cazale) 
y Michael (Al Pacino).""")
        elif(s4 == "roma"):
            print( )
            print("""Sinopsis: La película narra la vida de una empleada doméstica, 
Cleo, que trabaja en la casa de una familia acomodada de la colonia Roma, un barrio 
de la Ciudad de México, a principios de la década de los 70.""")
        elif(s4 == "parásitos "):
            print( )
            print("""Sinopsis: Kim Ki-Taek (Song Kang-Ho), un conductor desempleado, 
vive con su esposa Choong-Sook (Jang Hye-Jin), su hijo Ki-Woo (Choi Woo-Shik) y su 
hija Ki-Jeong (Park So-Dam) en un destartalado apartamento en un semisótano. La familia 
lucha por sobrevivir, trabajando en trabajos mal pagados, como doblar cajas de pizza.""")
        else:
            print("La pelicula ingresada no esta dentro de las recomendaciones")
    case "ciencia ficcion":
        print( )
        print("Te recomendamos estas pel ́ıculas de ciencia ficcion: ",peliculas["ciencia ficcion"])
        print( )
        s5 = input("ingrese la pelicula de las recomendaciones de la cual desee la sinopsis : ").lower()
        if(s5 == "Interestelar"):
            print( )
            print("""Sinopsis: Cuando en el futuro la Tierra se vuelve inhabitable, 
un granjero y ex piloto de la NASA, Joseph Cooper, recibe la misión de pilotar 
una nave espacial, junto con un equipo de investigadores, para encontrar un nuevo 
planeta para los humanos.""")
        elif(s5 == "blade runner" or s5 == "blade runner 2049" or s5 == "blade"):
            print( )
            print("""Sinopsis: La unidad Blade Runner se formó para matar a todos 
los Nexus 6 restantes en la Tierra. En Los Ángeles, en noviembre de 2019, el ex 
oficial de policía Rick Deckard (Harrison Ford) es detenido por el oficial Gaff 
(Edward James Olmos) y llevado ante su ex supervisor, Bryant (M. Emmet Walsh).""")
        elif(s5 == "matrix"):
            print( )
            print("""Sinopsis: En 1999, en una ciudad sin nombre, el programador 
informático Thomas Anderson (Keanu Reeves) es en secreto un hacker conocido 
como "Neo". Es inquieto, ansioso y motivado por aprender el significado de las 
referencias crípticas a "Matrix" que aparecen en su computadora.""")
        elif(s5 == "iron man"):
            print( )
            print("""Sinopsis: La película cuenta la historia de Anthony Stark, 
un multimillonario industrial y genio inventor, que es secuestrado y obligado a 
construir un arma devastadora. En su lugar, utilizando su inteligencia e ingenio, 
Anthony construye una armadura de alta tecnología y escapa de su cautiverio.""")
        elif(s5 == "pantera negra"):
            print( )
            print("""Sinopsis: Hace siglos, cinco tribus africanas se enfrentan 
por un meteorito que contiene vibranium. Un guerrero ingiere una "hierba con forma 
de corazón" afectada por el metal y obtiene habilidades sobrehumanas, convirtiéndose 
en el primer "Black Panther". Une a todos excepto a la tribu Jabari para formar 
la nación de Wakanda.""")
        else:
            print("La pelicula ingresada no esta dentro de las recomendaciones")
    case _: print("Lo siento, no tengo recomendaciones para ese g ́enero.")
print( )
print("Gracias por su visita :)")










































































