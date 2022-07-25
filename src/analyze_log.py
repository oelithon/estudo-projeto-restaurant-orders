import csv
from src import manage_search


def analyze_log(path_to_file):
    csv_file = path_to_file.split(".")

    if csv_file[1] != 'csv':
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file) as file:
            file_reader = csv.reader(file, delimiter=",", quotechar='"')
            orders_list = [order for order in file_reader]

            maria = manage_search.most_requested_meal_by_maria(orders_list)
            arnaldo = manage_search.arnaldo_burgers(orders_list)
            joao_never_requested = manage_search.joao_no_orders(orders_list)
            joao_never_visit = manage_search.joao_no_visit(orders_list)

        result = [
            f"{maria}\n",
            f"{arnaldo}\n",
            f"{joao_never_requested}\n",
            f"{joao_never_visit}",
        ]

        with open('data/mkt_campaign.txt', 'w') as file:
            file.writelines(result)
            file.close()

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
