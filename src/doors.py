from player import Player

class Door:
    def __init__(self, is_open=True, is_locked=False,):
        self.is_open = is_open
        self.is_locked = is_locked

    def open_door(self, player):
        if self.is_open:
            print("It's already opened.... Did you want to CLOSE it?")
            return
            
        if self.is_locked:
            print("This door is locked!")
            return
        self.is_open = True
        print("You opened the door!")
    
    def unlock_door(self, player):
        if not self.is_locked:
            print("This door isn't locked!")
            return

        if "key" in player.inventory:
            print("You unlocked the door!")
            player.inventory.pop("key")
            self.is_locked = False
        else: print("You need a key!")

        


class BossDoor(Door):
    def __init__(self, is_open=True, is_locked=False):
        super().__init__(is_open=is_open, is_locked=is_locked)
        
    def unlock_door(self, player):
    # Requires GOLDENKEY
        if not self.is_locked:
            print("This door isn't locked!")
            return

        if "golden key" in player.inventory:
            print("You unlocked the door, GOOD LUCK!")
            player.inventory.pop("key")
            self.is_locked = False
        else: print("You need a key!")

        
