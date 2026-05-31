def register_client(name, phone):
    """Регистрирует нового клиента"""
    return {
        "имя": name,
        "телефон": phone,
        "статус": "активен"
}

def create_order(item, price, loyalty_card=False):
    """Создаёт заказ с возможной скидкой по карте лояльности"""
    if loyalty_card:
        final_price = price * 0.9
        print(f"Заказ {item} оформлен со скидкой. К оплате: {final_price}")
    else:
        print(f"Заказ {item} оформлен. К оплате: {price}")
        
TAX_RATE = 0.20

def calculate_tax(price):
    """Рассчитывает сумму налога"""
    print(f"До изменения: глобальная TAX_RATE = {TAX_RATE}")
    
    TAX_RATE = 0.15
    
    print(f"Внутри функции локальная TAX_RATE = {TAX_RATE}")
    return price * TAX_RATE

print(f"Снаружи до вызова: TAX_RATE = {TAX_RATE}")
tax = calculate_tax(1000)
print(f"Сумма налога (по локальной 15%): {tax}")
print(f"Снаружи после вызова: TAX_RATE = {TAX_RATE}")