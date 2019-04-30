# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 12:10:40 2018

@author: NathanLHall
"""

import csv
from datetime import datetime
quality_threshold = 0.9

# Not (fully) implemented:
    # Architect
    # Armorsmith
    # Artisan
    # Bio-Engineer
    # Chef
    # Droid Engineer
    # Smuggler
    # Shipwright - Ithorian & Sullustan
    # Tailor
    # Weaponsmith


#    *´¨)
#    ¸.•´¸.•*´¨) ¸.•*¨)
#    (¸.•´ (¸.•` ¤ CRAFTABLE ITEMS*´¨)

                 #[("<resource>", "<craftable item>", ["<primary attribute>", "<secondary attribute>", ...])

architect_items = [("Conductive Borcarbitic Copper", "Crafting Stations/Tools", ["Quality"]),
                   ("Crystallized Bicorbantium Steel", "Heavy Harvesting Mechanism, Crafting Stations/Tools", ["Quality", "Extraction Rate", "Hopper Size"]),
                   ("Duralloy Steel", "Heavy Harvesting Mechanism", ["Extraction Rate", "Hopper Size"]),
                   ("Fermionic Siliclastic Ore", "Heavy Harvesting Mechanism", ["Extraction Rate", "Hopper Size"]),
                   ("Hardened Arveshium Steel", "Heavy Harvesting Mechanism, Crafting Stations/Tools", ["Quality", "Extraction Rate", "Hopper Size"]),
                   ("Kammris Iron", "Heavy Harvesting Mechanism", ["Extraction Rate", "Hopper Size"]),
                   ("Katrium Intrusive Ore", "Heavy Harvesting Mechanism", ["Extraction Rate", "Hopper Size"]),
                   ("Perovskitic Aluminum", "Crafting Stations/Tools", ["Quality"]),
                   ("Polysteel Copper", "Crafting Stations/Tools", ["Quality"]),
                   ("Unknown Ferrous Metal", "Heavy Harvesting Mechanism", ["Extraction Rate", "Hopper Size"]),
                   ("Unknown Gem Type", "Heavy Harvesting Mechanism", ["Extraction Rate", "Hopper Size"]),
                   ("Unknown Igneous Ore", "Heavy Harvesting Mechanism", ["Extraction Rate", "Hopper Size"]),
                   ("Unknown Non-Ferrous Metal", "Crafting Stations/Tools", ["Quality"]),
                   ("Vertex Crystalline Gemstone", "Heavy Harvesting Mechanism", ["Extraction Rate", "Hopper Size"]),
                   ("Vintrium Extrusive Ore", "Heavy Harvesting Mechanism", ["Extraction Rate", "Hopper Size"])]

armorsmith_items = [("Aluminum", "Composite Armor", ["Encumbrance", "Integrity", "Effectiveness", "Special Effectiveness"]),
                    ("Beyrllius Copper", "Composite Armor", ["Encumbrance", "Integrity", "Effectiveness", "Special Effectiveness"]),
                    ("Colat Iron", "Advanced Composite Armor Segment", ["Encumbrance", "Integrity", "Effectiveness", "Special Effectiveness"]),
                    ("Intrusive Ore", "Composite Armor", ["Encumbrance", "Integrity", "Effectiveness", "Special Effectiveness"]),
                    ("Kiirium Steel", "Advanced Composite Armor Segment", ["Encumbrance", "Integrity", "Effectiveness", "Special Effectiveness"]),
                    ("Nabooian Fiberplast", "Composite Armor", ["Encumbrance", "Integrity", "Effectiveness", "Special Effectiveness"]),
                    ("Polysteel Copper", "Advanced Composite Armor Segment", ["Encumbrance", "Integrity", "Effectiveness", "Special Effectiveness"]),
                    ("Solid Petro Fuel", "Composite Armor", ["Encumbrance", "Integrity", "Effectiveness", "Special Effectiveness"]),
                    ("Wooly Hide", "Composite Armor", ["Encumbrance", "Integrity", "Effectiveness", "Special Effectiveness"]),]

artisan_items = [("Kammris Iron", "Swoop", ["Hit Points"]),
                 ("Crystallized Bicorbantium Steel", "Swoop", ["Hit Points"]),
                 ("Hardened Arveshium Steel", "Swoop", ["Hit Points"]),
                 ("Unknown Ferrous Metal", "Swoop", ["Hit Points"]),
                 ("Perovskitic Aluminum", "Swoop", ["Hit Points"]),
                 ("Conductive Borcarbitic Copper", "Swoop", ["Hit Points"]),]

bio_engineer_items = []

chef_items = [("Berry", "Vasarian Brandy", ["Nutritional Value", "Filling", "Flavor", "Food Quantity"]),
              ("Fruit", "Citros Snow Cake, Pikatta Pie, Pyollian Cake, Vasarian Brandy", ["Nutritional Value", "Filling", "Flavor", "Food Quantity"]),
              ("Oat", "Pyollian Cake", ["Nutritional Value", "Filling", "Food Quantity"]),
              ("Tatooinian Berry Fruit", "Bespin Port", ["Nutritional Value", "Filling", "Food Quantity"]),
              ("Tatooinian Fruit", "Bespin Port", ["Nutritional Value", "Filling", "Food Quantity"]),
              ("Tatooinian Vegetable Tubers", "Bespin Port", ["Nutritional Value", "Filling", "Food Quantity"]),
              ("Water", "Pikatta Pie", ["Nutritional Value", "Filling", "Flavor", "Food Quantity"]),
              ("Wheat", "Pikatta Pie", ["Nutritional Value", "Filling", "Flavor", "Food Quantity"]),
              ("Wild Wheat", "Citros Snow Cake", ["Nutritional Value", "Filling", "Flavor", "Food Quantity"])]

combat_medic_items = [("Aluminum", "Ranged Stimpack - E", ["Combat Medic Power", "Range", "Medical Charges", "Skill", ]),
            ("Class 1 Radioactive", "Advanced Resilience Compound", ["Potency", "Duration"]),
            ("Class 2 Liquid Petro Fuel", "Advanced Dispersal Mechanism", ["Medical Charges", "Range", "Area"]),
            ("Class 4 Liquid Petro Fuel", "ACRDM", ["Doctor Power"]),
            ("Dantooine Berry Fruit", "Advanced Liquid Suspension", ["Doctor Power"]),
            ("Eleton Reactive Gas", "Advanced Infection Amplifier", ["Combat Medic Power"]),
            ("Fiberplast", "Area Stimpack - C, Ranged Stimpack - E", ["Combat Medic Power", "Range", "Area", "Medical Charges", "Skill"]),
            ("Fungi", "HAM (Area) Poison Delivery Unit - C", ["Combat Medic Power", "Range", "Potency", "Area", "Duration", "Medical Charges", "Skill"]),
            ("Herbivore Meat", "ACRDM", ["Doctor Power"]),
            ("Insect Meat", "HAM (Area) Disease Delivery Unit - C", ["Combat Medic Power", "Potency", "Range", "Area", "Duration", "Medical Charges", "Skill"]),
            ("Liquid Petro Fuel", "HAM (Area) Poison Delivery Unit - C", ["Combat Medic Power", "Potency", "Range", "Area", "Duration", "Medical Charges", "Skill"]),
            ("Lokian Wild Wheat", "ABEC", ["Doctor Power", "Medical Charges"]),
#            ("Non-Ferrous Metal", "HAM (Area) Disease/Poison Delivery Unit - C, Area Stimpack - C", ["Combat Medic Power", "Potency", "Range", "Area", "Duration", "Medical Charges", "Skill"]),
#            ("Organic", "Area Stimpack - C, Ranged Stimpack - E", ["Combat Medic Power", "Range", "Area", "Medical Charges", "Skill"]),
            ("Radioactive", "HAM (Area) Disease Delivery Unit - C", ["Combat Medic Power", "Potency", "Range", "Area", "Duration", "Medical Charges", "Skill"]),
            ("Talusian Water Vapor", "Advanced Liquid Suspension", ["Doctor Power"]),
            ("Tatooinian Fiberplast", "ABEC", ["Medical Charges", "Doctor Power"]),
            ("Tolium Reactive", "Advanced Resilience Compound", ["Potency", "Duration"]),
            ("Titanium Aluminum", "Advanced Infection Amplifier", ["Combat Medic Power"]),
            ("Yavinian Fiberplast", "Advanced Dispersal Mechanism", ["Medical Charges", "Range", "Area"])]

droid_engineer_items = [("Conductive Borcarbitic Copper", "Crafting Stations/Tools", ["Charge"]),
                        ("Crystallized Bicorbantium Steel", "Droid Battery", ["Charge"]),
                        ("Hardened Arveshium Steel", "Droid Battery", ["Charge"]),
                        ("Perovskitic Aluminum", "Droid Battery", ["Charge"]),
                        ("Polysteel Copper", "Droid Battery", ["Charge"]),
                        ("Unknown Non-Ferrous Metal", "Droid Battery", ["Charge"])]

doctor_items = [("Aluminum", "Flame Suppresion Blanket", ["Doctor Power", "Medical Charges", "Skill"]),
            ("Avian Meat", "Buffs", ["Doctor Power", "Duration", "Medical Charges"]),
            ("Beans", "Resist Poison", ["Doctor Power", "Duration", "Absorption", "Medical Charges"]),
            ("Class 4 Liquid Petro Fuel", "ACRDM", ["Doctor Power"]),
            ("Dantooine Berry Fruit", "Advanced Liquid Suspension", ["Doctor Power"]),
            ("Dolovite Iron", "ASDS", ["Doctor Power"]),
            ("Domesticated Oats", "ASDS", ["Doctor Power"]),
            ("Dylinium Intrusive Ore", "Resist Poison", ["Doctor Power", "Duration", "Absorption", "Medical Charges"]),
            ("Flower", "Cure Poison", ["Doctor Power", "Medical Charges", "Skill"]),
            ("Greens", "Cure Disease", ["Doctor Power", "Medical Charges", "Skill"]),
            ("Herbivore Meat", "ACRDM", ["Doctor Power"]),
            ("Inert Gas", "Cure Disease/Poison", ["Doctor Power", "Medical Charges", "Skill"]),
            ("Lokian Animal Bones", "Resist Disease", ["Doctor Power", "Duration", "Absoprtion", "Medical Charges"]),
            ("Lokian Wild Wheat", "ABEC", ["Medical Charges", "Doctor Power"]),
            ("Polymer", "Wound Packs, Resist Disease/Poison", ["Doctor Power", "Duration", "Absorption", "Medical Charges", "Skill"]),
            ("Reactive Gas", "Buffs", ["Medical Charges", "Duration", "Doctor Power"]),
            ("Regvis Amorphous Gemstone", "Resist Disease", ["Doctor Power", "Duration", "Absorption", "Medical Charges"]),
            ("Rori Vegetable Fungus", "Flame Suppresion Blanket", ["Doctor Power", "Medical Charges", "Skill"]),
            ("Talusian Water Vapor", "Advanced Liquid Suspension", ["Doctor Power"]),
            ("Tatooinian Fiberplast", "ABEC", ["Medical Charges", "Doctor Power"]),
            ("Tatooinian Herbivore Meat", "Resist Poison", ["Doctor Power", "Duration", "Absorption", "Medical Charges"]),
            ("Tubers", "Wound Packs", ["Doctor Power", "Medical Charges", "Skill"]),
            ("Wild Corn", "Resist Disease", ["Doctor Power", "Duration", "Absorption", "Medical Charges"])]

ranger_items = [("Bone", "Camo Kit", ["Quantity"]),
                ("Hide", "Camo Kit", ["Quantity"]),
                ("Meat", "Camo Kit", ["Quantity"])]

#smuggler_items = [("Molecular Clamp",Non-Ferrous Metal,[]),
#                  ("Precision Laser Knife",Metal,[]),]

shipwright_items = []

tailor_items = []

weaponsmith_items = [("Polymer", "Imperial Detonator", ["Speed", "Damage"]),
                     ("Steel", "Imperial Detonator", ["Speed", "Damage"]),
                     ("Low-Grade Ore", "Warhead Fusing Mechanism", ["Speed"]),
                     ("Metal", "Warhead Fusing Mechanism", ["Speed"]),
                     ("Amorphous Gemstone", "Warhead Fusing Mechanism", ["Speed"])]
#                     ("", "Warhead Stabilizing Device", []),
#                     ("", "Meadium Warhead Mechanism", [])]
#    *´¨)
#    ¸.•´¸.•*´¨) ¸.•*¨)
#    (¸.•´ (¸.•` ¤ RESOURCE CLASSES *´¨)



#    *´¨)
#    ¸.•´¸.•*´¨) ¸.•*¨)
#    (¸.•´ (¸.•` ¤ DATA IMPORT AND CONVERSION*´¨)
class resource:
    def __init__(self, Type, CR=0, CD=0, DR=0, FL=0, HR=0, MA=0, PE=0, OQ=0, SR=0, UT=0,
                 ER=0, Name=None, Planets=None, Date=None):
        self.Type = Type
        self.CR = int(CR)
        self.CD = int(CD)
        self.DR = int(DR)
        self.FL = int(FL)
        self.HR = int(HR)
        self.MA = int(MA)
        self.PE = int(PE)
        self.OQ = int(OQ)
        self.SR = int(SR)
        self.UT = int(UT)
        self.ER = int(ER)
        self.Name = Name
        self.Planets = Planets
        self.Date = Date
        self.stats = [("CR", self.CR), ("CD", self.CD), ("DR", self.DR), ("FL", self.FL),
                      ("HR", self.HR), ("MA", self.MA), ("PE", self.PE), ("OQ", self.OQ),
                      ("SR", self.SR), ("UT", self.UT), ("ER", self.ER)]
        self.absorption = 2/3 * self.OQ + 1/3 * self.PE
        self.area = 2/3 * self.OQ + 1/3 * self.CD
        self.droid_charges = 0.5 * self.OQ + 0.5 * self.CD
        self.charge = self.CD
        self.medical_charges = 2/3 * self.OQ + 1/3 * self.UT
        self.damage = 0.5 * self.OQ + 0.5 * self.SR
        self.duration = 0.5 * self.OQ + 0.5 * self.DR
        self.effectiveness = 0.5 * self.OQ + 0.5 * self.SR
        self.encumbrance = 0.5 * self.MA + 0.5 * self.OQ
        self.extraction = 0.5 * self.UT + 0.25 * self.HR + 0.25 * self.SR
        self.filling = 0.75 * self.DR + 0.25 * self.OQ
        self.flavor = 2/3 * self.FL + 1/3 * self.OQ
        self.food_quantity = 0.75 * self.PE + 0.25 * self.DR
        self.hit_points = self.SR
        self.hopper = 2/3 * self.UT + 1/3 * self.MA
        self.integrity = 0.5 * self.OQ + 0.5 * self.UT
        self.nutrition = 2/3 * self.PE + 1/3 * self.OQ
        self.potency = 2/3 * self.OQ + 1/3 + self.DR
        self.doctor_power = 2/3 * self.OQ + 1/3 * self.PE
        self.combat_medic_power = 0.75 * self.OQ + 0.25 * self.DR
        self.quality = self.CD
        self.quantity = self.OQ
        self.range = 2/3 * self.OQ + 1/3 * self.CD
        self.skill = 2/3 * self.OQ + 1/3 * self.PE
        self.speed = 0.5 * self.OQ + 0.5 * self.SR
        self.special_effectiveness = 0.5 * self.OQ + 0.5 * self.SR

    def display(self):
        print("--", self.Type, "--")
        print("Name:", self.Name)
        print("Date:", self.Date)
        print("CR:", self.CR)
        print("CD:", self.CD)
        print("DR:", self.DR)
        print("FL:", self.FL)
        print("HR:", self.HR)
        print("MA:", self.MA)
        print("PE:", self.PE)
        print("OQ:", self.OQ)
        print("SR:", self.SR)
        print("UT:", self.UT)
        print("ER:", self.ER)
        print("Planets:", self.Planets)

def convert_Galaxy_Harvester(data):
    if "Egg Meat" in data[5]:
        cut = data[5].index("Egg")
        data[5] = data[5][:cut] + "Egg"
    elif "Reptillian" in data[5]:
        cut1 = data[5].index("Reptillian")
        cut2 = cut1 + len("Reptillian")
        data[5] = data[5][:cut1] + "Reptilian" + data[5][cut2:]

    new_resource = resource(data[5], data[7], data[8], data[9], data[10], data[11],
                            data[12], data[13], data[14],data[15], data[16], data[17],
                            data[0], data[19], data[3])
    return new_resource

def convert_SWGCraft(data, resources):
    if data[4] == "Corellia Berry Fruit":
        data[4] = "Corellian Berry Fruit"
    if data[4] == "Corellia Evergreen Wood":
        data[4] = "Corellian Evergreen Wood"
    if data[4] == "Corellia Fiberplast":
        data[4] = "Corellian Fiberplast"
    if data[4] == "Corellia Flower Fruit":
        data[4] = "Corellian Flower Fruit"
    if data[4] == "Dathomir Water Vapor":
        data[4] = "Dathomirian Water Vapor"
    if data[4] == "Dathomir Wild Wheat":
        data[4] = "Dathomirian Wild Wheat"
    new_resource = resource(data[4], # Type
                            data[7], # CR
                            data[8], # CD
                            data[9], # DR
                            data[10], # FL
                            data[11], # HR
                            data[12], # MA
                            data[16], # PE
                            data[13], # OQ
                            data[14], # SR
                            data[15], # UT
                            data[6], # ER
                            data[3]) # Name

    for listing in resources:
        if listing.Name.title() == new_resource.Name.title():
            return None

    return new_resource

def convert_max(data):

    for i in range(len(data)):
        if data[i] == '' or data[i] == "?--->" or data[i] == "<---?":
            data[i] = 0
    new_resource = resource(data[0], data[2], data[4], data[6], data[8], data[10],
                                data[12], data[14], data[16], data[18], data[20], data[22])
    return new_resource

def missing(resources, resources_max):
    missing = set()

    for resource_max in resources_max:
        if "Asteroid" in resource_max.Type:
            continue
        elif "Blended" in resource_max.Type:
            continue
        elif "Chemical Compound" in resource_max.Type:
            continue
        elif "Combined Radioactive" in resource_max.Type:
            continue
        elif "Degraded Solid" in resource_max.Type:
            continue
        elif "Geothermal" in resource_max.Type:
            continue
        elif "Ground" in resource_max.Type:
            continue
        elif "Homogenized" in resource_max.Type:
            continue
        elif "Kashyyyk" in resource_max.Type:
            continue
        elif "Low Grade Ore" in resource_max.Type:
            continue
        elif "Low Quality Gemstone" in resource_max.Type:
            continue
        elif "Mixed" in resource_max.Type:
            continue
        elif "Mustafar" in resource_max.Type:
            continue
        elif "Processed" in resource_max.Type:
            continue
        elif "Smelted" in resource_max.Type:
            continue
        elif "Synthesized" in resource_max.Type:
            continue
        elif "Water Solution" in resource_max.Type:
            continue
        elif "Weak Geothermal" in resource_max.Type:
                continue
        else:
            missing.add(resource_max.Type)

    listed = set()
    for resource in resources:
        listed.add(resource.Type)

    for listing in listed:
        missing.remove(listing)

    missing_list = []
    for item in missing:
        missing_list.append(item)
        missing_list = sorted(missing_list)

    return missing_list

def screen(profession, resource, resource_max, items, primary_attribute, secondary_attribute, listings):
    for item in items:
        listing = []
        # if resource used in item matches current resource
        if item[0] in resource.Type:
            # Add the current resource to listing
            listing.append(resource)
            # Add which craft item it is used in to listing
            listing.append(item[1])
            # Cycle through experimental attributes
            for attribute in item[2]:
                # Search the attribute and add it to the listing
                if attribute == "Absorption":
                    listing.append(("Absorption", round(100 * resource.absorption / resource_max.absorption, 1)))
                elif attribute == "Area":
                    listing.append(("Area", round(100 * resource.area / resource_max.area, 1)))
                elif attribute == "Medical Charges":
                    listing.append(("Medical Charges", round(100 * resource.medical_charges / resource_max.medical_charges, 1)))
                elif attribute == "Combat Medic Power":
                    listing.append(("Power", round(100 * resource.combat_medic_power / resource_max.combat_medic_power, 1)))
                elif attribute == "Doctor Power":
                    listing.append(("Power", round(100 * resource.doctor_power / resource_max.doctor_power, 1)))
                elif attribute == "Damage":
                    listing.append(("Damage", round(100 * resource.damage / resource_max.damage, 1)))
                elif attribute == "Duration":
                    listing.append(("Duration", round(100 * resource.duration / resource_max.duration, 1)))
                elif attribute == "Effectiveness":
                    listing.append(("Effectiveness", round(100 * resource.effectiveness / resource_max.effectiveness, 1)))
                elif attribute == "Encumbrance":
                    listing.append(("Encumbrance", round(100 * resource.encumbrance / resource_max.encumbrance, 1)))
                elif attribute == "Extraction Rate":
                    listing.append(("Extraction Rate", round(100 * resource.extraction / resource_max.extraction, 1)))
                elif attribute == "Filling":
                    listing.append(("Filling", round(100 * resource.filling / resource_max.filling, 1)))
                elif attribute == "Flavor":
                    listing.append(("Flavor", round(100 * resource.flavor / resource_max.flavor, 1)))
                elif attribute == "Hit Points":
                    listing.append(("Hit Points", round(100 * resource.hit_points / resource_max.hit_points, 1)))
                elif attribute == "Hopper Size":
                    listing.append(("Hopper Size", round(100 * resource.hopper / resource_max.hopper, 1)))
                elif attribute == "Integrity":
                    listing.append(("Integrity", round(100 * resource.integrity / resource_max.integrity, 1)))
                elif attribute == "Nutritional Value":
                    listing.append(("Nutritional Value", round(100 * resource.nutrition / resource_max.nutrition, 1)))
                elif attribute == "Quality":
                    listing.append(("Quality", round(100 * resource.quality / resource_max.quality, 1)))
                elif attribute == "Food Quantity":
                    listing.append(("Quantity", round(100 * resource.food_quantity / resource_max.food_quantity, 1)))
                elif attribute == "Potency":
                    listing.append(("Potency", round(100 * resource.potency / resource_max.potency, 1)))
                elif attribute == "Quantity":
                    listing.append(("Quantity", round(100 * resource.quantity / resource_max.quantity, 1)))
                elif attribute == "Range":
                    listing.append(("Range", round(100 * resource.range / resource_max.range, 1)))
                elif attribute == "Skill":
                    listing.append(("Skill", round(100 * resource.skill / resource_max.skill, 1)))
                elif attribute == "Speed":
                    listing.append(("Speed", round(100 * resource.speed / resource_max.speed, 1)))
                elif attribute == "Special Effectiveness":
                    listing.append(("Special Effectiveness", round(100 * resource.special_effectiveness / resource_max.special_effectiveness, 1)))

            return listing

def export(title, listings, primary_emphasis=True):
    # listing = [<resource>, <craft item>, (<attribute>, <percent>), ...]
    with open("D:\\Games\\SWGEmu\\Resource Reports\\" + title + ".txt", 'w') as f:
        if title == "Missing":
            for item in listings:
                f.write(item + '\n')
        elif primary_emphasis == False:
            for listing in listings:
                # Check for at least 90% rating on ANY attribute
                for i in range(len(listing) - 2):
                    if listing[2 + i][1] >= 90.0:
                        f.write("Resource - ")
                        f.write(listing[0].Type)
                        f.write('\n')
                        f.write("Item - ")
                        f.write(listing[1])
                        f.write('\n')
                        f.write("Name - ")
                        f.write(listing[0].Name.title())
                        f.write('\n')

                        # Write the non-zero stats of the resource
                        for i in range(11): # There are 11 stats on a resource
                            if listing[0].stats[i][1] > 0:
                                f.write(listing[0].stats[i][0] + " - ")
                                f.write(str(listing[0].stats[i][1]))
                                f.write('\n')

                        # Write the ratings of the resource
                        for i in range(len(listing[2:])):
                            line = "{0} - {1}".format(listing[2 + i][0], listing[2 + i][1])
                            f.write(line)
                            f.write('%')
                            f.write('\n')

                        if listing[0].Planets != None:
                            f.write("Location(s) - ")
                            f.write(listing[0].Planets)
                            f.write('\n')

                        f.write('\n')
                        break
        else:
            for listing in listings:
                # Check for at least 90% rating on PRIMARY attribute
                if listing[2][1] >= 90.0:
                    f.write("Resource - ")
                    f.write(listing[0].Type)
                    f.write('\n')
                    f.write("Item - ")
                    f.write(listing[1])
                    f.write('\n')
                    f.write("Name - ")
                    f.write(listing[0].Name.title())
                    f.write('\n')

                    # Write the non-zero stats of the resource
                    for i in range(11): # There are 11 stats on a resource
                        if listing[0].stats[i][1] > 0:
                            f.write(listing[0].stats[i][0] + " - ")
                            f.write(str(listing[0].stats[i][1]))
                            f.write('\n')

                    # Write the ratings of the resource
                    for i in range(len(listing[2:])):
                        line = "{0} - {1}".format(listing[2 + i][0], listing[2 + i][1])
                        f.write(line)
                        f.write('%')
                        f.write('\n')

                    if listing[0].Planets != None:
                        f.write("Location(s) - ")
                        f.write(listing[0].Planets)
                        f.write('\n')

                    f.write('\n')

def main():
#    *´¨)
#    ¸.•´¸.•*´¨) ¸.•*¨)
#    (¸.•´ (¸.•` ¤ Galaxy Harvester *´¨)

    PATH = "D:\\Downloads\\"
    filename = "current14.csv"
    contents = []
    resources = []
    with open(PATH + filename) as file:
        dump = csv.reader(file, delimiter = ',')
        for row in dump:
            contents.append(row)
    for i in range(len(contents) - 1):
        resources.append(convert_Galaxy_Harvester(contents[i + 1]))

#    *´¨)
#    ¸.•´¸.•*´¨) ¸.•*¨)
#    (¸.•´ (¸.•` ¤ SWGCraft Project *´¨)

    PATH = "D:\\Downloads\\"
    filename = "currentresources_basilisk.csv"
    contents = []
    with open(PATH + filename) as file:
        dump = csv.reader(file, delimiter = ',')
        for row in dump:
            contents.append(row)
    for i in range(len(contents) - 1):
        possible_new_resource = convert_SWGCraft(contents[i + 1], resources)
        if possible_new_resource != None:
            resources.append(possible_new_resource)

#    *´¨)
#    ¸.•´¸.•*´¨) ¸.•*¨)
#    (¸.•´ (¸.•` ¤ Max Data Table *´¨)

    PATH = "D:\\Games\\SWGEmu\\"
    max_filename = "Resource Guide.csv"
    contents = []
    resources_max = []
    with open(PATH + max_filename) as file:
        dump = csv.reader(file, delimiter = ',')
        for row in dump:
            contents.append(row)
    for i in range(len(contents) - 1):
        resources_max.append(convert_max(contents[i + 1]))

    ### Search Filter ###
    architect_list = []
    armorsmith_list = []
    artisan_list = []
    chef_list = []
    combat_medic_list = []
    doctor_list = []
    ranger_list = []
    weaponsmith_list = []

    # Go through each resource
    for resource in resources:
        # Find the matching resource in the maximum list
        for resource_max in resources_max:
            if resource.Type == resource_max.Type:

                architect_result = screen("Architect", resource, resource_max, architect_items, "Quality", None, architect_list)
                armorsmith_result = screen("Armorsmith", resource, resource_max, armorsmith_items, "Quality", None, architect_list)
                artisan_result = screen("Artisan", resource, resource_max, artisan_items, "Quality", None, artisan_list)
                chef_result = screen("Ranger", resource, resource_max, chef_items, "Nutritional Value", None, chef_list)
                combat_medic_result = screen("Combat Medic", resource, resource_max, combat_medic_items, "Combat Medic Power", "Potency", combat_medic_list)
                doctor_result = screen("Doctor", resource, resource_max, doctor_items, "Doctor Power", None, doctor_list)
                ranger_result = screen("Ranger", resource, resource_max, ranger_items, "Quantity", None, ranger_list)
                weaponsmith_result = screen("Weaponsmith", resource, resource_max, weaponsmith_items, None, None, weaponsmith_list)

                if architect_result != None and architect_result != []:
                    architect_list.append(architect_result)
                if armorsmith_result != None and armorsmith_result != []:
                    armorsmith_list.append(armorsmith_result)
                if artisan_result != None and artisan_result != []:
                    artisan_list.append(artisan_result)
                if chef_result != None and chef_result != []:
                    chef_list.append(chef_result)
                if combat_medic_result != None and combat_medic_result != []:
                    combat_medic_list.append(combat_medic_result)
                if doctor_result != None and doctor_result != []:
                    doctor_list.append(doctor_result)
                if ranger_result != None and ranger_result != []:
                    ranger_list.append(ranger_result)
                if weaponsmith_result != None and weaponsmith_result != []:
                    weaponsmith_list.append(weaponsmith_result)

    architect_list = sorted(architect_list, key=lambda listing: listing[2][1], reverse=True)
    armorsmith_list = sorted(armorsmith_list, key=lambda listing: listing[2][1], reverse=True)
    artisan_list = sorted(artisan_list, key=lambda listing: listing[2][1], reverse=True)
    chef_list = sorted(chef_list, key=lambda listing: listing[2][1], reverse=True)
    combat_medic_list = sorted(combat_medic_list, key=lambda listing: listing[2][1], reverse=True)
    doctor_list = sorted(doctor_list, key=lambda listing: listing[2][1], reverse=True)
    ranger_list = sorted(ranger_list, key=lambda listing: listing[2][1], reverse=True)
    weaponsmith_list = sorted(weaponsmith_list, key=lambda listing: listing[2][1], reverse=True)

    export("Architect", architect_list, False)
    export("Armorsmith", armorsmith_list, False)
    export("Artisan", artisan_list, False)
    export("Chef", chef_list, False)
    export("Combat Medic", combat_medic_list, False)
    export("Doctor", doctor_list, True)
    export("Ranger", ranger_list)
    export("Weaponsmith", weaponsmith_list)

    missing_list = missing(resources, resources_max)
    export("Missing", missing_list)

    return None

main()
