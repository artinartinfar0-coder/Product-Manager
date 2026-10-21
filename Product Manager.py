class Product:
    total_products = 0
    def __init__(self,name,price):
        self.name = name
        self.__price = price
        Product.total_products += 1
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,new_price):
        if new_price >= 0:
            self.__price = new_price
        else:
            print("Error: Price cannot be negative!")
    @staticmethod
    def show_total():
        print(f"All Products:{Product.total_products}")
class DigitalProduct(Product):
    def __init__(self, name, price,download_link):
        super().__init__(name, price)
        self.download_link = download_link
products = []
while True:
    i = input("1.Add Phydical Product\n2.Add Digital Product\n3.Show All & Exit\nchoose one option:")
    if i == "1":
        n = input("name:")
        p = float(input("price:"))
        product = Product(n,p)
        products.append(product)
    if i == "2":
        n = input("name:")
        p = float(input("price:"))
        d = input("download_link:")
        dp = DigitalProduct(n,p,d)
        products.append(dp)
    if i == "3":
        for item in products:
            if isinstance(item,DigitalProduct):
                print(f"Product:{item.name},Price:{item.price}, Link:{item.download_link}")
            else:
                print(f"Product:{item.name},Price:{item.price}")
        Product.show_total()
        break
    print("*" * 20)