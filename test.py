
from data_management.connect_db import load_and_combine
from data_management.patient_data import get_patient_conditions

df = load_and_combine()

print(get_patient_conditions(df, 1001))