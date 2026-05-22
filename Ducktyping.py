#Duck-typing
'''class Bird:
    def fly(self):
        print("Bird is flying")
class Airplane:
    def fly(self):
        print("Airplane is flying")
def make_it_fly(obj):
    obj.fly()
make_it_fly(Bird())
make_it_fly(Airplane())'''

class Androidphone:
    def charge(self):
        print("Android phone is charging")
class Iphone:
    def charge(self):
        print("Iphone is charging")
class Powerbank:
    def charge(self):
        print("Powerbank is charging")
def start_charging(device):
    device.charge()
start_charging(Androidphone())
start_charging(Iphone())
start_charging(Powerbank())
