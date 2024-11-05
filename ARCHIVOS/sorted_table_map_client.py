from sorted_table_map import SortedTableMap
from src.python_ed_fcad_uner.data_structures.maps_dicts_hash.map_base import MapBase

def test_sorted_table_map():
    map_instance = SortedTableMap()
    
    assert len(map_instance) == 0, "Error: El mapa deberaa estar vacio al prinicipio"
    print(f"El mapa está vacio al principio. Tamaño: {len(map_instance)}")
    
    map_instance['a'] = 1
    map_instance['c'] = 3
    map_instance['b'] = 2
    map_instance['d'] = 4
    print("Elementos agregados: {'a': 1, 'c': 3, 'b': 2, 'd': 4}")
    
    assert len(map_instance) == 4, "Error: El tamaño debe ser 4 luego de insertar 4 elementos"
    print(f"Tamaño luego de insertar elementos: {len(map_instance)}")
    
    assert map_instance['a'] == 1, "Error: Valor incorrecto para la clave 'a'"
    assert map_instance['b'] == 2, "Error: Valor incorrecto para la clave 'b'"
    assert map_instance['c'] == 3, "Error: Valor incorrecto para la clave 'c'"
    assert map_instance['d'] == 4, "Error: Valor incorrecto para la clave 'd'"
    

    map_instance['a'] = 10
    assert map_instance['a'] == 10, "Error: El valor es incorrecto después de actualizar la clave 'a'"
    print("Valor actualizado 'a': 10")
    
    del map_instance['b']
    assert len(map_instance) == 3, "Error: El tamaño debe ser 3 luego de eliminar 1 elemento"
    print(f"El tamaño luego de la eliminaciin del elemento 'b'. Tamaño: {len(map_instance)}")

    try:
        map_instance['b']
        assert False, "Error: La clave 'b' fue eliminada"
    except KeyError:
        pass  
    
    keys = list(iter(map_instance))
    assert keys == ['a', 'c', 'd'], f"Error: Las claves no están ordenadas. Resultado: {keys}"
    print(f"Claves ordenadas correctamente: {keys}")
    
    items = list(map_instance.iter_items())
    expected_items = [('a', 10), ('c', 3), ('d', 4)]
    assert items == expected_items, f"Error: Los pares de clave-valor no son correctos. Resultado: {items}"
    
    assert str(map_instance) == "{(a, 10), (c, 3), (d, 4)}", "Error en la representación en cadena del mapa"
    assert repr(map_instance) == "{(a, 10), (c, 3), (d, 4)}", "Error en la representación del mapa"
    print("Representación en cadena correcta:", str(map_instance))

if __name__ == "__main__":
    test_sorted_table_map()