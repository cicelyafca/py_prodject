# Text Adventure Framework

This is a simple text adventure framework in Python that you can use as a starting point to create your own text-based games.

## Getting Started

1. Clone or download this repository to your local machine.

2. Run the script `text_adventure.py` with Python:

    ```bash
    python text_adventure.py
    ```

3. Follow the on-screen instructions to interact with the game. Use commands like `move`, `take`, `inventory`, and `quit` to navigate and explore.

## Game Structure

The framework consists of two main classes:

- **Room:** Represents a location in the game. Rooms have descriptions, exits to other rooms, and items that can be interacted with.

- **Player:** Represents the player character. The player can move between rooms, take items, and maintain an inventory.

## Customization

Feel free to customize and extend the framework to fit the needs of your specific game. You can add more features, create a larger map, and include complex puzzles to enhance the gaming experience.

## Example Usage

```python
# Example Room Creation
living_room = Room("Living Room", "A cozy living room with a fireplace.")
kitchen = Room("Kitchen", "A well-equipped kitchen with a dining table.")
garden = Room("Garden", "A beautiful garden with blooming flowers.")

# Adding Exits
living_room.add_exit("east", kitchen)
kitchen.add_exit("west", living_room)
kitchen.add_exit("south", garden)
garden.add_exit("north", kitchen)

# Adding Items
living_room.add_item("Key")
kitchen.add_item("Knife")

# Creating Player
player = Player(living_room)

# Starting the Game
player.current_room.display_info()
