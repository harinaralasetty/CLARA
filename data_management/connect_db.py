import pandas as pd
import config

def load_and_combine() -> pd.DataFrame:
    """
    Reads the three CSVs and returns a single DataFrame where:
      - each visit is joined with its patient info
      - each visit+patient row is also joined with any chronic conditions
    """
    # Load CSV paths from config
    patients_csv = config.PATIENTS_CSV
    visits_csv = config.VISITS_CSV
    conditions_csv = config.CONDITIONS_CSV
    
    # Load each table
    patients = pd.read_csv(patients_csv)
    visits = pd.read_csv(visits_csv)
    conditions = pd.read_csv(conditions_csv)

    # Merge visits with patients
    df = visits.merge(
        patients,
        on="PatientID",
        how="left",
        suffixes=("", "_patient")
    )

    # Merge in conditions (may duplicate rows if multiple conditions)
    df = df.merge(
        conditions,
        on="PatientID",
        how="left",
        suffixes=("", "_condition")
    )

    return df


def get_patient_info(df: pd.DataFrame, patient_id: int) -> pd.DataFrame:
    """
    Filters the combined DataFrame for a specific patient_id.
    Returns all visit+condition rows for that patient.
    """
    return df[df["PatientID"] == patient_id].reset_index(drop=True)


# # === Example usage ===
# if __name__ == "__main__":
#     combined_df = load_and_combine(
#         "patients.csv",
#         "visits.csv",
#         "conditions.csv"
#     )
#     # View the full combined table
#     print(combined_df.head())

#     # Fetch info just for patient 1001
#     patient_1001 = get_patient_info(combined_df, 1001)
#     print(patient_1001)
