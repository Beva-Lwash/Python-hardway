from sys import exit
from random import randint
from textwrap import dedent

class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

central_corridor = Room("Central Corridor",
"""
The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew. You are the lst surviving member and your last mission is to get the neutron destruct bomb from the Weapons Armory, put it in the bridge, and blow the ship up after getting into the escape pod.

You're running down the central corridor to the Weapons Armory when a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume flowing around his hate filled body. He's blocking the door to the Armory and anout to pull a weapon to blast you.
""")

laser_weapon_armory = Room("Laser Weapon Armory",
"""
Lucky for you they made you learn Gothon insults int he academy. You tell the one Gothon joke tou knoe: Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr. The Gothon stops, tries not to laugh, then busts out ;aughing and can't move. While he's laughing you run up and shoot him square in the head putting him down, then jump trough the Weapon Armory door.

You do a a dive roll into the Weapon Armory, crouch and scan the room for more Gothons that might be hiding . It's dead quiet, too quiet. You stand up and run to the far sideof the room and find the neutron bomb in its container. There's a keypad lock on the box and you need the code to get the bomb out. If you get the code wrong 10 times then the lock closes forever and you can't get the bomb. The code is 3 digits.
""")

the_bridge = Room("The Bridge",
"""
The container clicks open and teh seal breaks, letting gas out. You grab teh neutron bomb and run as fast as you can to the brisge where you must place it in the right spot.

You burst onto the Bridge with the neutron destruct bomb under your arm and surprise 5 Gothons who are trying to take control of the ship. Each of them has an even uglier clown costume than the lsat. They haven't
""")

escape_pod = Room("Escape Pod",
"""
You point your blaster at the bomb under your arm and the Gothons put their hands up and start to sweat. You inch backward to the door, open it , and then carefully place the bomb on the floor, pointing you blaster at it . You then jump back trough the door, punch the close button and blast the lock so the Gothons can't get out. Now that the bomb is placed you run to the escape pod to get off this tin can.

You rush through the ship desperately trying to make it to the escape pod before the whole ship explodes. It seems like hardly ant Gothons are on the ship, so your run is cleat of interference. You get to the chamber with the escape pods, and now need to pick one to take. Some of them could be damaged but you don't have time to look. There's 5 pods, which one do you take?
""")

the_end_winner = Room("The End",
"""
You jump into pod 2 and hit the eject button. the pod easily slides out into space heading to the planet below. As it flies to the planet, you look back and see your ship implode then explode like a bright star, taking out the Gothon ship at the same time. You won!
""")

the_end_loser = Room("The End",
"""
You jump into a random pod and hit the eject button. The pod escapes out into the coid of space, then implodes as the hull ruptures, crushing your body into jam jelly.
""")
shoot_death = Room('shoot', """
Quick on the draw you yank out your blaster and fire
it at the Gothon. His clown costume is flowing and
moving around his body, which throws off your aim.
Your laser hits his costume but misses him entirely.
This completely ruins his brand new costume his mothe
bought him, which makes him fly into an insane rage
and blast you repeatedly in the face until you are
dead. Then he eats you.
    """)

dodge_death = Room('dodge',"""
Like a world class boxer you dodge, weave, slip and
slide right as the Gothon's blaster cranks a laser
past your head. In the middle of your artful dodge
your foot slips and you bang your head on the metal
wall and pass out. You wake up shortly after only to
die as the Gothon stomps on your head and eats you.
                   """ )

throw_a_bomb = Room('throw a bomb', """
In a panic you throw the bomb at the group of Gothon
and make a leap for the door. Right as you drop it a
Gothon shoots you right in the back killing you. As
you die you see another Gothon frantically try to
disarm the bomb. You die knowing they will probably
blow up when it goes off.
         """)


tell_a_joke = Room('tell_a_joke', """
Lucky for you they made you learn Gothon insults in
the academy. You tell the one Gothon joke you know:
Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr
fur fvgf nebhaq gur ubhfr. The Gothon stops, tries
not to laugh, then busts out laughing and can't move.
While he's laughing you run up and shoot him square i
the head putting him down, then jump through the
Weapon Armory door.
            """)


escape_pod.add_paths({
    '2': the_end_winner,
    '*': the_end_loser,
})



the_bridge.add_paths({
    'throw the bomb': shoot_death,
    'slowly place the bomb': 'escape_pod'
})

laser_weapon_armory.add_paths({
    '0132': the_bridge,
    '*': shoot_death
})

central_corridor.add_paths({
    'shoot!': shoot_death,
    'dodge!': dodge_death,
    'tell a joke': laser_weapon_armory
})

shoot_death.add_paths({
    'died': 'death'})

dodge_death.add_paths({
    'died': 'death'})

throw_a_bomb.add_paths({
    'died': 'death'})

START = 'central_corridor'

roomsy = {central_corridor, laser_weapon_armory}
death_rooms_central_corridor = {shoot_death, dodge_death}
rooms = {central_corridor, laser_weapon_armory, shoot_death, dodge_death}

def load_room(name):
    for room in rooms:
        if room.name == name:
            return room

def name_room(room):
        if isinstance(room, Room):
            return room.name

class Scene(object):
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
            current_scene = self.scene_map.opening_scene()
            last_scene = self.scene_map.next_scene('finished')
            while current_scene != last_scene:
                next_scene_name = current_scene.enter()
                current_scene = self.scene_map.next_scene(next_scene_name)

            # be sure to print out the last scene
            current_scene.enter()

class Death(Scene):
    quips = [
        "You died. You kinda suck at this.",
        "Your Mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print(dedent(central_corridor.description))
        action = input("> ")

        if action in central_corridor.paths:
            if central_corridor.go(action) in death_rooms_central_corridor:
                print(dedent(central_corridor.go(action).description))
                return central_corridor.go(action).go('died')
            else:
                return 'laser_weapon_armory'
        else:
            print("Mauvais chemin!!!")
            return  'central_corridor'

class LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent(laser_weapon_armory.description))
        code = '0132'
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            return 'the_bridge'

        else:
            print(dedent(shoot_death.description))
            return shoot_death.go('died')

class TheBridge(Scene):
    def enter(self):
        print(dedent(the_bridge.description))
        action = input("> ")

        if action == "throw the bomb":
            return throw_a_bomb.go('died')
        elif action == "slowly place the bomb":
            return the_bridge.go(action)
        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"

class EscapePod(Scene):
    def enter(self):
        print(dedent(escape_pod.description))
        good_pod = 2
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(the_end_loser.description)
            return 'death'
        else:
            print(escape_pod.go('*').description)
            return 'finished'

class Finished(Scene):
    def enter(self):
        print("You won! Good job.")
        return 'finished'

class Map(object):
    scenes = {
'central_corridor': CentralCorridor(),
'laser_weapon_armory': LaserWeaponArmory(),
'the_bridge': TheBridge(),
'escape_pod': EscapePod(),
'death': Death(),
'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene


    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map  = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
