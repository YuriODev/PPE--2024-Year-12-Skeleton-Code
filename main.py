import csv


class Application:
    def __init__(self):
        self.cars = []
        self.trucks = []
        self.suvs = []
        self.violations = []

    def load_data_from_files(self):
        self.cars = self.load_vehicles('cars.txt')
        self.trucks = self.load_vehicles('trucks.txt')
        self.suvs = self.load_vehicles('suvs.txt')
        self.violations = self.load_violations('violations.txt')

    def display_vehicles(self):
        print("\nVehicle Information")
        print("-" * 60)
        for vehicle in self.cars:
            print(f"Make: {vehicle.make},\n"
                  f"Model: {vehicle.model},\n"
                  f"Year: {vehicle.year},\n"
                  f"Mileage: {vehicle.mileage},\n"
                  f"Price: £{vehicle.price},\n"
                  f"Registration: {vehicle.registration_number}")
            if isinstance(vehicle, Car):
                print(f"Doors: {vehicle.doors}")
            elif isinstance(vehicle, Truck):
                print(f"Drive Type: {vehicle.drive_type}")
            elif isinstance(vehicle, SUV):
                print(f"Passenger Capacity: {vehicle.passenger_capacity}")
            print("-" * 60)

    def display_violations(self):
        print("\nSpeed Violations")
        print("-" * 40)
        for violation in self.violations:
            print(f"Registration: {violation.registration_number},\n"
                  f"Date: {violation.violation_date},\n"
                  f"Speed: {violation.speed} MPH,\n"
                  f"Limit: {violation.limit} MPH")
            over_limit = int(violation.speed) - int(violation.limit)
            print(f"Over Limit: {over_limit} MPH")
            print("-" * 40)

    def add_new_car(self):
        registration_number = input("Enter registration number: ")
        make = input("Enter make: ")
        model = input("Enter model: ")
        year = input("Enter year: ")
        mileage = input("Enter mileage: ")
        price = input("Enter price: ")
        doors = input("Enter number of doors: ")
        new_car = Car(registration_number, make, model, year, mileage, price, doors)
        vehicles = self.load_vehicles('cars.txt')
        vehicles.append(new_car)
        self.save_vehicles('cars.txt', vehicles)
        print("New car added successfully.")

    def record_new_violation(self):
        registration_number = input("Enter registration number: ")
        violation_date = input("Enter violation date (YYYY-MM-DD): ")
        speed = input("Enter speed: ")
        limit = input("Enter speed limit: ")
        new_violation = SpeedViolation(registration_number, violation_date, speed, limit)
        violations = self.load_violations('violations.txt')
        violations.append(new_violation)
        self.save_violations('violations.txt', violations)
        print("New speed violation recorded successfully.")

    def load_vehicles(self, filename):
        vehicles = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if filename == 'cars.txt':
                    vehicles.append(Car(*row))
                elif filename == 'trucks.txt':
                    vehicles.append(Truck(*row))
                elif filename == 'suvs.txt':
                    vehicles.append(SUV(*row))
        return vehicles

    def save_vehicles(self, filename, vehicles):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for vehicle in vehicles:
                writer.writerow(vehicle.__dict__.values())

    def load_violations(self, filename):
        violations = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                violations.append(SpeedViolation(*row))
        return violations

    def save_violations(self, filename, violations):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for violation in violations:
                writer.writerow(violation.__dict__.values())


class Vehicle:
    def __init__(self, registration_number, make, model, year, mileage, price):
        self.registration_number = registration_number
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.price = price


class Car(Vehicle):
    def __init__(self, registration_number, make, model, year, mileage, price, doors):
        super().__init__(registration_number, make, model, year, mileage, price)
        self.doors = doors


class Truck(Vehicle):
    def __init__(self, registration_number, make, model, year, mileage, price, drive_type):
        super().__init__(registration_number, make, model, year, mileage, price)
        self.drive_type = drive_type


class SUV(Vehicle):
    def __init__(self, registration_number, make, model, year, mileage, price, passenger_capacity):
        super().__init__(registration_number, make, model, year, mileage, price)
        self.passenger_capacity = passenger_capacity


class SpeedViolation:
    def __init__(self, registration_number, violation_date, speed, limit):
        self.registration_number = registration_number
        self.violation_date = violation_date
        self.speed = speed
        self.limit = limit


def main_menu(app):
    while True:
        print("\nMain Menu")
        print("1) Show all vehicles")
        print("2) Show all speed violations")
        print("3) Add new car")
        print("4) Record speed violation")
        print("5) Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            app.display_vehicles()
        elif choice == '2':
            app.display_violations()
        elif choice == '3':
            app.add_new_car()
        elif choice == '4':
            app.record_new_violation()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    app = Application()
    app.load_data_from_files()
    main_menu(app)
