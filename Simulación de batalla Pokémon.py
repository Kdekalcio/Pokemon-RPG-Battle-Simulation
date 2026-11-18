import time
import random
fuente = input('Para jugar correctamente, se necesita cambiar la fuente de la consola manualmente. Para hacer esto, haz clic derecho en la parte superior de la ventana de la simulación, donde aparece el nombre de esta. Luego, ve a "Propiedades", luego, dentro de la nueva ventana que se ha abierto, a la pestaña "Fuente" y, finalmente, en el apartado "Fuente", elige "MS Gothic" o "MS Mincho" y haz clic en el botón "Aceptar", en la parte inferior de la misma ventana. Si esto no se hace, habrá carácteres que no se mostrarán correctamente, siendo reemplazados por cuadros raros. A continuación, verá un texto que solo se mostrará correctamente si ha hecho lo previamente indicado: 『ポケットモンスター 緑』をすることが好きです。 (No, no tendrás que leer japonés para jugar, esto es solo una prueba). Una vez estés listo/a con la fuente, presiona Enter para continuar.')
print('Este es un proyecto autoeducativo con el propósito de enseñar a su propio desarrollador los más básicos aspectos del sistema de combate de los juegos de Pokémon y su funcionamiento interno, incluyendo fórmulas de daño y captura. Por el bien de la simplicidad, se ha tomado a los juegos de 1996 "Pocket Monsters Aka" y "Pocket Monsters Midori" (lanzados en España como "Pokémon Edición Roja" y "Pokémon Edición Azul" en 1999  —Como curiosidad, 緑 (Midori) significaba "verde", pero este nunca salio en occidente, siendo lanzada una edición azul (青 (Ao) en Japón) en su lugar—).')
print('Además de las mecánicas de combate de Rojo y Azul, se han hecho también algunos mínimos cambios inspirados en los arreglos que los juegos de 1999 "Pocket Monsters Kin & Gin" (Oro y Plata en España, 2001) le hicieron a las mecánicas de Rojo y Azul, con el propósito de balancear las cosas (Vamos, que no es que Rojo y Azul hayan sido una obra maestra en cuanto a balanceo...).')
print('Además, este es un proyecto hecho por el arte que hay detrás de las mecánicas de combate de los juegos de Pokémon. De ninguna manera se pretende usar la marca de Pokémon con el propósito de aprovecharse monetariamente de esta, ni nada que sea malo y/o infrinja alguna ley de derechos de autor o cosas por el estilo.')
explicar = input('¿Quieres leer una explicación de las mecánicas antes de empezar el juego? Escribir "Sí" y presionar Enter para leerla, dejar en blanco y presionar Enter para comenzar sin leerla.')
if explicar == "Sí" or explicar == "sí" or explicar == "SÍ" or explicar == "Si" or explicar == "si" or explicar == "SI":
    print("\n")
    print("Al empezar, se presentará un menú de opciones que el jugador puede hacer durante el turno, las cuales para ser elegidas tendrán que ser escritas por el jugador. Tu Pokémon es un Clefable nivel 50, con características elegidas al azar. Estás luchando contra un Poliwrath salvaje nivel 50, también con características elegidas al azar. A continuación, se explicaran todas las opciones una por una:")
    print('LUCHA: Los Pokémon intercambian ataques entre sí, una vez por turno. Tu Clefable tiene asignado el ataque "Mega Patada", el cual tiene una potencia de 120 y una precisión de 75%, mientras que el Poliwrath salvaje tiene asignado el ataque "Hidrobomba", con una potencia de 120 y una precisión de 80%. Quien tenga mayor velocidad atacará primero. El primero en perder todos sus PS pierde la batalla. La cantidad de PS que quitan los ataques de uno están determinados por la siguiente fórmula: ((((0.2×Nivel de usuario+1)×(ATAQUE de usuario×Potencia))÷(25×DEFENSA enemiga))+2)×(0.01×Bono por ataque de mismo tipo×Efectividad×Variación generada al azar de 85 a 100). Si esta fórmula da un número decimal, será convertido a natural truncado.')
    print('PKMN: Revisa la información de tu Pokémon.')
    print('OBJ: Esta es tu mochila, lo único que tienes son Ultra Balls ilimitadas. En los juegos, una Ultra Ball es un tipo de Poké Ball que es doblemente mejor que la Poké Ball normal. Aquí puedes usarlas para intentar atrapar al Poliwrath salvaje, lo cual resulta difícil, pero no imposible. Al atraparlo, la batalla terminará. El éxito de la captura está determinado por la siguiente fórmula: (((3×PS máx. de enemigo)-(2×PS actuales de enemigo))×(Ratio de captura de enemigo×Ratio de captura de Ball usada))÷(3×PS máx. de enemigo))+Bono por estado. Luego de calcular esta fórmula, se genera un número al azar de 0 a 255. Si este número es menor o igual al resultado de la fórmula, la captura será un éxito. De lo contrario, fallará.')
    print('ESC: Intenta escapar de la batalla. Podrás hacerlo mientras la velocidad de tu Pokémon sea mayor o igual a la del oponente, pero, si no, hay una probabilidad de que no lo logres.')
Enter = input("Preferible jugar con esta banda sonora de fondo (presiona Enter para comenzar la batalla): https://www.youtube.com/watch?v=aQrmCB4ZGGo")
print("\n")
print("¡Un POLIWRATH salvaje apareció!")
time.sleep(1)
print("¡Ve CLEFABLE!")
print("============================")
time.sleep(1)
p1 = {"Nombre": "CLEFABLE", "PS": random.randint(155, 202), "ATAQUE": random.randint(67, 134), "VELOCID.": random.randint(58, 123), "ESPECIAL": random.randint(81, 150)}
PS1Max = p1["PS"]
p2 = {"Nombre": "POLIWRATH", "PS": random.randint(150, 197), "DEFENSA": random.randint(90, 161), "VELOCID.": random.randint(67, 134), "ESPECIAL": random.randint(67, 134)}
PS2Max = p2["PS"]
while True:
    print('「', p1["Nombre"], ': ', p1["PS"], '\n', p2["Nombre"], ': ', p2["PS"], '」')
    turno = input("LUCHA\nPKMN\nOBJ\nESC")
    if turno == "LUCHA" or turno == "lucha" or turno == "Lucha":
        print("============================")
        if p1["VELOCID."] > p2["VELOCID."]:
            print('¡', p1["Nombre"], ' usó MEGA PATADA!')
            preciso = random.randint(1,100)
            if preciso < 75:
                p2["PS"] = p2["PS"] - (int(((((0.2*50+1)*(p1["ATAQUE"]*120))/(25*p2["DEFENSA"]))+2)*(0.01*1.5*1*random.randint(85,100))))
                round(p2["PS"])
                if p2["PS"] <= 0:
                    time.sleep(1)
                    print('¡', p2["Nombre"], ' enemigo se desmayó!')
                    time.sleep(1)
                    end = input('¡', p1["Nombre"], ' ganó 131 Puntos EXP.!')
                    break
                else:
                    time.sleep(1)
                    print('¡', p2["Nombre"], ' usó HIDROBOMBA!')
                    preciso = random.randint(1,100)
                    if preciso < 80:
                        p1["PS"] = p1["PS"] - (int(((((0.2*50+1)*(p2["ESPECIAL"]*120))/(25*p1["ESPECIAL"]))+2)*(0.01*1.5*1*random.randint(85,100))))
                        if p1["PS"] <= 0:
                            time.sleep(1)
                            print('¡', p1["Nombre"], ' debilitado!')
                            time.sleep(1)
                            print("¡ROJO no tiene más POKéMON!")
                            time.sleep(1)
                            end = input("¡ROJO perdió el conocimiento!")
                            break
                    else:
                        time.sleep(1)
                        print("Pero, ¡falló!")
            else:
                time.sleep(1)
                print("Pero, ¡falló!")
                time.sleep(1)
                print('¡', p2["Nombre"], ' usó HIDROBOMBA!')
                preciso = random.randint(1,100)
                if preciso < 80:
                    p1["PS"] = p1["PS"] - (int(((((0.2*50+1)*(p2["ESPECIAL"]*120))/(25*p1["ESPECIAL"]))+2)*(0.01*1.5*1*random.randint(85,100))))
                    if p1["PS"] <= 0:
                        time.sleep(1)
                        print('¡', p1["Nombre"], ' debilitado!')
                        time.sleep(1)
                        print("¡ROJO no tiene más POKéMON!")
                        time.sleep(1)
                        end = input("¡ROJO perdió el conocimiento!")
                        break
                else:
                    time.sleep(1)
                    print("Pero, ¡falló!")
        if p2["VELOCID."] > p1["VELOCID."]:
            print('¡', p2["Nombre"], ' usó HIDROBOMBA!')
            preciso = random.randint(1,100)
            if preciso < 80:
                p1["PS"] = p1["PS"] - (int(((((0.2*50+1)*(p2["ESPECIAL"]*120))/(25*p1["ESPECIAL"]))+2)*(0.01*1.5*1*random.randint(85,100))))
                if p1["PS"] <= 0:
                    time.sleep(1)
                    print('¡', p1["Nombre"], ' debilitado!')
                    time.sleep(1)
                    print("¡ROJO no tiene más POKéMON!")
                    time.sleep(1)
                    end = input("¡ROJO perdió el conocimiento!")
                    break
                else:
                    time.sleep(1)
                    print('¡', p1["Nombre"], ' usó MEGA PATADA!')
                    preciso = random.randint(1,100)
                    if preciso < 75:
                        p2["PS"] = p2["PS"] - (int(((((0.2*50+1)*(p1["ATAQUE"]*120))/(25*p2["DEFENSA"]))+2)*(0.01*1.5*1*random.randint(85,100))))
                        if p2["PS"] <= 0:
                            print('¡', p2["Nombre"], ' enemigo se desmayó!')
                            time.sleep(1)
                            end = input('¡', p1["Nombre"], ' ganó 131 Puntos EXP.!')
                            break
                    else:
                        time.sleep(1)
                        print("Pero, ¡falló!")
            else:
                time.sleep(1)
                print("Pero, ¡falló!")
                time.sleep(1)
                print('¡', p1["Nombre"], ' usó MEGA PATADA!')
                preciso = random.randint(1,100)
                if preciso < 75:
                    p2["PS"] = p2["PS"] - (int(((((0.2*50+1)*(p1["ATAQUE"]*120))/(25*p2["DEFENSA"]))+2)*(0.01*1.5*1*random.randint(85,100))))
                    if p2["PS"] <= 0:
                        time.sleep(1)
                        print('¡', p2["Nombre"], ' enemigo se desmayó!')
                        time.sleep(1)
                        end = input('¡', p1["Nombre"], ' ganó 131 Puntos EXP.!')
                        break
                else:
                    time.sleep(1)
                    print("Pero, ¡falló!")
        if p1["VELOCID."] == p2["VELOCID."]:
            primer = random.randint(1,2)
            if primer == 1:
                print('¡', p1["Nombre"], ' usó MEGA PATADA!')
                preciso = random.randint(1,100)
                if preciso < 75:
                    p2["PS"] = p2["PS"] - (int(((((0.2*50+1)*(p1["ATAQUE"]*120))/(25*p2["DEFENSA"]))+2)*(0.01*1.5*1*random.randint(85,100))))
                    if p2["PS"] <= 0:
                        time.sleep(1)
                        print('¡', p2["Nombre"], ' enemigo se desmayó!')
                        time.sleep(1)
                        end = input('¡', p1["Nombre"], ' ganó 131 Puntos EXP.!')
                        break
                    else:
                        time.sleep(1)
                        print('¡', p2["Nombre"], ' usó HIDROBOMBA!')
                        preciso = random.randint(1,100)
                        if preciso < 80:
                            p1["PS"] = p1["PS"] - (int(((((0.2*50+1)*(p2["ESPECIAL"]*120))/(25*p1["ESPECIAL"]))+2)*(0.01*1.5*1*random.randint(85,100))))
                            if p1["PS"] <= 0:
                                time.sleep(1)
                                print('¡', p1["Nombre"], ' debilitado!')
                                time.sleep(1)
                                print("¡ROJO no tiene más POKéMON!")
                                time.sleep(1)
                                end = input("¡ROJO perdió el conocimiento!")
                                break
                        else:
                            time.sleep(1)
                            print("Pero, ¡falló!")
                else:
                    time.sleep(1)
                    print("Pero, ¡falló!")
                    time.sleep(1)
                    print('¡', p2["Nombre"], ' usó HIDROBOMBA!')
                    preciso = random.randint(1,100)
                    if preciso < 80:
                        p1["PS"] = p1["PS"] - (int(((((0.2*50+1)*(p2["ESPECIAL"]*120))/(25*p1["ESPECIAL"]))+2)*(0.01*1.5*1*random.randint(85,100))))
                        if p1["PS"] <= 0:
                            time.sleep(1)
                            print('¡', p1["Nombre"], ' debilitado!')
                            time.sleep(1)
                            print("¡ROJO no tiene más POKéMON!")
                            time.sleep(1)
                            end = input("¡ROJO perdió el conocimiento!")
                            break
                    else:
                        time.sleep(1)
                        print("Pero, ¡falló!")
            else:
                print('¡', p2["Nombre"], ' usó HIDROBOMBA!')
                preciso = random.randint(1,100)
                if preciso < 80:
                    p1["PS"] = p1["PS"] - (int(((((0.2*50+1)*(p2["ESPECIAL"]*120))/(25*p1["ESPECIAL"]))+2)*(0.01*1.5*1*random.randint(85,100))))
                    if p1["PS"] <= 0:
                        time.sleep(1)
                        print('¡', p1["Nombre"], ' debilitado!')
                        time.sleep(1)
                        print("¡ROJO no tiene más POKéMON!")
                        time.sleep(1)
                        end = input("¡ROJO perdió el conocimiento!")
                        break
                    else:
                        time.sleep(1)
                        print('¡', p1["Nombre"], ' usó MEGA PATADA!')
                        preciso = random.randint(1,100)
                        if preciso < 75:
                            p2["PS"] = p2["PS"] - (int(((((0.2*50+1)*(p1["ATAQUE"]*120))/(25*p2["DEFENSA"]))+2)*(0.01*1.5*1*random.randint(85,100))))
                            if p2["PS"] <= 0:
                                time.sleep(1)
                                print('¡', p2["Nombre"], ' enemigo se desmayó!')
                                time.sleep(1)
                                end = input('¡', p1["Nombre"], ' ganó 131 Puntos EXP.!')
                                break
                        else:
                            time.sleep(1)
                            print("Pero, ¡falló!")
                else:
                    time.sleep(1)
                    print("Pero, ¡falló!")
                    time.sleep(1)
                    print('¡', p1["Nombre"], ' usó MEGA PATADA!')
                    preciso = random.randint(1,100)
                    if preciso < 75:
                        p2["PS"] = p2["PS"] - (int(((((0.2*50+1)*(p1["ATAQUE"]*120))/(25*p2["DEFENSA"]))+2)*(0.01*1.5*1*random.randint(85,100))))
                        if p2["PS"] <= 0:
                            time.sleep(1)
                            print('¡', p2["Nombre"], ' enemigo se desmayó!')
                            time.sleep(1)
                            end = input('¡', p1["Nombre"], ' ganó 131 Puntos EXP.!')
                            break
                    else:
                        time.sleep(1)
                        print("Pero, ¡falló!")
        print("============================")
        time.sleep(1)
    if turno == "PKMN" or turno == "pkmn" or turno == "Pkmn":
        print('\n')
        print('「N°. 036 ', p1["Nombre"], ': N50\nPS: ', p1["PS"], '/', PS1Max)
        print('ESTADO OK」')
        print('============================\nATAQUE ', p1["ATAQUE"], '\nVELOCID. ', p1["VELOCID."], '\nESPECIAL ', p1["ESPECIAL"], '\n============================')
        print('「TIPO1/NORMAL')
        ID = random.randint(10000,99999)
        print('N°ID/', ID)
        print('EO/ROJO」')
        exit = input("                                              [Presiona Enter para regresar a las opciones]")
    if turno == "OBJ" or turno == "obj" or turno == "Obj":
        ball = input("[Escribe POKé BALL para lanzar una ULTRA BALL. Presiona Enter sin haber escrito nada para regresar a las opciones]")
        if ball == "POKé BALL" or ball == "Poké ball" or ball == "poké ball" or ball == "POKÉ BALL" or ball == "POKE BALL" or ball == "Poke ball" or ball == "poke ball" or ball == "pokeball" or ball == "Pokeball" or ball == "POKEBALL" or ball == "Pokéball" or ball == "pokéball" or ball == "POKÉBALL":
            print("¡ROJO utilizó ULTRA BALL!")
            a = ((((3*PS2Max)-(2*p2["PS"]))*(45*2))/(3*PS2Max))+0
            captura = random.randint(0,255)
            if captura <= a:
                time.sleep(1)
                print("                                                                                 [1...]")
                time.sleep(1)
                print("                                                                                 [2...]")
                time.sleep(1)
                print("                                                                                 [3...]")
                time.sleep(1)
                print('¡Muy bien! ¡', p2["Nombre"], ' fue atrapado!')
                time.sleep(1)
                print('¡Serán añadidos nuevos datos POKéDEX sobre ', p2["Nombre"], '!')
                time.sleep(1)
                print('\n')
                print('N°062 ', p2["Nombre"])
                print('RENACUAJO\nAL 1.3m\nPE 54.0kg\n============================')
                end = input('Experto nadador tanto en braza como en crawl. Gana fácilmente a todo nadador humano')
                break
            else:
                d = random.randint(1,120)
                if d < 10:
                    time.sleep(1)
                    print("¡¡No acertaste al POKéMON!!")
                elif d >= 10 and d <= 29:
                    time.sleep(1)
                    print("                                                                                 [1...]")
                    time.sleep(1)
                    print("¡Maldición! ¡El POKéMON se escapó!")
                elif d >= 30 and d <= 69:
                    time.sleep(1)
                    print("                                                                                 [1...]")
                    time.sleep(1)
                    print("                                                                                 [2...]")
                    time.sleep(1)
                    print("¡Auu! ¡Creía haberlo atrapado!")
                elif d >= 70:
                    time.sleep(1)
                    print("                                                                                 [1...]")
                    time.sleep(1)
                    print("                                                                                 [2...]")
                    time.sleep(1)
                    print("                                                                                 [3...]")
                    time.sleep(1)
                    print("¡Auu! ¡Creía haberlo atrapado!")
                time.sleep(1)
                print('¡', p2["Nombre"], ' usó HIDROBOMBA!')
                preciso = random.randint(1,100)
                if preciso < 80:
                    p1["PS"] = p1["PS"] - (int(((((0.2*50+1)*(p2["ESPECIAL"]*120))/(25*p1["ESPECIAL"]))+2)*(0.01*1.5*1*random.randint(85,100))))
                    if p1["PS"] <= 0:
                        time.sleep(1)
                        print('¡', p1["Nombre"], ' debilitado!')
                        time.sleep(1)
                        print("¡ROJO no tiene más POKéMON!")
                        time.sleep(1)
                        end = input("¡ROJO perdió el conocimiento!")
                        break
                    else:
                        print("\n")
                else:
                    time.sleep(1)
                    print("Pero, ¡falló!")
    if turno == "ESC" or turno == "esc" or turno == "Esc":
        if p1["VELOCID."] >= p2["VELOCID."]:
            end = input("¡Escapaste sano y salvo!")
            break
        else:
            huida = random.randint(0,510)
            if huida > 255:
                end = input("¡Escapaste sano y salvo!")
                break
            else:
                print("¡No puede huir!")
                time.sleep(1)
                print('¡', p2["Nombre"], ' usó HIDROBOMBA!')
                preciso = random.randint(1,100)
                if preciso < 80:
                    p1["PS"] = p1["PS"] - (int(((((0.2*50+1)*(p2["ESPECIAL"]*120))/(25*p1["ESPECIAL"]))+2)*(0.01*1.5*1*random.randint(85,100))))
                    if p1["PS"] <= 0:
                        time.sleep(1)
                        print('¡', p1["Nombre"], ' debilitado!')
                        time.sleep(1)
                        print("¡ROJO no tiene más POKéMON!")
                        time.sleep(1)
                        end = input("¡ROJO perdió el conocimiento!")
                        break
                else:
                    time.sleep(1)
                    print("Pero, ¡falló!")
                print("\n")
