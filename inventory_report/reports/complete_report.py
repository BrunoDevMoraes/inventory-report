from simple_report import SimpleReport


class CompleteReport():
    @staticmethod
    def generate(products_list):
        companies_products = SimpleReport.get_company_with_most_products(
            products_list)[0]
        companies_report = ''
        for key in companies_products:
            companies_report += f"\n- {key}: {companies_products[key]}"
        return (
            f"{SimpleReport.generate(products_list)}\n"
            f"Produtos estocados por empresa:"
            f"{companies_report}"
        )
