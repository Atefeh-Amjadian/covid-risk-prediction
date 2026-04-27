import pandas as pd


def extract_symptoms(df_raw):
    # TODO: extract symptoms
    return None


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