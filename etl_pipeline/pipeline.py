"""
pipeline.py

Main controller for IntelliBiz ETL Pipeline.

Current Workflow:
    Extract Data
        ↓
    Validate Data
        ↓
    Generate Data Quality Report

Future Workflow:
    Extract → Validate → Transform → Load
"""


# Import ETL modules
from extract import extract_data
from validate import validate_data
from transform import transform_data
from load import load_data



def run_pipeline():
    """
    Execute the complete ETL pipeline.
    """

    print("\n===================================")
    print("   IntelliBiz ETL Pipeline Started")
    print("===================================\n")


    # Step 1: Extract raw datasets
    dataframes = extract_data()


    # Step 2: Validate extracted data
    quality_report = validate_data(dataframes)

    # test data
    # Temporary company for testing
    company_id = 1 # need removal


# step 3 Transform the extracted data
    transformed_data = transform_data(
    dataframes,
    company_id
)
    # Step 4: Load transformed data into MySQL
    load_data(transformed_data)

    print("\n===================================")
    print(" ETL Pipeline Completed Successfully")
    print("===================================\n")


    return dataframes, quality_report, transformed_data

# Run pipeline when this file is executed directly
if __name__ == "__main__":

    datasets, report, transformed  = run_pipeline()





