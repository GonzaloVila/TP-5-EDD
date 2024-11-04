from superheroes_process import superHeroesProcess

def main():
    processor = superHeroesProcess("superheroes_villanos.txt")
    processor.process_file()
    
    heroes_count, villains_count = processor.get_counts()
    
    print(f"Total Superheroes: {heroes_count}")
    print(f"Total Villanos: {villains_count}")
    print("\nDetalle de personajes en la tabla hash:")

if __name__ == "__main__":
    main()