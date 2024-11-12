from random import randint
from time import sleep
import threading

def input_with_timeout(prompt, timeout):
    answer = [None]
    
    def get_input():
        answer[0] = input(prompt)
    
    thread = threading.Thread(target=get_input)
    thread.start()
    
    thread.join(timeout)
    
    return answer[0]


t1_done = False
while not t1_done:
    print("\n")
    print("Артур входить до загадкового лісу, де древні дерева шепочуть та можуть навести на правильний шлях,")
    print("але лише якщо він розгадає їхню загадку.")
    
    print("\nЗагадка: 'Я маю коріння, але не можу рости, я маю гілки, але не можу летіти. Що я?'")
    
    answer = input("Ваша відповідь: ")
    
    if answer == "дерево":
        print("\nПравильно! Древні дерева розступаються, вказуючи Артуру шлях далі.")
        print("Артур продовжує свою подорож глибше в ліс...")
        t1_done = True
    else:
        print("\nНеправильно. Древні дерева мовчать, не розкриваючи шляху.")
        print("Спробуйте ще раз!")

# 2

print("На околиці лісу Артур стикається з бандою грабіжників. Лицар повинен перемогти їх, щоб продовжити свій шлях.")
        
bandits = 3
while bandits > 0:
    action = input("\nВаш вибір: 'атакувати' або 'уникнути': ")
    if action == "атакувати":
        bandits -= 1
        print("Ви перемогли одного з бандитів! Залишилося: " + str(bandits))
    elif action == "уникнути":
        print("Ви ухилилися від атаки, але бій триває.")
    else:
        print("Невірна команда. Спробуйте ще раз.")
    
print("Ви перемогли всіх бандитів і знайшли карту, що вказує шлях до печери дракона.")


# 3

hints = [ "Там, де розцвітає чотирилистий клевер.", "Під першою сосною, що зростає на південь.", "Там, де співають солов'ї."]
for hint in hints:
    input("\nПідказка: " + hint + " Натисніть Enter, щоб продовжити пошук.")
print("Артур знаходить магічний камінь, який збільшує його захист.")

# 4

materials = ["деревину", "мотузки", "камені"]
for material in materials:
    input("\nАртур шукає " + material + " Натисніть Enter, щоб продовжити пошуки.")
    
print("Артур знайшов усі матеріали та відновив міст. Він переходить через річку.")

# 5
arthur_health = 3
dragon_health = 3
delay_time = 3
magical = False

choice = input("Сяйво магічного каміння привертає увагу Артура... Використати? ")
if choice == "так":
    print("Магічне світло проникає у тіло Артура, надаючи йому величезну силу...")
    magical = True
else:
    print("'Краще на аукціоні продам...' - подумав Артур..")

print("\nНастав час останньої битви! Здолайте дракона!!!111")
print("\n")
while dragon_health > 0 and arthur_health > 0:
    action = input("Ваша дія: 'атакувати' або 'уникнути': ")
    
    if action == "атакувати":
        luck = randint(0, 10)
        if luck < 4:
            dragon_health -= 1
            print("Артур завдав потужний удар драконові! Його здоров'я: " + str(dragon_health))
        else:
            print("Дракон був насторожений і захищений. Атака не завдала йому великої шкоди.")
            print("О ні! Дракон підготував вогняний шар й намагається атакувати Артура! Артур, уникни удару!")
            print("\nУ вас є " + str(delay_time) + " секунд, щоб надрукувати слово 'ухилянт'!")
            
            yhilant = input_with_timeout("Хутчіше, пропиши слово 'ухилянт': ", delay_time)
            
            if yhilant == "ухилянт":
                print("Артуру вдалося ухилитися від атаки!")
                delay_time -= 0.5
                
            else:
                if magical:
                    print("\nАртур прийняв на себе смертельний удар, але замість смерті він почув сміх...")
                    sleep(3)
                    print("'А ти ще хотів мене на аукціоні продати' - сказала невідома фігура")
                    sleep(5)
                    print("'Це був не простий камінь, я - дух, якого закрили у камінні декілька днів тому...' - продовжила фігура")
                    sleep(6)
                    print("'Коротше кажучи, я зголоднів. Зараз я допоможу тобі з драконом, а ти мене нагодуєш.' - з усмішкою додав дух")
                    sleep(10)
                    print("'А як ти їсти будеш, якщо ти дух..' - прокрихтів Артур")
                    sleep(2)
                    print("Циц!")
                    sleep(7)

                    print("Дух завдає смертельний удар дракону! Артур вийграв!")
                    print("\nЗаключення")
                    print("Артур звільняє принцесу Катрін, і вони разом повертаються до царства.")
                    print("Король оголошує святкування на честь їхнього повернення. Вітаємо з перемогою!")
                    print("P.S. А дух з'їдає половину їжі на банкеті")
                    break
                else:
                    arthur_health = 0
                    print("О ні! Дракон завдав фатальний удар Артуру! Його здоров'я: " + str(arthur_health))
                    print("А краще б на аукціон не лишав...")

    elif action == "уникнути":
        print("Ви ухилилися від вогняної атаки.")
        delay_time += 0.5 
    else:
        print("Невірна команда. Спробуйте ще раз.")

if arthur_health <= 0:
    print("Ви програли! Артур не зміг пережити битву з драконом.")
else:
    print("Артур завдає вирішальний удар і перемагає дракона!")

    print("\nЗаключення")
    print("Артур звільняє принцесу Катрін, і вони разом повертаються до царства.")
    print("Король оголошує святкування на честь їхнього повернення. Вітаємо з перемогою!")
    