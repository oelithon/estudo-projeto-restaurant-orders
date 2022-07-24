class TrackOrders:
    def __init__(self):
        self.__orders_list = list()
        
    def __len__(self):
        return len(self.__orders_list)

    def add_new_order(self, customer, order, day):
        self.__orders_list.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        orders_count = dict()

        for name, order, _day in self.__orders_list:
            if name == customer:
                if order not in orders_count:
                    orders_count[order] = 1
                else:
                    orders_count[order] += 1

        return max(orders_count, key=orders_count.get)

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
