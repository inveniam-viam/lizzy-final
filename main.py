# INSY 662: Data Mining and Visualization
# Prof. Elizabeth Han
# Fall 2023

# Individual Project
# Submitted by: Jared Balakrishnan
# November 29, 2023


# Loading all the libraries
import pandas as pd
import numpy as np 
from pathlib import Path


dataset_path = Path().absolute() / "Data"

# Function to read in dataset

def read_dataset(path: Path, filename: str) -> pd.DataFrame:

    """Reading in the provided dataset as a data frame."""

    dataframe = pd.read_excel(path / filename)

    dataframe.columns = dataframe.columns.str.lower().str.replace(' ', '_')

    return dataframe

# Function to optimize the data types (computational efficiency)

def validate_dtypes(type_dict: dict, df: pd.DataFrame) -> pd.DataFrame:

    """Optimizing the data types in the dataset so as to get the lowest possible runtimes."""

    return df.astype(type_dict)

# Initializing a data type dictionary for the kickstarter dataset

kickstarter_types: dict[str, str] = {
    "id": "int64",
    "name": "string",
    "goal": "float64",
    "pledged": "float64",
    "state": "category",
    "disable_communication": "bool",
    "country": "string",
    "currency": "string",
    "deadline": "datetime64[ns]",
    "state_changed_at": "datetime64[ns]",
    "created_at": "datetime64[ns]",
    "launched_at": "datetime64[ns]",
    "staff_pick": "bool",
    "backers_count": "int64",
    "static_usd_rate": "float64",
    "usd_pledged": "float64",
    "category": "category",
    "spotlight": "bool",
    "name_len": "float64",
    "name_len_clean": "float64",
    "blurb_len": "float64",
    "blurb_len_clean": "float64",
    "deadline_weekday": "string",
    "state_changed_at_weekday": "string",
    "created_at_weekday": "string",
    "launched_at_weekday": "string",
    "deadline_month": "int64",
    "deadline_day": "int64",
    "deadline_yr": "int64",
    "deadline_hr": "int64",
    "state_changed_at_month": "int64",
    "state_changed_at_day": "int64",
    "state_changed_at_yr": "int64",
    "state_changed_at_hr": "int64",
    "created_at_month": "int64",
    "created_at_day": "int64",
    "created_at_yr": "int64",
    "created_at_hr": "int64",
    "launched_at_month": "int64",
    "launched_at_day": "int64",
    "launched_at_yr": "int64",
    "launched_at_hr": "int64",
    "create_to_launch_days": "int64",
    "launch_to_deadline_days": "int64",
    "launch_to_state_change_days": "int64"
}

# READING IN THE KICKSTARTER DATASET

kickstarter_df = read_dataset(dataset_path, "Kickstarter.xlsx")

# CLEAN UP THE DATA TYPES IN THE DATASET

kickstarter_df = validate_dtypes(kickstarter_types, kickstarter_df)

# PRE-PROCESSING THE DATASET

# Task 1 - Remove any column that is not made available at the moment of a project's launch

unavailable_at_launch: list[str] = ['id', 'pledged', 'disable_communication', 'state_changed_at', 'staff_pick',
                                     'backers_count', 'static_usd_rate', 'usd_pledged', 'spotlight', 'state_changed_at_weekday', 
                                     'state_changed_at_month', 'state_changed_at_day', 'state_changed_at_yr', 'state_changed_at_hr', 'launch_to_state_change_days']

kickstarter_df.drop(unavailable_at_launch, axis = 1, inplace = True)

# Task 2 - Only including observations that have the value of 'successful' or 'failed' for the 'state' variable

kickstarter_df = kickstarter_df[(kickstarter_df['state'] == 'successful') | (kickstarter_df['state'] == 'failed')]

kickstarter_df.reset_index(drop = True, inplace = True)

# DO MORE EXPLORATORY DATA ANALYSIS



# LOOK INTO STANDARDIZATION AND NORMALIZATION (IF NECESSARY)