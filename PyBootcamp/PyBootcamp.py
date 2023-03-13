import csv
import datetime

# menu.txt dosyasını oluşturup menü seçeneklerini yazdırma işlemi
with open("menu.txt", "w", encoding="utf-8") as file:
    file.write("* Lütfen Bir Pizza Tabanı Seçiniz:\n")
    file.write("1: Klasik\n")
    file.write("2: Margarita\n")
    file.write("3: TürkPizza\n")
    file.write("4: Sade Pizza\n\n")
    
    file.write("* Ve seçeceğiniz sos:\n")
    file.write("11: Zeytin\n")
    file.write("12: Mantarlar\n")
    file.write("13: Keçi Peyniri\n")
    file.write("14: Et\n")
    file.write("15: Soğan\n")
    file.write("16: Mısır\n\n")
    
    file.write("* Teşekkür ederiz!")
    
# Pizza sınıfı ve alt sınıflarının tanımlanması
class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost
    
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost

class ClassicPizza(Pizza):
    def __init__(self):
        super().__init__("Klasik Pizza", 20.0)
        
class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__("Margarita Pizza", 25.0)
        
class TurkishPizza(Pizza):
    def __init__(self):
        super().__init__("Türk Pizza", 30.0)
        
class DominosPizza(Pizza):
    def __init__(self):
        super().__init__("Dominos Pizza", 35.0)
        
class Decorator(Pizza):
    def __init__(self, pizza):
        super().__init__(pizza.get_description(), pizza.get_cost())
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description() + ", " + super().get_description()

    def get_cost(self):
        return self.pizza.get_cost() + super().get_cost()
    
class Zeytin(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Zeytin"
        self.cost = 2.0
        
class Mantarlar(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mantarlar"
        self.cost = 3.0
        
class KeciPeyniri(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Keçi Peyniri"
        self.cost = 5.0
        
class Et(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Et"
        self.cost = 6.0
        
class Sogan(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Soğan"
        self.cost = 1.5
        
class Misir(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mısır"
        self.cost = 2.5

# kullanıcıdan pizza siparişi alma işlemi
while True:
    print("Lütfen yapmak istediğiniz işlemi seçiniz:")
    print("1: Pizza Siparişi Ver")
    print("2: Siparişleri Görüntüle")
    print("3: Çıkış")
    
    choice = input()

    if choice == "1":
        print("Lütfen pizza seçiminizi yapınız (1-4): ")
        print("1: Klasik Pizza ")
        print("2: Margarita Pizza ")
        print("3: Türk Pizza ")
        print("4: Dominos Pizza ")
        pizza_choice = input()

        if pizza_choice == "1":
            pizza = ClassicPizza()
        elif pizza_choice == "2":
            pizza = MargheritaPizza()
        elif pizza_choice == "3":
            pizza = TurkishPizza()
        elif pizza_choice == "4":
            pizza = DominosPizza()
        else:
            print("Hatalı seçim yaptınız!")
            continue

        while True:
            print("Lütfen sos seçiminizi yapınız (11-16) veya çıkmak için 'q' tuşuna basınız: ")
            print("11: Zeytin ")
            print("12: Mantarlar ")
            print("13: Keçi Peyniri ")
            print("14: Et ")
            print("15: Soğan ")
            print("16: Mısır ")
              
            sos_choice = input()

            if sos_choice == "11":
                pizza = Zeytin(pizza)
            elif sos_choice == "12":
                pizza = Mantarlar(pizza)
            elif sos_choice == "13":
                pizza = KeciPeyniri(pizza)
            elif sos_choice == "14":
                pizza = Et(pizza)
            elif sos_choice == "15":
                pizza = Sogan(pizza)
            elif sos_choice == "16":
                pizza = Misir(pizza)
            elif sos_choice == "q":
                break
            else:
                print("Hatalı seçim yaptınız!")
                continue

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("orders.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([current_time, pizza.get_description(), pizza.get_cost()])

    elif choice == "2":
        with open("orders.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    elif choice == "3":
        break

    else:
        print("Hatalı seçim yaptınız!")
        continue
    
    