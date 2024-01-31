import pandas as pd

df_cards = pd.read_csv("cards.csv", dtype = str).to_dict(orient = "records")
df_cards_security = pd.read_csv("card_security.csv", dtype = str)
df = pd.read_csv("hotels.csv", dtype = {"id":str}) # only the id columns will be treated as string
df2 = df.to_string(index = False)
print(df2)

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index = False)

    def available(self):
        """Checking the hotel's availability"""
        availability = df.loc[df["id"] == self.hotel_id]["available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False
        
class SpaHotel(Hotel):
    def book_spa_package(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_object): 
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank your for your reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}"""
        return content
    
class CreditCard:
    def __init__(self, number):
        self.number = number
    def validate(self, expiration, holder, cvc):
        card_data = {"number" : self.number, "expiration" : expiration, 
                     "holder" : holder, "cvc": cvc}
        if card_data in df_cards: # verifying if this full dictionary exists in cards.csv
            return True 
        else:
            return False
    
# heritage
class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        # this child class inherit the self.number's attribute from parent class "CreditCard"
        password = df_cards_security.loc[df_cards_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True 
        else:
            return False
        
class SpaTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object
    def generate(self):
        content = f"""
        Thank your for your SPA reservation!
        Here are your SPA booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}"""
        return content


hotel_ID = input("Enter the id of the hotel: ")
hotel = SpaHotel(hotel_ID)

if hotel.available():
    credit_card = SecureCreditCard(number = "1234567890123456")
    if credit_card.validate(expiration = "12/26", holder = "Luca Rossi", cvc = "123"):
        if credit_card.authenticate(given_password = "mypass"):
            hotel.book()
            name = input("Enter your name bro: ")
            reservation_ticket = ReservationTicket(customer_name = name, hotel_object = hotel)
            print(reservation_ticket.generate())
            spa = input("Do you want to book a spa package? ")
            if spa.lower() == "yes":
                hotel.book_spa_package()
                spa_ticket = SpaTicket(customer_name = name, hotel_object = hotel)
                print(spa_ticket.generate())
        else:
            print("Credit card authentication failed.")
    else:
        print("There was a problem with your payment")
else:
    print("Hotel is not free.")