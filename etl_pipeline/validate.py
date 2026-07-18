"""
validate.py

Purpose:
    Performs data quality assessment on extracted datasets.

Current Validations:
    1. Missing value detection
    2. Duplicate row detection
    3. Dataset quality report generation

Future Enhancements:
    - Data type validation
    - Foreign key integrity checks
    - Business rule validation
    - Data quality scoring
"""


def check_missing_values(df):
    """
    Check the number of missing values in each column.

    Parameters:
        df (DataFrame): Input dataset

    Returns:
        dict: Column-wise missing value counts
    """

    missing_values = df.isnull().sum()

    return missing_values.to_dict()


def check_duplicates(df):
    """
    Check for duplicate rows in a dataset.

    Parameters:
        df (DataFrame): Input dataset

    Returns:
        int: Number of duplicate rows
    """

    duplicate_count = df.duplicated().sum()

    return int(duplicate_count)


def validate_data(dataframes):
    """
    Validate all extracted datasets.

    Parameters:
        dataframes (dict):
            Dictionary containing all datasets.

    Returns:
        dict:
            Complete data quality report.
    """

    print("\n=================================")
    print(" Starting Data Quality Validation")
    print("=================================\n")

    quality_report = {}

    # Validate each dataset one by one
    for dataset_name, df in dataframes.items():

        print(f"Validating dataset: {dataset_name}")

        missing_report = check_missing_values(df)

        duplicate_report = check_duplicates(df)

        quality_report[dataset_name] = {
            "total_rows": len(df),
            "total_columns": len(df.columns),
            "missing_values": missing_report,
            "duplicate_rows": duplicate_report
        }

        print(f"Completed validation: {dataset_name}")
        print("-" * 40)

    print("\n=================================")
    print(" Data Quality Validation Finished")
    print("=================================\n")

    return quality_report