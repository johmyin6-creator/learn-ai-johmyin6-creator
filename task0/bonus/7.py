class good:
    def __init__(self, product_id, name, price, total_count, remain_count):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__total_count = total_count
        self.__remain_count = remain_count
    def display(self):
        print(f"商品编号：{self.__product_id}")
        print(f"商品名称：{self.__name}")
        print(f"商品价格：{self.__price}")
        print(f"商品总数：{self.__total_count}")
        print(f"商品剩余数量：{self.__remain_count}")
    def income(self):
        return self.__price * (self.__total_count - self.__remain_count)
    def setdata(self, product_id, name, price, total_count, remain_count):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__total_count = total_count
        self.__remain_count = remain_count