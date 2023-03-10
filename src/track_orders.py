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

                orders_count[order] += 1

        return max(orders_count, key=orders_count.get)

    def get_never_ordered_per_customer(self, customer):
        menu = set()
        orders = set()

        for name, order, _day in self.__orders_list:
            if name == customer:
                orders.add(order)
            menu.add(order)

        return menu - orders

    def get_days_never_visited_per_customer(self, customer):
        days = set()
        client_visit_days = set()

        for name, _order, day in self.__orders_list:
            if name == customer:
                client_visit_days.add(day)
            days.add(day)

        return days - client_visit_days

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
