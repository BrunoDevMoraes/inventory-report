from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @staticmethod
    def import_data(path: str, type: str) -> str:
        with open(path, 'r') as csvfile:
            file_data = csv.DictReader(csvfile)
            data_list = [row for row in file_data]
            if type == "simples":
                return SimpleReport.generate(data_list)
            if type == "completo":
                return CompleteReport.generate(data_list)
