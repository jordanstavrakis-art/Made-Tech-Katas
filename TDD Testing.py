import unittest
from Classes import DND_Class, barbarian

list_of_classes = ["Artificer", "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
list_of_hit_dice = ["d6", "d8", "d10", "d12"]
list_of_abilities = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
list_of_skills = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"]
list_of_tools = ["Alchemist's Supplies", "Brewer's Supplies", "Calligrapher's Supplies", "Carpenter's Tools", "Cartographer's Tools", "Cobbler's Tools", "Cook's Utensils", "Glassblower's Tools", "Jeweler's Tools", "Leatherworker's Tools", "Mason's Tools", "Painter's Supplies", "Potter's Tools", "Smith's Tools", "Tinker's Tools", "Weaver's Tools", "Woodcarver's Tools"]
list_of_simple_weapons = ["Simple Weapons", "Club", "Dagger", "Greatclub", "Handaxe", "Javelin", "Light Hammer", "Mace", "Quarterstaff", "Sickle", "Spear", "Crossbow, Light", "Dart", "Shortbow", "Sling"]
list_of_martial_weapons = ["Martial Weapons", "Battleaxe", "Flail", "Glaive", "Greataxe", "Greatsword", "Halberd", "Lance", "Longsword", "Maul", "Morningstar", "Pike", "Rapier", "Scimitar", "Shortsword", "Trident", "War Pick", "Warhammer", "Whip"]
list_of_armor_types = ["Light Armor", "Medium Armor", "Heavy Armor", "Shields"]


class Testing(unittest.TestCase):
    def setUp(self):
        self.barbarian = barbarian

    def test_class_name(self):
        self.assertIn(self.barbarian.name, list_of_classes)

    def test_hit_die(self):
        self.assertIn(self.barbarian.hit_die, list_of_hit_dice)

    def test_primary_ability(self):
        self.assertIn(self.barbarian.primary_ability, list_of_abilities)

    def test_secondary_ability(self):
        self.assertIn(self.barbarian.secondary_ability, list_of_abilities)
    
    def test_saving_throws(self):
        self.assertEqual(len(self.barbarian.saving_throws), 2)
        for saving_throw in self.barbarian.saving_throws:
            self.assertIn(saving_throw, list_of_abilities)
    
    def test_proficiencies(self):
        self.assertGreater(len(self.barbarian.proficiencies), 0)
        for proficiency in self.barbarian.proficiencies:
            self.assertIn(proficiency, list_of_simple_weapons + list_of_martial_weapons + list_of_armor_types + list_of_tools + list_of_skills)

if __name__ == '__main__':
    unittest.main()