import json

class TuLanh:
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], TuLanh):
            tl = args[0]
            self.__nhanhieu  = tl.__nhanhieu
            self.__maso      = tl.__maso
            self.__nuocsx    = tl.__nuocsx
            self.__tkdien    = tl.__tkdien
            self.__dungtich  = tl.__dungtich
            self.__gia       = tl.__gia
        elif len(args) == 6:
            self.__nhanhieu, self.__maso, self.__nuocsx, self.__tkdien, self.__dungtich, self.__gia = args
        else:
            self.__nhanhieu  = "Elextrolux"
            self.__maso      = "UNKNOWN"
            self.__nuocsx    = "Việt Nam"
            self.__tkdien    = True
            self.__dungtich  = 256
            self.__gia       = 7_000_000

    def makeCopy(self, tl):
        if not isinstance(tl, TuLanh):
            raise ValueError("Phải truyền TuLanh")
        self.__init__(tl)

    def nhapThongTin(self):
            self.__nhanhieu = input("Nhập nhãn hiệu: ")
            self.__maso = input("Nhập mã số: ")
            self.__nuocsx = input("Nhập nước sx: ")
            self.__tkdien = input("Nhập tk điện: ") == "True"
            self.__dungtich = int(input("Nhập dung tích: "))
            self.__gia = int(input("Nhập giá: "))

    def hienThi(self):
        print("=" * 10)
        print(f"{'Nhãn hiệu':<15}: {self.__nhanhieu}")
        print(f"{'Mã số':<15}: {self.__maso}")
        print(f"{'Nước SX':<15}: {self.__nuocsx}")
        print(f"{'T/K điện':<15}: {'Có' if self.__tkdien else 'Không'}")
        print(f"{'Dung tích':<15}: {self.__dungtich}L")
        print(f"{'Giá':<15}: {self.__gia}VNĐ")
        print("=" * 10)

    def layNhanHieu(self):
        return self.__nhanhieu

    def layGia(self):
        return self.__gia

    def soNguoiSD(self):
        return self.__dungtich // 100

    def cungNhanHieu(self, tl):
        return isinstance(tl, TuLanh) and self.__nhanhieu == tl.__nhanhieu

    def nhHon(self, tl):
        return isinstance(tl, TuLanh) and self.__dungtich < tl.__dungtich

    def to_dict(self):
        return {
            'nhanhieu': self.__nhanhieu,
            'maso': self.__maso,
            'nuocsx': self.__nuocsx,
            'tkdien': self.__tkdien,
            'dungtich': self.__dungtich,
            'gia': self.__gia
        }

class C002454:
    @staticmethod
    def testCase1():
        tl1 = TuLanh()
        tl1.nhapThongTin()

        tl2 = TuLanh("LG", "LG-28382", "Hàn Quốc", True, 600, 43000000)
        tl2.hienThi()

        tl3 = TuLanh(tl1)
        tl3.hienThi()

    @staticmethod
    def testCase2():
        n = int(input("Nhập số tủ lạnh: "))
        ds = []
        for _ in range(n):
            tl = TuLanh()
            tl.nhapThongTin()
            ds.append(tl)
        for tl in reversed(ds):
            tl.hienThi()

    @staticmethod
    def testCase3():
        n = int(input("Nhập số tủ lạnh: "))
        ds = []
        for _ in range(n):
            tl = TuLanh()
            tl.nhapThongTin()
            ds.append(tl)
        ds.sort(key=lambda x: x.layGia(), reverse=True)
        for tl in ds:
            tl.hienThi()

    @staticmethod
    def testCase4():
        n = int(input("Nhập số tủ lạnh: "))
        ds = []
        for _ in range(n):
            tl = TuLanh()
            tl.nhapThongTin()
            ds.append(tl)
        with open("DsTuLanh.json", "w", encoding='utf-8') as f:
            json.dump([tl.to_dict() for tl in ds], f, ensure_ascii=False, indent=4)
        print("Đã lưu vào DsTuLanh.json")

    @staticmethod
    def testCase5():
        n = int(input("Nhập số tủ lạnh: "))
        ds = []
        for _ in range(n):
            tl = TuLanh()
            tl.nhapThongTin()
            ds.append(tl)
        thongke = {}
        for tl in ds:
            nh = tl.layNhanHieu()
            if nh in thongke:
                thongke[nh] += 1
            else:
                thongke[nh] = 1
        for nh in sorted(thongke):
            print(f"{nh} ({thongke[nh]})")

C002454.testCase5()
