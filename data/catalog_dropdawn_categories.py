from data.electronics_subcategory import Projectors, Tablets, Laptops, Phones


class CatalogDropdownItems:
    def __init__(self):
        self.electronics = Electronics()
        # self.demo_products = DemoProducts()
        # self.clothes = Clothes()
        # self.children_products = ChildrenProducts()
        # self.sport_products = SportProducts()
        # self.gifts = Gifts()

    DEMO = "Демо-продукты"
    ELECTRONICS = "Электроника"
    CLOTHES = "Одежда, обувь"
    CHILDREN_PRODUCTS = "Детские товары"
    SPORT_PRODUCTS = "Спорт товары"
    GIFTS = "Подарки"


class Electronics:
    def __init__(self):
        self.projectors = Projectors()
        self.tablets = Tablets()
        self.laptops = Laptops()
        self.phones = Phones()
        # self.smartphones = Smartphones()

    PROJECTORS = "Проекторы"
    TABLETS = "Планшеты"
    LAPTOPS = "Ноутбуки"
    PHONES = "Телефоны"
    SMARTPHONES = "Смартфоны"
