''' OOPS Mock Garden simulation '''

#importing modules
import time
import statistics
import math
from typing import final

class garden():
    def __init__(self, garden_name, capacity, waterneed, terrain, size):
        # Use underscored attributes for properties
        self._garden_name = None
        self._capacity = None
        self._waterneed = None
        # Set through properties for validation
        self.garden_name\
            = garden_name
        self.capacity = capacity
        self.waterneed = waterneed
        # Regular attributes
        self.terrain = terrain
        self.size = size

        global hashmap
        global plants_in_garden
        global plants_set
        hashmap = {}
        plants_in_garden = []  # Initialize this as a list instead of in add_plants
        plants_set = set()

    def __str__(self) -> str:
        return f" Garden Specifications :\n Name : {self.garden_name}, Capacity: {self.capacity}, Water needed : {self.waterneed}, Terrain : {self.terrain}, Size : {self.size}"

    def add_plants(self, pname, plant_type) -> str:
        
        if isinstance(pname, plants):
            try:
                self.pname = pname
                self.plant_type = plant_type
                hashmap[self.pname] = plant_type
                plants_in_garden.append(1)
                self.capacity -= 1
                plants_set.add(pname.pname
                               )# because when we add a plant the capacity decreases automatically
                return f" {pname} is now growing in the garden 🌱 ! "
            except Exception as e:
                return f" Error code 123 {pname} couldn't be added in the garden'\n {e}"
        else:
            raise ValueError(
                f"Unable to add {pname} in the garden error code 121 belongs to the category of plants")

        # limiter
        if len(plants_in_garden) >= self.capacity:
            raise ValueError(
                f"You've reached your limit of {self.capacity} plants")
        
    def check_plant_availibility(self, pname) -> str:
        self.pname = pname
        try:
            if self.pname in hashmap.keys():
                return f" {pname} is present in {self.garden_name}"
            else:
                return f" {pname} is not present in {self.garden_name}"
        except Exception as e:
            return f"Error {e}"

    def view_garden(self, g) -> str:
        self.g = g
        try:
            if not isinstance(g, garden):
                raise ValueError(" Invalid input enter your garden name")
            else:
                word = ''
                for key, value in hashmap.items():
                    word += f" {g.garden_name}  \n {key} belongign to the categiry of {value} \n"
                return word
        except Exception as e:
            return f"Error {e} unable to view garden"
    
    def uniqueplantsingarden(self):
        if not hasattr(self,'garden_name'):
            raise MemoryError(' Please select valid garden')
        if 'plants_set' not in globals():
            raise GeneratorExit(f" We found no plants in the garden")
        output = f"{self.garden_name} Unique Plants \n"
        for index, p in plants_set.enumerate():
            output+= f"{index}: {p}\n"

# adding a getter aka reeptionsit which throws back values 
    @property
    def capacity(self):
        return self._capacity
# setter aka bouncer which checks the values and makes sure only the right values are returned
    @capacity.setter 
    def capacity(self, value):
        if not isinstance(value,int):
                raise ValueError(f"Invalid input {value} \n capacity must be a number try again")
        else:
             self._capacity = value

    @property 
    def garden_name(self):
        return self._garden_name
        
    @garden_name.setter
    def garden_name(self, name):
        if not isinstance(name, str):
            raise TypeError('Invalid garden name type. Must be string.')
        self._garden_name = name

    @property 
    def waterneed(self):
        return self._waterneed

    @waterneed.setter  
    def waterneed(self, water):
        if isinstance(water, (int, float)): 
            self._waterneed = water
        else:
            raise TypeError('Invalid water need type. Must be number.')

class plants():

    def __init__(self,pname=None,plant_category=None,waterneed=None,sunlightneed=None,color=None):
        # Using underscore for attribute getter and setter
        self._pname = None
        self._plant_category = None
        self._waterneed = None
        self._sunlightneed = None
        self._color = None
        
        # Set each property through setters for validation
        self.pname = pname
        self.plant_category = plant_category
        self.waterneed = waterneed
        self.sunlightneed = sunlightneed
        self.color = color

    def __str__(self) -> str:
        try:
            output = f" Info \n Name: {self.pname}"

            if self.plant_category is not None:
                output += f" belongs to the category of {self.plant_category}"
            if self.color is not None:
                output += f" having color {self.color}"
            if self.waterneed is not None:
                output += f"Water_need{self.waterneed}"
            if self.sunlightneed is not None:
                output += f"Sunlightneed: {self.sunlightneed}"

            return output

        except Exception as e:
            return f"Error in printing plant details {e}"

#adding getters and setters
    @property
    def pname(self):
        return self._pname

    @pname.setter
    def pname(self,pn):
        if pn is not None and not isinstance(pn,str):
            raise ValueError(f"Invalid Plant name {pn} please enter a proper plant in the garden !")
        else:
            self._pname = pn

    # Plant category property
    @property
    def plant_category(self):
        return self._plant_category

    @plant_category.setter
    def plant_category(self, category):
        if category is not None and not isinstance(category, str):
            raise TypeError('Invalid plant category type. Must be string.')
        self._plant_category = category

    # Water need property
    @property
    def waterneed(self):
        return self._waterneed

    @waterneed.setter
    def waterneed(self, water):
        if water is not None and not isinstance(water, int):
            raise TypeError('Invalid water need type. Must be integer.')
        self._waterneed = water

    # Sunlight need property
    @property
    def sunlightneed(self):
        return self._sunlightneed

    @sunlightneed.setter
    def sunlightneed(self, sunlight):
        if sunlight is not None and not isinstance(sunlight, str):
            raise TypeError('Invalid sunlight need type. Must be string.')
        self._sunlightneed = sunlight

    # Color property
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, col):
        if col is not None and not isinstance(col, str):
            raise TypeError('Invalid color type. Must be string.')
        self._color = col


p1 = plants('Rosemary', 'Small shrub')

g1 = garden("Dave's Garden", 10, 12, 'Plains', 32)

#all functions running and now adding more plants in the garden 
print(g1.add_plants(p1, p1.plant_category))
print("\n")
print(g1.check_plant_availibility(p1))

print('\n')
view_1 = g1.view_garden(g1)
print(view_1)


p2 = plants('Snake Plant', 'Asparagace')
print(g1.add_plants(p2,p2.plant_category))

print(g1.check_plant_availibility(p2))

print(g1.uniqueplantsingarden())

