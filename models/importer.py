# While working with Python
# It is important to design a code flow.
# This class acts as the main function provider for all the classes.
# if the code is written everywhere,
# and functions call each other everywhere.
# It created a loop lock which gets the program to stuck.


import os, pandas as pd
import logging.config
from datetime import date
ROOT_DIR = os.path.abspath(os.getcwd())

def get_logger_obj() -> object:
    """
    Reads logging-ini cofiguration and return logger object.
    """
    logging.config.fileConfig(f"{ROOT_DIR}\\configs\\logging.ini")
    logger = logging.getLogger(__name__)
    return logger

logger = get_logger_obj()

def get_date():
    date_today = date.today()
    return str(date_today)



def get_data_from_csv():
    """
    This function uses pandas to read csv file which converts the data into dataframe
    
    """
    try:
        with open(f"{ROOT_DIR}\\data_source\\student.csv") as data_file:
            data = pd.read_csv(data_file)
            return data
    except Exception as get_data_Exc:
        logger.error(f"Exception in models/importer/get_data_from_csv: {get_data_Exc}")



