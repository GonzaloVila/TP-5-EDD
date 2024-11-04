from sorted_table_map import SortedTableMap
from sorted_table_map_abstract import SortedTableMapAbstract
from src.python_ed_fcad_uner.data_structures.maps_dicts_hash.map_base import MapBase

def test_sorted_table_map():
    # Crear una instancia de SortedTableMap
    map_instance = SortedTableMap()
    
    assert len(map_instance) == 0, "Error: El mapa debe estar vacio al inicio."
    
    map_instance['a'] = 1
    map_instance['c'] = 3
    map_instance['b'] = 2
    map_instance['d'] = 4
    
    assert len(map_instance) == 4, "Error: La longitud debe ser 4 después de insertar 4 elementos."
    
    assert map_instance['a'] == 1, "Error: Valor incorrecto para la clave 'a'."
    assert map_instance['b'] == 2, "Error: Valor incorrecto para la clave 'b'."
    assert map_instance['c'] == 3, "Error: Valor incorrecto para la clave 'c'."
    assert map_instance['d'] == 4, "Error: Valor incorrecto para la clave 'd'."
    

    map_instance['a'] = 10
    assert map_instance['a'] == 10, "Error: Valor incorrecto después de actualizar la clave 'a'."
    
    del map_instance['b']
    assert len(map_instance) == 3, "Error: La longitud debe ser 3 después de eliminar 1 elemento."
    try:
        map_instance['b']
        assert False, "Error: La clave 'b' debería haber sido eliminada."
    except KeyError:
        pass  
    
    keys = list(iter(map_instance))
    assert keys == ['a', 'c', 'd'], f"Error: Las claves no están en orden. Resultado: {keys}"
    
    items = list(map_instance.iter_items())
    expected_items = [('a', 10), ('c', 3), ('d', 4)]
    assert items == expected_items, f"Error: Los pares clave-valor no coinciden. Resultado: {items}"
    
    assert str(map_instance) == "{(a, 10), (c, 3), (d, 4)}", "Error en la representación en cadena del mapa."
    assert repr(map_instance) == "{(a, 10), (c, 3), (d, 4)}", "Error en la representación del mapa."

    print("Todas las pruebas pasaron exitosamente.")

test_sorted_table_map()