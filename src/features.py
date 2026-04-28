import pandas as pd


def extract_symptoms(df_raw):
    """
    Extract Present Illness symptoms as binary features.
    """

    symptom_cols = ['Unnamed: 6'] + list(df_raw.columns[7:36])
    df_symptoms_raw = df_raw[symptom_cols].copy()

    # Remove form header rows
    df_symptoms = df_symptoms_raw.iloc[3:].reset_index(drop=True)

    symptom_rename_map = {
        'Unnamed: 8': 'Fever',
        'Unnamed: 9': 'Myalgia',
        'Unnamed: 10': 'Chills',
        'Unnamed: 11': 'Fatigue',
        'Unnamed: 12': 'Sweating',
        'Unnamed: 13': 'Anorexia',
        'Unnamed: 14': 'Sore_Throat',
        'Unnamed: 15': 'Sneezing',
        'Unnamed: 16': 'Cough',
        'Unnamed: 17': 'Dyspnea',
        'Unnamed: 18': 'Eye_Burning',
        'Unnamed: 19': 'Anosmia',
        'Unnamed: 20': 'Rhinorrhea',
        'Unnamed: 21': 'Voice_Change',
        'Unnamed: 22': 'Nasal_Congestion',
        'Unnamed: 23': 'Ageusia',
        'Unnamed: 24': 'Chest_Pain',
        'Unnamed: 25': 'Palpitations',
        'Unnamed: 26': 'Nausea',
        'Unnamed: 27': 'Vomiting',
        'Unnamed: 28': 'Abdominal_Pain',
        'Unnamed: 29': 'Diarrhea',
        'Unnamed: 32': 'Depression',
        'Unnamed: 33': 'Sleep_Disorder',
        'Unnamed: 34': 'Headache',
    }

    df_symptoms_binary = df_symptoms.notna().astype(int)
    df_symptoms_binary.rename(columns=symptom_rename_map, inplace=True)

    symptom_features = list(symptom_rename_map.values())
    df_symptoms_final = df_symptoms_binary[symptom_features].copy()

    return df_symptoms_final


def extract_pmh(df_raw):
    """
    Extract Past Medical History (PMH) features as binary variables.
    """

    # Select PMH-related columns from the raw form
    pmh_cols = list(df_raw.columns[37:67])
    df_pmh_raw = df_raw[pmh_cols].copy()

    # Remove form header rows
    df_pmh = df_pmh_raw.iloc[3:].reset_index(drop=True)

    # Convert presence-based medical conditions to binary features
    df_pmh_binary = df_pmh.notna().astype(int)

    # Rename raw unnamed columns to meaningful clinical feature names
    pmh_rename_map = {
        'Unnamed: 37': 'Cancer',
        'Unnamed: 38': 'Organ_Transplant',
        'Unnamed: 39': 'Chronic_Kidney_Disease',
        'Unnamed: 40': 'Dialysis',
        'Unnamed: 41': 'Cancer_Type',
        'Unnamed: 42': 'Solid_Organ_Transplant',
        'Unnamed: 43': 'Asthma',
        'Unnamed: 44': 'Chronic_Respiratory_Disease',
        'Unnamed: 45': 'Hypertension',
        'Unnamed: 46': 'Myocardial_Infarction',
        'Unnamed: 47': 'Valvular_Heart_Disease',
        'Unnamed: 48': 'Heart_Failure',
        'Unnamed: 49': 'Hypertriglyceridemia',
        'Unnamed: 50': 'Hypercholesterolemia',
        'Unnamed: 51': 'IBD',
        'Unnamed: 52': 'IBS',
        'Unnamed: 53': 'Chronic_Hepatitis',
        'Unnamed: 55': 'Stroke',
        'Unnamed: 56': 'Seizure',
        'Unnamed: 57': 'Diabetes_Type1',
        'Unnamed: 58': 'Diabetes_Type2',
        'Unnamed: 59': 'Hypothyroidism',
        'Unnamed: 60': 'Hyperthyroidism',
        'Unnamed: 61': 'Insulin_Use',
        'Unnamed: 62': 'Rheumatoid_Arthritis',
        'Unnamed: 63': 'Lupus',
        'Unnamed: 64': 'Behcet',
        'Unnamed: 65': 'Sjogren',
    }

    df_pmh_binary.rename(columns=pmh_rename_map, inplace=True)

    # Keep only validated PMH features
    pmh_features = list(pmh_rename_map.values())
    df_pmh_final = df_pmh_binary[pmh_features].copy()

    return df_pmh_final


def extract_covid_history(df_raw):
    # TODO: extract COVID history
    return None


def extract_vaccination(df_raw):
    # TODO: extract vaccination
    return None


def build_features(df_raw):
    df_symptoms = extract_symptoms(df_raw)
    df_pmh = extract_pmh(df_raw)
    df_covid = extract_covid_history(df_raw)
    df_vax = extract_vaccination(df_raw)

    return None