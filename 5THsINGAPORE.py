import streamlit as st
import pandas as pd

st.title("Singapore Resident Population Dashboard")

# --------------------------------
# Load preloaded CSV file
# --------------------------------
CSV_PATH = "Singapore_Residents.csv"

df = pd.read_csv(CSV_PATH)

# -------------------------------
# Total Population by Year
# -------------------------------
st.header("Total Population by Year")

total_population_df = (
    df.groupby('Year')['Count']
    .sum()
    .reset_index()
)
total_population_df.columns = ['Year', 'Total_Population']

st.dataframe(
    total_population_df.style.format(
        {"Total_Population": "{:,}"}
    )
)

# -------------------------------
# Female to Male Ratio
# -------------------------------
st.header("Female to Male Ratio by Ethnic Group")

years = sorted(df['Year'].unique())
groups = {
    'Total': ('Total Male Residents', 'Total Female Residents'),
    'Malays': ('Total Male Malays', 'Total Female Malays'),
    'Chinese': ('Total Male Chinese', 'Total Female Chinese'),
    'Indians': ('Total Male Indians', 'Total Female Indians'),
    'Others': (
        'Other Ethnic Groups (Males)',
        'Other Ethnic Groups (Females)'
    )
}

for y in years:
    with st.expander(f"Year {int(y)}"):
        ratio_data = []

        for g, (m, f) in groups.items():
            male_row = df[
                (df['Year'] == y) & (df['Residents'] == m)
            ]
            female_row = df[
                (df['Year'] == y) & (df['Residents'] == f)
            ]

            if not male_row.empty and not female_row.empty:
                male = male_row['Count'].values[0]
                female = female_row['Count'].values[0]
                ratio = female / male

                ratio_data.append({
                    'Group': g,
                    'Males': f"{male:,}",
                    'Females': f"{female:,}",
                    'F/M Ratio': f"{ratio:.4f}"
                })

        if ratio_data:
            st.table(pd.DataFrame(ratio_data))

# -------------------------------
# Population Growth
# -------------------------------
st.header("Total Resident Population Growth")

popu = (
    df[df['Residents'] == 'Total Residents']
    [['Year', 'Count']]
    .sort_values('Year')
    .copy()
)

popu['Growth % (YoY)'] = popu['Count'].pct_change() * 100
popu['Cumulative Growth %'] = (
    (popu['Count'] - popu['Count'].iloc[0])
    / popu['Count'].iloc[0]
) * 100

# Format for display
display_popu = popu.copy()
display_popu['Year'] = display_popu['Year'].astype(int)
display_popu['Count'] = display_popu['Count'].apply(
    lambda x: f"{int(x):,}"
)
display_popu['Growth % (YoY)'] = display_popu['Growth % (YoY)'].apply(
    lambda x: "N/A" if pd.isna(x) else f"{x:.2f}%"
)
display_popu['Cumulative Growth %'] = display_popu[
    'Cumulative Growth %'
].apply(lambda x: f"{x:.2f}%")

st.table(display_popu)
