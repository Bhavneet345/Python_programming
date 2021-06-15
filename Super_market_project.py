class Supermarket:
    product_det = []

    def __init__(self, store_name):
        self.store_name = store_name

    @staticmethod
    def listen_audio(products):
        from win32com.client import Dispatch
        speaker = Dispatch("Sapi.SpVoice")
        for items in products:
            speaker.Speak(f"Item number{items}")

    def display_products(self):
        self.product_det = []
        with open("Products_available") as p:
            for product_description in p:
                self.product_det.append(product_description)
        choice = input("Do you want to listen the available products or wanna see??\n")
        if choice == "listen":
            print("Following are the available items!!")
            self.listen_audio(self.product_det)
        elif choice == "see":
            print("Following are the available items!!")
            print("Sno.//Items//Price_amount")
            for items in self.product_det:
                print(items.rstrip())
        else:
            print("Invalid request!!")

    def order_products(self):
        order_det = []
        quantities = []
        product = []
        prices = []
        flag = True
        customer_name = input("What's your name??\n")
        product_det = []
        available = None
        with open("Products_available") as p:
            for product_description in p:
                product_det.append(product_description)
        while flag:
            product_name = input("Enter the product you want to buy\n")
            product.append(product_name)
            for products in product_det:
                if products.split("-")[1].lower() == product_name:
                    available = True
                    quantity = float(input("Enter how much quantity do you want??\n"))
                    quantities.append(quantity)
                    price = int(products.split('-')[2]) * quantity
                    prices.append(price)
                    order_det.append(price)
                    order_det.append(quantity)
                    break
                else:
                    available = False
            if available == False:
                print("Not available!!")
            discount = [self.discount(pri, quan) for pri, quan in zip(prices, quantities)]
            choice = input("Do you want to go for any other product(Yes/No)??\n")
            if choice.lower() == 'yes':
                flag = True
            elif choice.lower() == 'no' and available==True:
                return self.generate_bill(customer_name, product, quantities, prices, discount)
            else:
                print("No bill required!!")
                flag = False

    @staticmethod
    def discount(price, quantity):
        if quantity >= 2 and quantity <= 5:
            discounted_price = price*0.3
        elif quantity > 5 and quantity <=10:
            discounted_price = price*0.5
        else:
            discounted_price = price
        return discounted_price

    @staticmethod
    def generate_bill(name, item, quantity, price, discount):
        print("\t\t*******INVOICE*******\t\t")
        print(f"Customer Name:{name}")
        print("Sno.\tItem-Name\tQuantity\tPrice\tDiscounted-Price")
        for i in range(0, len(item)):
            print(f" {i+1} \t\t{item[i]} \t\t{quantity[i]} \t\t{price[i]} \t\t{discount[i]}")
        print("Thank you!!For Shopping from our store,Hope you liked the service.\n")

    @staticmethod
    def add_item():
        item = []
        number = int(input("How many items do you want to add??\n"))
        f = open("Products_available", "r")
        for lines in f:
            item.append(lines)
        for i in range(number):
            name = input("Name of the product\n")
            price = input("Enter the price of the product\n")
            with open("Products_available", "a") as p:
                p.write(f"{len(item) + 1}-{name}-{price}\n")
        print("Products added successfully!!")

    def del_item(self):
        delete = True
        p_name = input("Enter the name of the product you want to delete\n")
        file = "updated_Products_available"
        self.product_det = []
        with open("Products_available") as p:
            for product_description in p:
                self.product_det.append(product_description)
        for prod in self.product_det:
            if p_name.lower() == prod.split("-")[1].lower():
                self.product_det.remove(prod)
                delete = True
                break
            else:
                delete = False
        if delete == False:
            print("Not available!!")
        for items1 in self.product_det:
            updated_file = open(file, "w")
            updated_file.write(items1)
            updated_file.close()
        if delete == True:
            print("File updated successfully!!")
        else:
            pass
        return file


if __name__ == '__main__':
    while True:
        role = input("Enter your designation(customer/owner)\n")
        if role.lower() == "customer":
            customer = Supermarket("Walmart")
            choice1 = int(input("Enter what do you want to do??\n"
                            "1.See/listen product list\n"
                            "2.Order product\n"))
            if choice1 == 1:
                customer.display_products()
            elif choice1 == 2:
                customer.order_products()
            else:
                print("Invalid request!!")
        elif role.lower() == "owner":
            owner = Supermarket("Walmart")
            choice2 = int(input("Enter what do you want to do??\n1.See/listen product list\n2.Add product"
                            "\n3.Delete product\n"))
            if choice2 == 1:
                owner.display_products()
            if choice2 == 2:
                owner.add_item()
            if choice2 == 3:
                new = owner.del_item()
                ch = input("Do you want to see the updated list(y/n)??\n")
                if ch =='y':
                    print("Following are the available items!!")
                    print("Sno.  Items  Price_amount")
                    with open(new) as u:
                        for lines in u:
                            print(lines.rstrip())
                else:
                    pass














