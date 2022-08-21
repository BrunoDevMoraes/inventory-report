from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @staticmethod
    def read_xml_file(file):
        file_data = xmltodict.parse(file.read())
        return [row for row in file_data["dataset"]["record"]]

    @staticmethod
    def read_file(path):
        with open(path, 'r') as file:
            file_data = dict()
            if path.lower().endswith('.csv'):
                file_data = csv.DictReader(file)
                return [row for row in file_data]
            if path.lower().endswith('.json'):
                file_data = json.load(file)
                return [row for row in file_data]
            else:
                return Inventory.read_xml_file(file)

    @staticmethod
    def import_data(path: str, type: str) -> str:
        data_list = Inventory.read_file(path)
        if type == "simples":
            return SimpleReport.generate(data_list)
        if type == "completo":
            return CompleteReport.generate(data_list)
