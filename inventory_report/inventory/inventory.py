from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    @staticmethod
    def import_data(path: str, type: str) -> str:
        with open(path, 'r') as file:
            file_data = dict()
            if path.lower().endswith('.csv'):
                file_data = csv.DictReader(file)
            if path.lower().endswith('.json'):
                file_data = json.load(file)
            if path.lower().endswith('.xml'):
                file_data = csv.DictReader(file)
            data_list = [row for row in file_data]
            if type == "simples":
                return SimpleReport.generate(data_list)
            if type == "completo":
                return CompleteReport.generate(data_list)
