class Rectangle(object):
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.x2 = x + w
        self.y1 = y
        self.y2 = y + h

    def is_involved(self, other):
        if all([other.x1 <= self.x1,
                other.y1 <= self.y1,
                other.x2 >= self.x2,
                other.y2 >= self.y2]):
            print("один прямоугольник включает другой")
            return "Да"
        else:
            return "Нет"


    def is_intersected(self, other):
        if any([all([other.x1 <= self.x1 <= other.x2, other.y1 <= self.y1 <= other.y2]),
                all([other.x1 <= self.x2 <= other.x2, other.y1 <= self.y1 <= other.y2]),
                all([other.x1 <= self.x1 <= other.x2, other.y1 <= self.y2 <= other.y2]),
                all([other.x1 <= self.x2 <= other.x2, other.y1 <= self.y2 <= other.y2])]):
            return "Нет"
        return "Да"

print("Введите координаты для")
print("Прямоугольника 1:")
rect1 = Rectangle(int(input("x левого нижнего угла = ")), int(input("y левого нижнего угла = ")), int(input("ширина = ")), int(input("высота = ")))
print()
print("Прямоугольника 2:")
rect2 = Rectangle(int(input("x левого нижнего угла = ")), int(input("y левого нижнего угла = ")), int(input("ширина = ")), int(input("высота = ")))

print()
print('а) Принадлежат ли все точки первого прямоугольника второму:')
print(rect2.is_involved(rect1))
print('б) Принадлежат ли все точки одного из прямоугольников другому:')
print(rect2.is_involved(rect1) or rect1.is_involved(rect2))
print('в) Пересекаются ли эти прямоугольники:')
print(rect2.is_intersected(rect1) or rect1.is_intersected(rect2))
