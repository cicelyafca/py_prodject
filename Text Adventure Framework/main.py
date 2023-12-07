class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def add_item(self, item):
        self.items.append(item)

    def display_info(self):
        print(f"{self.name}\n{self.description}")
        if self.items:
            print("Items in the room:", ', '.join(self.items))
        if self.exits:
            print("Exits:", ', '.join(self.exits.keys()))

class Player:
    def __init__(self, start_room):
        self.current_room = start_room
        self.inventory = []

    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            self.current_room.display_info()
        else:
            print("There is no exit in that direction.")

    def take(self, item):
        if item in self.current_room.items:
            self.current_room.items.remove(item)
            self.inventory.append(item)
            print(f"You picked up {item}.")
        else:
            print("There is no such item in the room.")

    def display_inventory(self):
        if self.inventory:
            print("Your inventory:", ', '.join(self.inventory))
        else:
            print("Your inventory is empty.")

# Example of using the framework
if __name__ == "__main__":
    # Creating rooms
    living_room = Room("Living Room", "A cozy living room with a fireplace.")
    kitchen = Room("Kitchen", "A well-equipped kitchen with a dining table.")
    garden = Room("Garden", "A beautiful garden with blooming flowers.")

    # Defining Outputs
    living_room.add_exit("east", kitchen)
    kitchen.add_exit("west", living_room)
    kitchen.add_exit("south", garden)
    garden.add_exit("north", kitchen)

    # Adding items
    living_room.add_item("key")
    kitchen.add_item("knife")

    # Creating a Player
    player = Player(living_room)

    # Start the game
    player.current_room.display_info()

    while True:
        command = input("\nEnter your command (move/take/inventory/quit): ").lower()

        if command == "quit":
            print("Thanks for playing!")
            break

        elif command.startswith("move "):
            direction = command.split(" ", 1)[1]
            player.move(direction)

        elif command.startswith("take "):
            item = command.split(" ", 1)[1]
            player.take(item)

        elif command == "inventory":
            player.display_inventory()

        else:
            print("Invalid command. Try again.")
