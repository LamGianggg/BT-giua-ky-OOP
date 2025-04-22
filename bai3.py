from bai1 import Point

class ColorPoint(Point):
    def __init__(self, x=0, y=1, color='xanh'):
        super().__init__(x, y)
        self.__color = color

    def read(self):
        data = input()
        parts = data.strip().split()
        self.setXY(int(parts[0]), int(parts[1]))
        self.__color = ' '.join(parts[2:])

    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

    def print(self):
        print(f"({self.getX()}, {self.getY()}): {self.__color}")

    def setXY(self, x, y):
        # Cập nhật x, y thông qua move nếu cần hoặc thiết lập trực tiếp
        self._Point__x = x
        self._Point__y = y

    def __copy__(self):
        return ColorPoint(self.getX(), self.getY(), self.__color)


class C002454:
    @staticmethod
    def testCase1():
        A = ColorPoint(5, 10, "trắng")
        A.print()
        print("Constructor: PASS")

    @staticmethod
    def testCase2():
        B = ColorPoint()
        B.read()
        B.move(10, 8)
        B.print()

    @staticmethod
    def testCase3():
        C = ColorPoint(6, 3, "đen")
        D = C.__copy__()
        D.print()
        D.setColor("vàng")
        D.print()
        C.print()
        print("Constructor: PASS")
        print("Set color: PASS")

    @staticmethod
    def main():
        C002454.testCase1()
        C002454.testCase2()
        C002454.testCase3()

C002454.main()
