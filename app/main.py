from typing import Any, Hashable


class Dictionary:

    def __init__(self) -> None:
        self.hash_table = [[] for _ in range(8)]
        self.size = 0
        self.load_threshold = len(self.hash_table) * 2 / 3

    def _resize(self) -> None:
        our_hash_table = self.hash_table[:]
        new_hash_table = [[] for _ in range(len(our_hash_table) * 2)]
        self.load_threshold = len(new_hash_table) * 2 / 3
        for box in our_hash_table:
            for data in box:
                new_index_hash_table = hash(data[0]) % len(new_hash_table)
                new_hash_table[new_index_hash_table].append(data)
        self.hash_table = new_hash_table

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.size >= self.load_threshold:
            self._resize()

        index_hash_table = hash(key) % len(self.hash_table)
        if self.hash_table[index_hash_table]:
            for index, data in enumerate(self.hash_table[index_hash_table]):
                if data[0] == key:
                    self.hash_table[index_hash_table][index] = (
                        key, hash(key), value
                    )
                    break
            else:
                self.hash_table[index_hash_table].append(
                    (key, hash(key), value)
                )
                self.size += 1
        else:
            self.hash_table[index_hash_table].append((key, hash(key), value))
            self.size += 1

    def __getitem__(self, key: Hashable) -> Any:
        index_hash_table = hash(key) % len(self.hash_table)
        for data in self.hash_table[index_hash_table]:
            if data[0] == key:
                return data[2]
        else:
            raise KeyError(key)

    def __len__(self) -> int:
        return self.size
