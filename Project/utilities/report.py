import os
from datetime import datetime
from time import sleep
from utilities.config_reader import ConfigReader

class AllureReporter:
    config=ConfigReader()
    base_dir = config.get_value("PATH","base_dir")
    result_dir = config.get_value("PATH","result_directory")
    report_dir = config.get_value("PATH","report_directory")

    def __init__(self):
        """
        Method name: __init__
        Author name: Grace
        Short description of method:
            Initializes Allure report directories if they do not exist.
        Return type: None
        Parameter list: None
        """
        try:
            sleep(2)
            os.makedirs(self.result_dir, exist_ok=True)
            os.makedirs(self.report_dir, exist_ok=True)
        except Exception as e:
            raise Exception(f"Failed to initialize Allure directories: {e}")

    def generate_report(self):
        """
        Method name: generate_report
        Author name: Grace
        Short description of method:
            Generates Allure HTML report inside a
            timestamped report directory.
        Return type: None
        Parameter list: None
        """
        try:
            sleep(2)
            time = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
            path = os.path.join(self.report_dir,f"AllureReports_{time}")

            allure_command = (f"allure generate {self.result_dir} -o {path}")
            os.system(allure_command)

        except Exception as e:
            raise Exception(f"Failed to generate Allure report: {e}")