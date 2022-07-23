import csv


def most_requested_meal_by_maria(orders_list):
    maria_orders = dict()

    for name, order in orders_list:
        if name == 'maria':
            if order not in maria_orders:
                maria_orders[order] = 1
            else:
                maria_orders[order] += 1

    favorite_plate = max(maria_orders, key=maria_orders.get)

    return favorite_plate


def analyze_log(path_to_file):
    csv_file = path_to_file.split(".")

    if csv_file[1] != 'csv':
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    
    raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")