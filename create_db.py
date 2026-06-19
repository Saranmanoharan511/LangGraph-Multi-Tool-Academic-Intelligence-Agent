import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///oulad.db")

csv_files = {
    "assessments": "data/assessments.csv",
    "courses": "data/courses.csv",
    "studentAssessment": "data/studentAssessment.csv",
    "studentInfo": "data/studentInfo.csv",
    "studentRegistration": "data/studentRegistration.csv",
    "studentVle": "data/studentVle.csv",
    "vle": "data/vle.csv"
}

for table_name, file_path in csv_files.items():

    print(f"Loading {table_name}")

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

print("Database Created Successfully")