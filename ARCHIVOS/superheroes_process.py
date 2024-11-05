import re
from src.python_ed_fcad_uner.data_structures.maps_dicts_hash.probe_hashmap  import ProbeHashMap

class superHeroesProcess:
    def __init__(self, filename):
        self.filename = filename
        self.heroes_count = 0
        self.villanos_count = 0
        self.hash_map = ProbeHashMap()

    def process_file(self):
        regex = r"(\w+)\((\w+)\)"
        with open(self.filename, 'r') as archivo:
            for linea in archivo:
                match = re.match(regex, linea.strip())
                if match:
                    tipo, name = match.groups()
                    self.add_to_map(tipo, name)

    def add_to_map(self, tipo, name):
        
        if tipo == "super_heroe":
            self.heroes_count += 1
            self.hash_map[name] = "Heroe"
            
        elif tipo == "villano":
            self.villanos_count += 1
            self.hash_map[name] = "Villano"

    def get_counts(self):
        return self.heroes_count, self.villanos_count