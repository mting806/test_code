from schema import Schema
print("test")

Schema(lambda x: x>5).validate(4)