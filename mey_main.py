import my_game

ucu = my_game.Station("Католицький університет")
ucu.set_description("Місце, де ти починаєш свій шлях")

park = my_game.Station("Стрийський парк")
park.set_description("Місце для чудових прогулянок з друзями.")

rynok = my_game.Station("Стрийський ринок")
rynok.set_description("Найкраще місце для того, щоб купити коханій дівчині квіточки.")

pidvalna = my_game.Station("Підвальна")
pidvalna.set_description("Звідси легко дістатися Площі Ринок")

ucu.link_station(park, "далі")
park.link_station(ucu, "назад")
park.link_station(rynok, "далі")
rynok.link_station(park, "назад")
pidvalna.link_station(rynok, "назад")
rynok.link_station(pidvalna, "далі")

rouge = my_game.Enemy("Грабіжник", "Хоче вкрасти твій гаманець")
rouge.set_conversation("Віддай гроші, або ж заберу силою.")
rouge.set_weakness("газовий балончик")
park.set_character(rouge)

kontroler = my_game.Enemy("Контролер", "Утік з трамваю і не знає, де себе подіти")
kontroler.set_conversation("Білетики є?")
kontroler.set_weakness("проїзний")
rynok.set_character(kontroler)

cygan = my_game.Enemy("Циган", "Проситиме у тебе гроші на проїзд")
cygan.set_conversation("Дай 5 грн")
cygan.set_weakness("банківська карта")
pidvalna.set_character(cygan)

good = my_game.Companion("Львів'янин","Друг, який супроводжуватиме тебе під час подожі")
ucu.set_character(good)

balon = my_game.Item("газовий балончик")
balon.set_description("Невеличкий балончик, який тобі подав тобі сусід по сидінню.")
rynok.set_item(balon)

ticket = my_game.Item("проїзний")
ticket.set_description("Папірчик завалявся у тебе в кишені")
pidvalna.set_item(ticket)

card = my_game.Item("банківська карта")
card.set_description("Ти знайшов у гаманці")
park.set_item(card)

current_Station = ucu
backpack = []

dead = False

while dead == False:

    print("\n")
    current_Station.get_details()

    inhabitant = current_Station.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_Station.get_item()
    if item is not None:
        item.describe()
    print('(напрямок: далі/назад; дія:взяти,битися,поговорити')
    command = input("> ")

    if command in ["далі", "назад"]:
        # Move in the given direction
        current_Station = current_Station.move(command)
    elif command == "поговорити":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "битися":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("Чим битимешся?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:

                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Оооо, ти виграв цю битву!")
                    current_Station.character = None
                    if inhabitant.get_defeated() == 3:
                        print("Вітання, ти переміг усіх ворогів.")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Еххх ти програв цю битву.")
                    print("На жаль, це кінець гри(")
                    dead = True
            else:
                print("У тебе немає " + fight_with)
        else:
            print("Тобі немає з ким битися")
    elif command == "взяти":
        if item is not None:
            print("Ти поклав " + item.get_name() + " до свого наплічника")
            backpack.append(item.get_name())
            current_Station.set_item(None)
        else:
            print("Тобі немає чого брати!")
    else:
        print("Мені невідомо як це " + command)