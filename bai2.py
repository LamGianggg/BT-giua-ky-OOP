from bai1 import Point

import math


class LineSegement:
    __d1 = Point()
    __d2 = Point(0)

# Phuong phap nap chong constructer method overloading
    def __init__(self, *args):
        if len(args) == 0:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)
        elif len(args) == 2:
            if not all(isinstance(arg, Point) for arg in args):
                raise TypeError("Point should be used")
            self.__d1 = args[0]
            self.__d2 = args[1]
        elif len(args) == 4:
            if not all(isinstance(item, int) for item in args):
                raise TypeError("Only integers can be added")
            self.__d1 = Point(args[0], args[1])
            self.__d2 = Point(args[2], args[3])
        elif len(args) == 1:
            if not isinstance(args[0],LineSegement):
                raise TypeError("Only a line segement can be added")
            self.__d1 = Point(args[0].__d1.getX(), args[0].__d1.getY())
            self.__d2 = Point(args[0].__d2.getX(), args[0].__d2.getY())
        else:
            raise ValueError("Invalid number of arguments")

    def angle(self):
        return math.atan2(self.__d2.getY() - self.__d1.getY(), self.__d2.getX()-self.__d1.getX())

    def read(self):
        tmp = input("Nhap vao doan thang: ")
        coords = list(map(int,tmp.split()))
        self.__d1 = Point(coords[0], coords[1])
        self.__d2 = Point(coords[2], coords[3])

    def __str__(self):
        return f"{((self.__d1.getX()),(self.__d1.getY())),((self.__d2.getX()),(self.__d2.getY()))}"

    def move(self,dx = 0,dy = 0):
        self.__d1.move(dx,dy)
        self.__d2.move(dx,dy)

    def length(self):
        return self.__d1.distance(self.__d2)

    def angle(self):
        return int(math.atan2((self.__d2.getY(),self.__d1.getY()),(self.__d2.getX(),self.__d1.getX())))

class LineSegementTest:
    def testCase1(self):
        diemA = Point(2,5)
        diemB = Point(20,35)
        doanAB = LineSegement(diemA,diemB)
        doanAB.move(35,51)
        print(doanAB)

    def testCase2(self):
        doanCD = LineSegement()
        doanCD.read()
        print("|CD| = {:.2f}".format(doanCD.length()))

    def testCase3(self):
        n = int(input("Nhap n: "))
        danhsach = []

        for i in range(n):
            l1 = LineSegement()
            l1.read()
            danhsach.append(l1)
            #hien thi cac doan thang trong danh sach
        print("Danh sach truoc khi sap xep: ")
        for item in danhsach:
            print(item)
            print(item.length())

LineSegementTest().testCase3()