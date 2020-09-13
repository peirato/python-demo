class MyArray:

    def __init__(self, capacity: int):
        self._data = []
        self._capacity = capacity

    def insert(self, index, value):
        if len(self) >= self._capacity
        pass


def test_array():
    array = MyArray(5)
    array.insert(0, 3)
    array.insert(0, 4)
    array.insert(1, 5)
    array.insert(3, 9)
    array.insert(3, 10)
    assert array.insert(0, 100) is False
    assert len(array) == 5
    assert array.find(1) == 5
    assert array.delete(4) is True
    array.print_all()


if __name__ == "__main__":
    test_array()
