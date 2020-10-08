class Gizmo:
    def __init__(self):
        print('Gizmo is: %d' %id(self))

x = Gizmo()
def ct(name):
    print(name)

cx = ct
print(id(cx), id(ct))
print(cx is ct, cx == ct)
print(dir(Gizmo))