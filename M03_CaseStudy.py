#Billy Parrish
#SDEV 220
#M03 Case_study
#The program will ask the user for the year, make, model, doors, and the type of roof (solid or sunroof) for the type of vehicle they want. 
#It will then print the information back to the user in a use friendly format. There is a Super class called Vehicle and a sub class called Automobile.
#Inside the sub class there are 5 attributes that store the information that the user provides. Those attributes are year, make, model, doors, and roof.



class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

def main():
    print("Enter details for your car:")
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")
    doors = input("Doors (2/4): ")
    roof = input("Roof (solid or Sun roof): ")

    car = Automobile("car", year, make, model, doors, roof)

    print("Car details:")
    print(f"Vehicle Type: {car.vehicle_type}")
    print(f"Year: {car.year}")
    print(f"Make: {car.make}")
    print(f"Model: {car.model}")
    print(f"Doors: {car.doors}")
    print(f"Roof: {car.roof}")

if __name__ == "__main__":
    main()