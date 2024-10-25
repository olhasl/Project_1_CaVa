import yaml
import pandas as pd
from utils.openspace import Openspace
from utils.file_utils import load_data

with open("config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

input_file_path = config['paths']['input_file']
output_file_path = config['paths']['output_file']
number_of_tables = config['settings']['number_of_tables']
space = Openspace(number_of_tables)
remaining_people = space.organize(load_data(input_file_path))
space.display()
space.store(output_file_path) 