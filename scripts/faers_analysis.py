import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

drug_df = pd.read_csv(r'c:\Users\richa\Desktop\Projects\FAERS Project\Data\DRUG25Q4.txt', delimiter = '$', encoding = 'latin-1')
reac_df = pd.read_csv(r'c:\Users\richa\Desktop\Projects\FAERS Project\Data\REAC25Q4.txt', delimiter = '$', encoding = 'latin-1')
demo_df = pd.read_csv(r'c:\Users\richa\Desktop\Projects\FAERS Project\Data\DEMO25Q4.txt', delimiter = '$', encoding = 'latin-1')
outc_df = pd.read_csv(r'c:\Users\richa\Desktop\Projects\FAERS Project\Data\OUTC25Q4.txt', delimiter = '$', encoding = 'latin-1')
indi_df = pd.read_csv(r'c:\Users\richa\Desktop\Projects\FAERS Project\Data\INDI25Q4.txt', delimiter = '$', encoding = 'latin-1')

drug_df.columns = drug_df.columns.str.strip().str.lower()
reac_df.columns = reac_df.columns.str.strip().str.lower()
outc_df.columns = outc_df.columns.str.strip().str.lower()
indi_df.columns = indi_df.columns.str.strip().str.lower()
demo_df.columns = demo_df.columns.str.strip().str.lower()

# merge drug_df with reac_df
df_merged = drug_df.merge(reac_df, on='primaryid', how='left')

# add outc_df
df_merged = df_merged.merge(outc_df, on='primaryid', how='left')

# add indi_df/indi_clean. needs both primaryid and drug_seq to match correctly. Only bringing in columns that are actually needed from indi_df
df_merged = df_merged.merge(indi_df[['primaryid', 'indi_drug_seq', 'indi_pt']],
                                left_on=['primaryid', 'drug_seq'],
                                right_on=['primaryid', 'indi_drug_seq'],
                                how='left')

# add demo_df
df_merged = df_merged.merge(demo_df[['primaryid', 'age', 'age_grp', 'sex', 'reporter_country', 'occr_country']],
                                on='primaryid',
                                how='left')

# Filter to primary suspect drugs only
df_primary = df_merged[df_merged['role_cod'] == 'PS']
print("Primary suspect drugs only:", df_primary.shape)

# Filter out off label use
df_primary = df_primary[df_primary['pt'] != 'Off label use']

# readable codes
outcome_code = {
    'DE': 'Death',
    'LT': 'Life Threatening',
    'HO': 'Hospitalization',
    'DS': 'Disability',
    'CA': 'Congenital Anomaly',
    'RI': 'Required Intervention',
    'OT': 'Other Serious Outcome'
}

# Apply mapping
df_primary['outcome_code'] = df_primary['outc_cod'].map(outcome_code)

# outcome analyses

# which drugs have the most death reports
drug_death = df_primary[df_primary['outc_cod'] == 'DE']['drugname'].value_counts().head(10)
print(f"Top 10 drugs associated with death: {drug_death}")

# which drugs have the most hospitalization reports
drug_hosp = df_primary[df_primary['outc_cod'] == 'HO']['drugname'].value_counts().head(10)
print(f"Top 10 drugs associated with hospitalization: {drug_hosp}")


# which drugs have the most life threatening reports
drug_lt = df_primary[df_primary['outc_cod'] == 'LT']['drugname'].value_counts().head(10)
print(f"Top 10 drugs associated with life threatening outcomes: {drug_lt}")

# reactions most common with death
reaction_death = df_primary[df_primary['outc_cod'] == 'DE']['pt'].value_counts().head()
print(f"Top 10 reactions associated with death: {reaction_death}")

# since death is an outcome, remove death and count top 10 aside from death
df_temp = df_primary[df_primary['pt'] != 'Death']
reaction_death = df_temp[df_temp['outc_cod'] == 'DE']['pt'].value_counts().head()
print(f"Top 10 reactions associated with death: {reaction_death}")

reaction_hosp = df_primary[df_primary['outc_cod'] == 'HO']['pt'].value_counts().head()
print(f"Top 10 reactions associated with hospitalization: {reaction_hosp}")

# outcome by gender
outcome_gender = df_primary.groupby(['sex', 'outcome_code']).size().reset_index(name='count')
outcome_gender_sorted = outcome_gender.sort_values(by=['sex', 'count'], ascending=[True,False], inplace=True)
print(outcome_gender)

# map age group codes
age_codes = {
    'N': 'Neonate',
    'I': 'Infant',
    'C': 'Child',
    'A': 'Adult',
    'E': 'Elderly',
    'U': 'Unknown'
}

df_primary['age_code'] = df_primary['age_grp'].map(age_codes)

# outcome by age group
outcome_age = df_primary.groupby(['age_code']).size().reset_index(name='count')
print(outcome_age)

# Categorize into serious vs other (non serious)
outcome_serious = ['DE', 'LT', 'HO', 'DS', 'CA', 'RI']

# count
df_primary['is_serious'] = df_primary['outc_cod'].isin(outcome_serious)
print(df_primary['is_serious'].value_counts())

# percentage
serious_pct = df_primary['is_serious'].mean() * 100
print(f"Percentage of serious outcomes: {serious_pct.round(2)}%")

# bar chart
outcome_counts = df_primary['outcome_code'].value_counts()

plt.figure(figsize = (12, 6))
sns.barplot(x = outcome_counts.index, y=outcome_counts.values)
plt.title('Distribution of Adverse Event Outcomes')
plt.xlabel('Outcome')
plt.ylabel('Number of Reports')
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()

# pie chart
plt.figure(figsize=(10, 8))
plt.pie(outcome_counts.values,
            labels = outcome_counts.index,
            autopct = '%1.1f%%')
plt.title('Distribution of Adverse Event Outcomes')
plt.show()