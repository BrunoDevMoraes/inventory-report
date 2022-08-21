import datetime


class SimpleReport:
    @staticmethod
    def get_company_with_most_products(products_list):
        products_per_company = dict()
        for product in products_list:
            if product["nome_da_empresa"] in products_per_company.keys():
                products_per_company[product["nome_da_empresa"]] += 1
            else:
                products_per_company[product["nome_da_empresa"]] = 1

        company_with_most_products = str()
        highest_amount = 0
        for key in products_per_company:
            if products_per_company[key] > highest_amount:
                highest_amount = products_per_company[key]
                company_with_most_products = key

        return [products_per_company, company_with_most_products]

    @staticmethod
    def get_oldest_date(products_list):
        oldest_date = datetime.datetime.strptime(
            products_list[0]["data_de_fabricacao"], "%Y-%m-%d"
        ).date()
        for product in products_list:
            date = datetime.datetime.strptime(
                product["data_de_fabricacao"], "%Y-%m-%d"
            ).date()
            if date < oldest_date:
                oldest_date = date

        return oldest_date

    @staticmethod
    def get_closest_future_date(products_list):
        current_date = datetime.datetime.now().date()
        future_dates = []
        for product in products_list:
            date = datetime.datetime.strptime(
                product["data_de_validade"], "%Y-%m-%d"
            ).date()
            if date > current_date:
                future_dates.append(date)

        return min(future_dates, default=0)

    @staticmethod
    def generate(products_list):
        oldest_date = SimpleReport.get_oldest_date(products_list)
        closest_date = SimpleReport.get_closest_future_date(products_list)
        company = SimpleReport.get_company_with_most_products(products_list)[1]
        return (
            "Data de fabricação mais antiga: {}\n"
            "Data de validade mais próxima: {}\n"
            "Empresa com mais produtos: {}"
            .format(oldest_date, closest_date, company)
        )
