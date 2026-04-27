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
    # TODO: extract PMH
    return None


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