from dataclasses import dataclass
from dataclasses import field


@dataclass(order=True)
class TestData:
    size: int
    name: str
    sort_index: str = field(init=False, repr=False)
    
    def __post_init__(self):
        self.sort_index = self.name

a = TestData(size=10, name="test1")
b = TestData(size=20, name="test2")
c = TestData(size=30, name="test3")

d = [a, b, c]
d.sort(key=lambda x: x.sort_index, reverse=True)
print(d)
