import streamlit as st
import pandas as pd

st.title("Singapore Resident Population Dashboard")

# --------------------------------
# Embedded Data (2000–2018)
# --------------------------------
data = [
    # ===== 2000 =====
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

    # ===== 2001 =====
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

    # ===== 2002 =====
    [2002, "Total Residents", 3382944],
    [2002, "Total Male Residents", 1684295],
    [2002, "Total Female Residents", 1698649],
    [2002, "Total Malays", 468360],
    [2002, "Total Male Malays", 235076],
    [2002, "Total Female Malays", 233284],
    [2002, "Total Chinese", 2589525],
    [2002, "Total Male Chinese", 1283362],
    [2002, "Total Female Chinese", 1306163],
    [2002, "Total Indians", 271923],
    [2002, "Total Male Indians", 140768],
    [2002, "Total Female Indians", 131155],
    [2002, "Other Ethnic Groups (Total)", 53136],
    [2002, "Other Ethnic Groups (Males)", 25089],
    [2002, "Other Ethnic Groups (Females)", 28047],

    # ===== 2003 =====
    [2003, "Total Residents", 3366891],
    [2003, "Total Male Residents", 1673401],
    [2003, "Total Female Residents", 1693490],
    [2003, "Total Malays", 469791],
    [2003, "Total Male Malays", 235597],
    [2003, "Total Female Malays", 234194],
    [2003, "Total Chinese", 2572607],
    [2003, "Total Male Chinese", 1273256],
    [2003, "Total Female Chinese", 1299351],
    [2003, "Total Indians", 269899],
    [2003, "Total Male Indians", 138642],
    [2003, "Total Female Indians", 131257],
    [2003, "Other Ethnic Groups (Total)", 54594],
    [2003, "Other Ethnic Groups (Males)", 25906],
    [2003, "Other Ethnic Groups (Females)", 28688],

    # ===== 2004 =====
    [2004, "Total Residents", 3413266],
    [2004, "Total Male Residents", 1695031],
    [2004, "Total Female Residents", 1718235],
    [2004, "Total Malays", 475689],
    [2004, "Total Male Malays", 238236],
    [2004, "Total Female Malays", 237453],
    [2004, "Total Chinese", 2599813],
    [2004, "Total Male Chinese", 1285557],
    [2004, "Total Female Chinese", 1314256],
    [2004, "Total Indians", 278106],
    [2004, "Total Male Indians", 142754],
    [2004, "Total Female Indians", 135352],
    [2004, "Other Ethnic Groups (Total)", 59658],
    [2004, "Other Ethnic Groups (Males)", 28484],
    [2004, "Other Ethnic Groups (Females)", 31174],

    # ===== 2005 =====
    [2005, "Total Residents", 3467814],
    [2005, "Total Male Residents", 1721139],
    [2005, "Total Female Residents", 1746675],
    [2005, "Total Malays", 480722],
    [2005, "Total Male Malays", 240406],
    [2005, "Total Female Malays", 240316],
    [2005, "Total Chinese", 2626723],
    [2005, "Total Male Chinese", 1297849],
    [2005, "Total Female Chinese", 1328874],
    [2005, "Total Indians", 291131],
    [2005, "Total Male Indians", 149621],
    [2005, "Total Female Indians", 141510],
    [2005, "Other Ethnic Groups (Total)", 69238],
    [2005, "Other Ethnic Groups (Males)", 33263],
    [2005, "Other Ethnic Groups (Females)", 35975],

    # ===== 2006 =====
    [2006, "Total Residents", 3525894],
    [2006, "Total Male Residents", 1748242],
    [2006, "Total Female Residents", 1777652],
    [2006, "Total Malays", 485978],
    [2006, "Total Male Malays", 242759],
    [2006, "Total Female Malays", 243219],
    [2006, "Total Chinese", 2656358],
    [2006, "Total Male Chinese", 1310873],
    [2006, "Total Female Chinese", 1345485],
    [2006, "Total Indians", 303096],
    [2006, "Total Male Indians", 155938],
    [2006, "Total Female Indians", 147158],
    [2006, "Other Ethnic Groups (Total)", 80462],
    [2006, "Other Ethnic Groups (Males)", 38672],
    [2006, "Other Ethnic Groups (Females)", 41790],

    # ===== 2007 =====
    [2007, "Total Residents", 3583082],
    [2007, "Total Male Residents", 1775477],
    [2007, "Total Female Residents", 1807605],
    [2007, "Total Malays", 490552],
    [2007, "Total Male Malays", 244969],
    [2007, "Total Female Malays", 245583],
    [2007, "Total Chinese", 2686997],
    [2007, "Total Male Chinese", 1324715],
    [2007, "Total Female Chinese", 1362282],
    [2007, "Total Indians", 313395],
    [2007, "Total Male Indians", 161484],
    [2007, "Total Female Indians", 151911],
    [2007, "Other Ethnic Groups (Total)", 92138],
    [2007, "Other Ethnic Groups (Males)", 44309],
    [2007, "Other Ethnic Groups (Females)", 47829],

    # ===== 2008 =====
    [2008, "Total Residents", 3642659],
    [2008, "Total Male Residents", 1802992],
    [2008, "Total Female Residents", 1839667],
    [2008, "Total Malays", 495110],
    [2008, "Total Male Malays", 247017],
    [2008, "Total Female Malays", 248093],
    [2008, "Total Chinese", 2721779],
    [2008, "Total Male Chinese", 1339596],
    [2008, "Total Female Chinese", 1382183],
    [2008, "Total Indians", 323431],
    [2008, "Total Male Indians", 167149],
    [2008, "Total Female Indians", 156282],
    [2008, "Other Ethnic Groups (Total)", 102339],
    [2008, "Other Ethnic Groups (Males)", 49230],
    [2008, "Other Ethnic Groups (Females)", 53109],

    # ===== 2009 =====
    [2009, "Total Residents", 3733876],
    [2009, "Total Male Residents", 1844732],
    [2009, "Total Female Residents", 1889144],
    [2009, "Total Malays", 500051],
    [2009, "Total Male Malays", 249115],
    [2009, "Total Female Malays", 250936],
    [2009, "Total Chinese", 2770303],
    [2009, "Total Male Chinese", 1360224],
    [2009, "Total Female Chinese", 1410079],
    [2009, "Total Indians", 343509],
    [2009, "Total Male Indians", 178129],
    [2009, "Total Female Indians", 165380],
    [2009, "Other Ethnic Groups (Total)", 120013],
    [2009, "Other Ethnic Groups (Males)", 57264],
    [2009, "Other Ethnic Groups (Females)", 62749],

    # ===== 2010–2018 =====
    # (Your provided data is already correct and included)
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
