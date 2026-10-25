import configparser


class ConfigReader:
    def __init__(self, config_file_path="/home/coder/project/workspace/Project/config/config.properties"):
        """
        Method Name: __init__
        Author Name: Prardhana
        Short Description of Method:
            Initializes the ConfigParser object and reads the configuration file.
        Return Type: None
        Parameter List:
            config_file_path (str): Path to the configuration file
        """
        self.config = configparser.ConfigParser()

        try:
            self.config.read(config_file_path)
        except Exception as error:
            raise Exception(f"Error while reading config file: {error}")

    def get_value(self, section_name, key_name):
        """
        Method Name: get_value
        Author Name: Prardhana
        Short Description of Method:
            Retrieves value from the given section and key in config file.
        Return Type: str
        Parameter List:
            section_name (str): Section name in config file
            key_name (str): Key name under the section
        """
        try:
            return self.config.get(section_name, key_name)

        except configparser.NoSectionError:
            raise Exception(f"Section '{section_name}' not found in config file")

        except configparser.NoOptionError:
            raise Exception(f"Key '{key_name}' not found in section '{section_name}'")

        except Exception as error:
            raise Exception(f"Unexpected error occurred: {error}")