# when we create a class it means that we are creating our own datatype.
class Cookie:
    def __init__(self, color):  # color is something which is passed to that instant it is applied
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


cookie_one = Cookie("green")
cookie_two = Cookie('blue')

print("Cookie 1 color is", cookie_one.get_color())
print("cookie 2 color is", cookie_two.get_color())

cookie_one.set_color('pink')

print('Cookie 1 color is', cookie_one.get_color())
print('cookie 2 color is', cookie_two.get_color())
