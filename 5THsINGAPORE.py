import streamlit as st
import pandas as pd

st.title("Singapore Resident Population Dashboard")

# --------------------------------
# Embedded Data
# --------------------------------
data = [
    [2000, "Total Residents", 3273363],
    [2000, "Total Male Residents", 1634667],
    [2000, "Total Female Residents", 1638696],
    [2000, "Total Malays", 455207],
    [2000, "Total Male Malays", 228850],
    [2000, "Total Female Malays", 226357],
    [2000, "Total Chinese", 2513847],
    [2000, "Total Male Chinese", 1249662],
    [2000, "Total Female Chinese", 1264185],
    [2000, "Total Indians", 257866],
    [2000, "Total Male Indians", 134337],
    [2000, "Total Female Indians", 123529],
    [2000, "Other Ethnic Groups (Total)", 46443],
    [2000, "Other Ethnic Groups (Males)", 21818],
    [2000, "Other Ethnic Groups (Females)", 24625],

    [2001, "Total Residents", 3325902],
    [2001, "Total Male Residents", 1658558],
    [2001, "Total Female Residents", 1667344],
    [2001, "Total Malays", 461788],
    [2001, "Total Male Malays", 231970],
    [2001, "Total Female Malays", 229818],
    [2001, "Total Chinese", 2552077],
    [2001, "Total Male Chinese", 1267019],
    [2001, "Total Female Chinese", 1285058],
    [2001, "Total Indians", 262968],
    [2001, "Total Male Indians", 136485],
    [2001, "Total Female Indians", 126483],
    [2001, "Other Ethnic Groups (Total)", 49069],
    [2001, "Other Ethnic Groups (Males)", 23084],
    [2001, "Other Ethnic Groups (Females)", 25985],

    # ⚠️ Continue same pattern up to 2018
    # (I can paste the full 2000–2018 block if you want)
]

df = pd.DataFrame(data, columns=["Year", "Residents", "Count"])

# -------------------------------
# Total Population by Year
# -------------------------------
st.header("Total Population by Year")

total_population_df = (
    df.groupby("Year")["Count"]
    .sum()
    .reset_index()
)
total_population_df.columns = ["Year", "Total_Population"]

st.dataframe(
    total_population_df.style.format(
        {"Total_Population": "{:,}"}
    )
)

# -------------------------------
# Female to Male Ratio
# -------------------------------
st.header("Female to Male Ratio by Ethnic Group")

years = sorted(df["Year"].unique())
groups = {
    "Total": ("Total Male Residents", "Total Female Residents"),
    "Malays": ("Total Male Malays", "Total Female Malays"),
    "Chinese": ("Total Male Chinese", "Total Female Chinese"),
    "Indians": ("Total Male Indians", "Total Female Indians"),
    "Others": (
        "Other Ethnic Groups (Males)",
        "Other Ethnic Groups (Females)"
    ),
}

for y in years:
    with st.expander(f"Year {int(y)}"):
        ratio_data = []

        for g, (m, f) in groups.items():
            male_row = df[(df["Year"] == y) & (df["Residents"] == m)]
            female_row = df[(df["Year"] == y) & (df["Residents"] == f)]

            if not male_row.empty and not female_row.empty:
                male = male_row["Count"].values[0]
                female = female_row["Count"].values[0]

                ratio_data.append({
                    "Group": g,
                    "Males": f"{male:,}",
                    "Females": f"{female:,}",
                    "F/M Ratio": f"{female / male:.4f}"
                })

        if ratio_data:
            st.table(pd.DataFrame(ratio_data))

# -------------------------------
# Population Growth
# -------------------------------
st.header("Total Resident Population Growth")

popu = (
    df[df["Residents"] == "Total Residents"]
    [["Year", "Count"]]
    .sort_values("Year")
    .copy()
)

popu["Growth % (YoY)"] = popu["Count"].pct_change() * 100
popu["Cumulative Growth %"] = (
    (popu["Count"] - popu["Count"].iloc[0])
    / popu["Count"].iloc[0]
) * 100

display_popu = popu.copy()
display_popu["Year"] = display_popu["Year"].astype(int)
display_popu["Count"] = display_popu["Count"].apply(lambda x: f"{x:,}")
display_popu["Growth % (YoY)"] = display_popu["Growth % (YoY)"].apply(
    lambda x: "N/A" if pd.isna(x) else f"{x:.2f}%"
)
display_popu["Cumulative Growth %"] = display_popu["Cumulative Growth %"].apply(
    lambda x: f"{x:.2f}%"
)

st.table(display_popu)
