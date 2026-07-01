import random

def create_player():
    """
    Задача 1.1: Инициализация игрока
    
    Возвращает словарь с начальными характеристиками игрока
    """
    return {
        'hp': 100,
        'max_hp': 100,
        'attack': 15,
        'gold': 50
    }

def make_monster(player_level):
    """
    ""1.2""
    
    Аргументы:
        player_level: int - текущий уровень игрока
    
    Возвращает словарь с характеристиками монстра
    """
    monster_names = ["Гоблин", "Скелет", "Орк"]
    name = random.choice(monster_names)
    

    base_hp = random.randint(10, 20)
    base_attack = random.randint(3, 8)
    base_gold = random.randint(5, 15)
    

    return {
        'name': name,
        'hp': base_hp * player_level,
        'attack': base_attack * player_level,
        'gold': base_gold * player_level
    }

def get_damage(base_attack):
    """
    ""1.3""
    
    Аргументы:
        base_attack: int - базовый показатель атаки
    
    Возвращает int - финальный урон (не меньше 1)
    """
    damage = base_attack + random.randint(-3, 3)
    return max(1, damage)

def check_crit():
    """
    ""1.4""
    
    Возвращает bool - True если критический удар (15% вероятность)
    При критическом ударе выводит сообщение в консоль
    """
    is_crit = random.random() < 0.15
    if is_crit:
        print("[КРИТ!] Нанесен двойной урон!")
    return is_crit

def get_combat_choice():
    """
    ""1.5""
    
    Выводит меню и запрашивает ввод пользователя
    Возвращает int или str с выбором пользователя
    """
    print("\n=== ВАШ ХОД ===")
    print("1 - Атаковать")
    print("2 - Выпить зелье")
    
    while True:
        choice = input("Ваш выбор: ").strip()
        if choice in ['1', '2']:
            return int(choice)
        print("Некорректный ввод. Пожалуйста, выберите 1 или 2.")

def heal_player(player):
    """
    ""1.6""
    
    Аргументы:
        player: dict - словарь игрока
    
    Возвращает dict - измененный словарь игрока
    """
    heal_amount = 30
    old_hp = player['hp']
    player['hp'] = min(player['hp'] + heal_amount, player['max_hp'])
    actual_heal = player['hp'] - old_hp
    
    print(f"💚 Вы использовали зелье лечения! Восстановлено {actual_heal} HP.")
    print(f"Текущее здоровье: {player['hp']}/{player['max_hp']}")
    
    return player

def start_battle(player, monster):
    """
    ""1.7""
    
    Аргументы:
        player: dict - словарь игрока
        monster: dict - словарь монстра
    
    Запускает пошаговый бой между игроком и монстром
    Функция изменяет словари по ссылке, ничего не возвращает
    """
    print(f"\n⚔️ БОЙ НАЧИНАЕТСЯ! ⚔️")
    print(f"Противник: {monster['name']} (HP: {monster['hp']}, ATK: {monster['attack']})")
    

    if monster['hp'] <= 0:
        monster['hp'] = 1
    
    while player['hp'] > 0 and monster['hp'] > 0:

        print(f"\n📊 Ваше здоровье: {player['hp']}/{player['max_hp']}")
        print(f"📊 Здоровье {monster['name']}: {monster['hp']}")
        
        choice = get_combat_choice()
        
        if choice == 1:

            damage = get_damage(player['attack'])
            
            if check_crit():
                damage *= 2
            
            monster['hp'] -= damage
            print(f"🗡️ Вы нанесли {damage} урона {monster['name']}!")
            

            if monster['hp'] <= 0:
                monster['hp'] = 0
                print(f"💀 {monster['name']} повержен!")
                break
                
        elif choice == 2:

            player = heal_player(player)
        

        if monster['hp'] > 0:
            monster_damage = get_damage(monster['attack'])
            player['hp'] -= monster_damage
            

            if player['hp'] < 0:
                player['hp'] = 0
                
            print(f"👊 {monster['name']} нанес вам {monster_damage} урона!")
            
            if player['hp'] <= 0:
                print("💀 Вы пали в бою...")
                break

def check_battle_result(player, monster):
    """
    ""1.8""
    
    Аргументы:
        player: dict - словарь игрока
        monster: dict - словарь монстра
    
    Проверяет исход боя
    Возвращает bool - True если победил игрок, False если проиграл
    """
    if monster['hp'] <= 0:

        reward = monster['gold']
        player['gold'] += reward
        print(f"\n🏆 ПОБЕДА! Вы получили {reward} золота!")
        print(f"💰 Всего золота: {player['gold']}")
        return True
    else:

        print("\n💀 ВЫ ПАЛИ В БОЮ...")
        return False
