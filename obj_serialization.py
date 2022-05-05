import pickle
import shelve

class test(object):
    def __init__(self, data):
        self.data = data
        print(self, "Object created")

    def set_date(self, data):
        self.data = data
        return data

    def get_data(self):
        return self.data
    
    def __del__(self):
        print(self, "Object deleted")

a = test(15)
a.set_date(20)
print(a.get_data())

with open("pickle_test.pickle", "wb") as f:
    pickle.dump(a, f, pickle.HIGHEST_PROTOCOL)
with shelve.open("shelf_test.shelf", "c") as shelf:
    shelf["a"] = a
del a

b = pickle.load(open("pickle_test.pickle", "rb", pickle.HIGHEST_PROTOCOL))
print(b.get_data())

with shelve.open("shelf_test.shelf", "r") as shelf:
    for key in shelf.keys():
        print(repr(key), repr(shelf[key]))
    c = shelf["a"]
print(c.get_data())