class Bank:
    def bank(self):
        return "Payment by Bank"
class Google_Pay(Bank):
    def bank(self):
        print("Payment by Google Pay")


obj=Google_Pay()
obj.bank()