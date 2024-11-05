from src.python_ed_fcad_uner.data_structures.maps_dicts_hash.map_base import MapBase
from sorted_table_map_abstract import SortedTableMapAbstract
from typing import Any, List, Generator

class SortedTableMap(SortedTableMapAbstract):
    def __init__(self) -> None:
        self._table: List[MapBase._Item] = []
    
    def __len__(self) -> int:
        return len(self._table)
    
    def __str__(self) -> str:
        return "{" + ", ".join(str(item) for item in self._table) + "}"
    
    def __repr__(self) -> str:
        return str(self)

    def __getitem__(self, k: Any) -> Any:
        for item in self._table:
            if item._key == k:
                return item._value
        raise KeyError(f"Key Error: {k}")

    def __setitem__(self, k: Any, v: Any) -> None:
        for item in self._table:
            if item._key == k:
                item._value = v 
                return
        new_item = self._Item(k, v)
        self._table.append(new_item)
        self._table.sort() 

    def __delitem__(self, k: Any) -> None:
        for index, item in enumerate(self._table):
            if item._key == k:
                self._table.pop(index)
                return
        raise KeyError(f"Key Error: {k}")

    def __iter__(self) -> Generator[Any, None, None]:
        for item in self._table:
            yield item._key

    def iter_items(self) -> Generator[Any, None, None]:
        for item in self._table:
            yield (item._key, item._value)