def most_requested_meal_by_maria(orders_list):
    maria_orders = dict()

    for name, order, day in orders_list:
        if name == 'maria':
            if order not in maria_orders:
                maria_orders[order] = 1
            else:
                maria_orders[order] += 1

    favorite_plate = max(maria_orders, key=maria_orders.get)

    return favorite_plate


def arnaldo_burgers(orders_list):
    burgers_quantity = 0

    for name, order, day in orders_list:
        if name == 'arnaldo' and order == 'hamburguer':
            burgers_quantity += 1

    return burgers_quantity


def joao_no_orders(orders_list):
    full_menu = set()
    joao_orders = set()

    for name, order, day in orders_list:
        full_menu.add(order)

        if name == 'joao':
            joao_orders.add(order)

    return full_menu - joao_orders


def joao_no_visit(orders_list):
    days = set()
    joao_visit_days = set()

    for name, order, day in orders_list:
        days.add(day)

        if name == 'joao':
            joao_visit_days.add(day)

    return days - joao_visit_days
