class Robot: 

    def __init__(self):
        self.x_coordinate = 10
        self.y_coordinate = 10
        self.fuel_amount = 100

    def move_left(self):
        if self.fuel_amount < 5:
            print("Insufficient fuel to perform action")
        else: 
            self.fuel_amount -= 5
            self.x_coordinate -= 1
        return

    def move_right(self):
        if self.fuel_amount < 5:
            print("Insufficient fuel to perform action")
        else: 
            self.fuel_amount -= 5
            self.x_coordinate += 1
        return

    def move_up(self):
        if self.fuel_amount < 5:
            print("Insufficient fuel to perform action")
        else: 
            self.fuel_amount -= 5
            self.y_coordinate -= 1
        return

    def move_down(self):
        if self.fuel_amount < 5:
            print("Insufficient fuel to perform action")
        else: 
            self.fuel_amount -= 5
            self.y_coordinate += 1
        return

    def display_status(self):
        print("({}, {}) - Fuel: {}".format(self.x_coordinate, self.y_coordinate, self.fuel_amount))
        return

    def fire_laser(self):
        if self.fuel_amount < 15:
            print("Insufficient fuel to perform action")
        else:
            print("Pew! Pew!")
            self.fuel_amount -= 15
        return 

def main():
    Mr_Robot = Robot()
    command = ""
    while command != "quit":
        command = input("Enter command: ")
        if command == "left":
            Mr_Robot.move_left()
        elif command == "right":
            Mr_Robot.move_right()
        elif command == "up":
            Mr_Robot.move_up()
        elif command == "down":
            Mr_Robot.move_down()
        elif command == "fire":
            Mr_Robot.fire_laser()
        elif command == "status":
            Mr_Robot.display_status()
        elif command == "quit":
            print("Goodbye.")

if __name__ == "__main__":
    main()