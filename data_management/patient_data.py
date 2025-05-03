import pandas as pd 

def get_patient_conditions(df: pd.DataFrame, patient_id: int) -> pd.DataFrame:
    """
    Filters the combined DataFrame for a specific patient_id.
    Returns all chronic conditions for that patient.
    """
    patient_id = int(patient_id)  
    conditions = df[df["PatientID"] == patient_id]["ConditionName"].dropna().unique()
    return conditions
    