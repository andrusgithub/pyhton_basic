class Contact:
    #конструктор класса - функция с именем __init__
    def __init__(self, name, phone, birthday):
    #тело метода
        self.name = name
        self.phone = phone
        self.birthday = birthday
    # после создания объекта сообщим об этом    
        print(f"Создан новый контакт {name}")
    
    # создадим метод show для вывода на печать данных любого контакта:
    def show(self):
        print(f"имя: {self.name}, телефон: {self.phone}, день рождения: {self.birthday}")

# теперь можно создать объект класса Contact, передав в конструктор значения
ivan = Contact(name="Иван", phone="+155512345", birthday="2.12.1985")

# а можно использовать сокращённый синтаксис:
maria = Contact("Марья", "+277734567", "4.04.1999")
daria = Contact("Дарья", "+123454415", "1.03.1980")

# вызовем метод show() для объекта ivan:
ivan.show()