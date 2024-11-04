import re
from src.python_ed_fcad_uner.data_structures.maps_dicts_hash.probe_hashmap  import ProbeHashMap

class superHeroesProcess:
    def __init__(self, filename):
        self.filename = filename
        self.heroes_count = 0
        self.villains_count = 0
        self.hash_map = ProbeHashMap()

    def process_file(self):
        pattern = r"(\w+)\((\w+)\)"
        
        with open(self.filename, 'r') as file:
            
            for line in file:
                match = re.match(pattern, line.strip())
                
                if match:
                    entity_type, name = match.groups()
                    self.add_to_map(entity_type, name)

    def add_to_map(self, entity_type, name):
        
        if entity_type == "super_heroe":
            self.heroes_count += 1
            self.hash_map[name] = "Hero"
            
        elif entity_type == "villano":
            self.villains_count += 1
            self.hash_map[name] = "Villain"

    def get_counts(self):
        return self.heroes_count, self.villains_count