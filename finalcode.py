class BikeRental:
    def __init__(self, stock=100):
        self.stock = stock
        print("Welcome to the Bike Rental Shop")

    def display_stock(self):
        print(f"\nAvailable bikes: {self.stock}")

    def rent_bike(self, quantity):
        if quantity <= 0:
            print("Number of bikes must be greater than zero")
            return False

        if quantity > self.stock:
            print("Not enough bikes available")
            return False

        self.stock -= quantity
        print(f"{quantity} bike(s) rented successfully")
        return True

    def return_bike(self, quantity):
        self.stock += quantity
        print(f"{quantity} bike(s) returned successfully")


class Customer:
    HOURLY_RATE = 20
    DAILY_RATE = 100
    WEEKLY_RATE = 500

    def __init__(self, bikes, basis, duration, late_days=0):
        self.bikes = bikes
        self.basis = basis.lower()
        self.duration = duration
        self.late_days = late_days

    def calculate_bill(self):
        if self.basis == "hourly":
            bill = self.bikes * self.duration * self.HOURLY_RATE
        elif self.basis == "daily":
            bill = self.bikes * self.duration * self.DAILY_RATE
        elif self.basis == "weekly":
            bill = self.bikes * self.duration * self.WEEKLY_RATE
        else:
            raise ValueError("Invalid rental basis")

        discount = 0
        if 3 <= self.bikes <= 5:
            discount = 0.30
            bill *= (1 - discount)

        penalty = self.late_days * 50
        bill += penalty

        return bill, discount, penalty

    def generate_receipt(self, bill, discount, penalty):
        print("\n========== RENTAL RECEIPT ==========")
        print(f"Bikes Rented : {self.bikes}")
        print(f"Rental Basis : {self.basis.capitalize()}")
        print(f"Duration     : {self.duration}")
        if discount > 0:
            print("Discount     : 30% Family Rental")
        else:
            print("Discount     : None")
        print(f"Late Penalty : ₹{penalty}")
        print(f"Total Bill   : ₹{int(bill)}")
        print("===================================")


def main():
    shop = BikeRental()
    shop.display_stock()

    try:
        bikes = int(input("\nEnter number of bikes: "))
        basis = input("Enter rental basis (hourly/daily/weekly): ")
        duration = int(input("Enter duration: "))
        late_days = int(input("Enter late return days (0 if none): "))
    except ValueError:
        print("Invalid input. Numbers only.")
        return

    customer = Customer(bikes, basis, duration, late_days)

    if shop.rent_bike(customer.bikes):
        bill, discount, penalty = customer.calculate_bill()
        customer.generate_receipt(bill, discount, penalty)
        shop.return_bike(customer.bikes)
        shop.display_stock()


if __name__ == "__main__":
    main()
