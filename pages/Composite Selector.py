import streamlit as st
import pandas as pd
from io import BytesIO

def generate_excel_template():
    columns = ["Name"]
    for prop in properties:
        columns.append(f"{prop} min")
        columns.append(f"{prop} max")
    
    df_template = pd.DataFrame(columns=columns)
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df_template.to_excel(writer, index=False, sheet_name='Template')
    output.seek(0)
    return output

if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("Unauthorized access. Please log in.")
    st.stop()

st.title("CompApp: Composite Application")
st.markdown("### :red[by Ali Baran Arıban]")
st.title("Composite Selector")
st.write("Click on the properties you want in your composite/polymer. Then fill in the blank spaces with the maximum or the minimum limits of the parameters you desire. The application will provide you a list of composites which are suitable for your project's requirements. You will also have a chance to compare these composites with total grades out of 100.")

if "datasets" not in st.session_state:
    st.session_state.datasets = {
        "PEEK UNFILLED": {"Cost (USD/kg)": (54.50, 81.75), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (40, 60), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (80, 80), "Shrinkage (%)": (1.1, 1.1), "Glass Transition Temperature (°C)": (143, 143), "Tensile Strength (MPa)": (70, 100), "Flexural Modulus (GPa)": (3.7, 3.9), "Density (kg/m3)": (1270, 1320)},
        "PEEK 30% GF": {"Cost (USD/kg)": (54.50, 81.75), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (15, 20), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (80, 80), "Shrinkage (%)": (0.2, 1.0), "Glass Transition Temperature (°C)": (143, 143), "Tensile Strength (MPa)": (150, 180), "Flexural Modulus (GPa)": (9, 10.3), "Density (kg/m3)": (1490, 1540)},
        "PEEK 30% CF": {"Cost (USD/kg)": (54.50, 81.75), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (15, 40), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (80, 80), "Shrinkage (%)": (0.1, 0.4), "Glass Transition Temperature (°C)": (143, 143), "Tensile Strength (MPa)": (200, 220), "Flexural Modulus (GPa)": (13, 20), "Density (kg/m3)": (1440, 1440)},
        "PEEK 5-60% GF": {"Cost (USD/kg)": (54.50, 81.75), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (3.24, 99.7), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (80, 80), "Shrinkage (%)": (0.05, 0.5), "Glass Transition Temperature (°C)": (143, 178), "Tensile Strength (MPa)": (80, 220), "Flexural Modulus (GPa)": (3.80, 55), "Density (kg/m3)": (1300, 1930)},
        "PEEK 10-60% CF": {"Cost (USD/kg)": (54.50, 81.75), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (1.80, 60), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (80, 80), "Shrinkage (%)": (0, 2.2), "Glass Transition Temperature (°C)": (143, 170), "Tensile Strength (MPa)": (75, 2070), "Flexural Modulus (GPa)": (2.12, 159), "Density (kg/m3)": (1320, 1900)},
        "PEEK 5-45% PTFE": {"Cost (USD/kg)": (54.50, 81.75), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (9, 65), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (80, 80), "Shrinkage (%)": (0.1, 2.5), "Glass Transition Temperature (°C)": (143, 170), "Tensile Strength (MPa)": (64, 155), "Flexural Modulus (GPa)": (2.41, 14), "Density (kg/m3)": (1320, 1690)},
        "PEEK ARAMID FIBER": {"Cost (USD/kg)": (54.50, 81.75), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (5, 10), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (80, 80), "Shrinkage (%)": (0.05, 1.5), "Glass Transition Temperature (°C)": (143, 170), "Tensile Strength (MPa)": (75, 193), "Flexural Modulus (GPa)": (4.83, 22.8), "Density (kg/m3)": (1310, 1500)},
        "PESU UNFILLED": {"Cost (USD/kg)": (7.63, 13.08), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (27, 60), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (50, 50), "Shrinkage (%)": (0.6, 0.7), "Glass Transition Temperature (°C)": (210, 230), "Tensile Strength (MPa)": (70, 95), "Flexural Modulus (GPa)": (2.4, 2.9), "Density (kg/m3)": (1370, 1400)},
        "PESU 10% GF": {"Cost (USD/kg)": (7.63, 13.08), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (25, 50.4), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (50, 50), "Shrinkage (%)": (0.1, 0.8), "Glass Transition Temperature (°C)": (225, 225), "Tensile Strength (MPa)": (66.9, 135), "Flexural Modulus (GPa)": (3.45, 8.62), "Density (kg/m3)": (1390, 1580)},
        "PESU 20% GF": {"Cost (USD/kg)": (7.63, 13.08), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (20, 39.6), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (50, 50), "Shrinkage (%)": (0.1, 0.8), "Glass Transition Temperature (°C)": (225, 225), "Tensile Strength (MPa)": (81.4, 150), "Flexural Modulus (GPa)": (3.79, 6.89), "Density (kg/m3)": (1470, 1620)},
        "PESU 30% GF": {"Cost (USD/kg)": (7.63, 13.08), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (15, 36), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (50, 50), "Shrinkage (%)": (0.1, 0.5), "Glass Transition Temperature (°C)": (225, 225), "Tensile Strength (MPa)": (60, 150), "Flexural Modulus (GPa)": (7.58, 11.3), "Density (kg/m3)": (1460, 1700)},
        "PPS UNFILLED": {"Cost (USD/kg)": (7.63, 14.17), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (30, 50), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (40, 40), "Shrinkage (%)": (0.6, 1.4), "Glass Transition Temperature (°C)": (88, 93), "Tensile Strength (MPa)": (50, 80), "Flexural Modulus (GPa)": (3.8, 4.2), "Density (kg/m3)": (1350, 1350)},
        "PPS 10% GF": {"Cost (USD/kg)": (7.63, 14.17), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (10, 50), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (40, 40), "Shrinkage (%)": (0.3, 1.0), "Glass Transition Temperature (°C)": (90, 90), "Tensile Strength (MPa)": (34.5, 375), "Flexural Modulus (GPa)": (4.83, 21), "Density (kg/m3)": (1380, 2060)},
        "PPS 20% GF": {"Cost (USD/kg)": (7.63, 14.17), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (12, 60), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (40, 40), "Shrinkage (%)": (0.05, 0.8), "Glass Transition Temperature (°C)": (90, 90), "Tensile Strength (MPa)": (86, 162), "Flexural Modulus (GPa)": (5.10, 25), "Density (kg/m3)": (1300, 2530)},
        "PPS 30% GF": {"Cost (USD/kg)": (7.63, 14.17), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (9, 120), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (40, 40), "Shrinkage (%)": (0.02, 1.20), "Glass Transition Temperature (°C)": (90, 90), "Tensile Strength (MPa)": (33.1, 203), "Flexural Modulus (GPa)": (1.20, 30.1), "Density (kg/m3)": (1400, 1690)},
        "PPS 40% GF": {"Cost (USD/kg)": (7.63, 14.17), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (10, 135), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (40, 40), "Shrinkage (%)": (0.05, 1.00), "Glass Transition Temperature (°C)": (88, 90), "Tensile Strength (MPa)": (32.4, 220), "Flexural Modulus (GPa)": (3.10, 34.90), "Density (kg/m3)": (1350, 1800)},
        "PPS 50% GF": {"Cost (USD/kg)": (7.63, 14.17), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (7, 45), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (40, 40), "Shrinkage (%)": (0.05, 1.00), "Glass Transition Temperature (°C)": (90, 90), "Tensile Strength (MPa)": (94.0, 179.953), "Flexural Modulus (GPa)": (10.3, 39.2), "Density (kg/m3)": (1530, 1900)},
        "PPS 10% CF": {"Cost (USD/kg)": (7.63, 14.17), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (5, 32), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (40, 40), "Shrinkage (%)": (0.1, 0.86), "Glass Transition Temperature (°C)": (90, 90), "Tensile Strength (MPa)": (67.6, 680), "Flexural Modulus (GPa)": (0.552, 57), "Density (kg/m3)": (1290, 1960)},
        "PPS 20% CF": {"Cost (USD/kg)": (7.63, 14.17), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (15, 20), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (40, 40), "Shrinkage (%)": (0.02, 0.25), "Glass Transition Temperature (°C)": (90, 90), "Tensile Strength (MPa)": (27.6, 186), "Flexural Modulus (GPa)": (8.27, 18.6), "Density (kg/m3)": (1350, 1540)},
        "PPS 30% CF": {"Cost (USD/kg)": (7.63, 14.17), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (5, 20), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (40, 40), "Shrinkage (%)": (0.02, 0.60), "Glass Transition Temperature (°C)": (90, 90), "Tensile Strength (MPa)": (46.9, 236), "Flexural Modulus (GPa)": (8.00, 32.00), "Density (kg/m3)": (1410, 1580)},
        "PPS 40% CF": {"Cost (USD/kg)": (7.63, 14.17), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (5, 10), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (40, 40), "Shrinkage (%)": (0.05, 0.60), "Glass Transition Temperature (°C)": (90, 90), "Tensile Strength (MPa)": (77.2, 234), "Flexural Modulus (GPa)": (11.00, 35.00), "Density (kg/m3)": (1480, 1720)},
        "PPS 10-40% CF + PTFE": {"Cost (USD/kg)": (7.63, 14.17), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (9, 60), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (40, 40), "Shrinkage (%)": (0.01, 0.50), "Glass Transition Temperature (°C)": (90, 94), "Tensile Strength (MPa)": (53, 180), "Flexural Modulus (GPa)": (9.00, 27.60), "Density (kg/m3)": (1080, 1620)},
        "PPS CONDUCTIVE": {"Cost (USD/kg)": (7.63, 14.17), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (19.80, 19.80), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (40, 40), "Shrinkage (%)": (0, 0.60), "Glass Transition Temperature (°C)": (90, 90), "Tensile Strength (MPa)": (45, 172), "Flexural Modulus (GPa)": (0.552, 25.50), "Density (kg/m3)": (1290, 3700)},
        "PPS 25-65% GF + MINERAL": {"Cost (USD/kg)": (7.63, 14.17), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (10, 250), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (40, 40), "Shrinkage (%)": (0.1, 1.00), "Glass Transition Temperature (°C)": (90, 90), "Tensile Strength (MPa)": (42.1, 197), "Flexural Modulus (GPa)": (7.00, 14.00), "Density (kg/m3)": (1530, 2110)},
        "PPS STAINLESS STEEL FIBER": {"Cost (USD/kg)": (7.63, 14.17), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (20, 30), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (40, 40), "Shrinkage (%)": (0.2, 1.60), "Glass Transition Temperature (°C)": (90, 90), "Tensile Strength (MPa)": (47, 145), "Flexural Modulus (GPa)": (4.00, 17.90), "Density (kg/m3)": (1410, 1790)},
        "PPS 10-50% GF + PTFE": {"Cost (USD/kg)": (7.63, 14.17), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (10.8, 32.4), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (40, 40), "Shrinkage (%)": (0.05, 0.80), "Glass Transition Temperature (°C)": (90, 90), "Tensile Strength (MPa)": (26.2, 180), "Flexural Modulus (GPa)": (4.90, 17.90), "Density (kg/m3)": (1410, 1870)},
        "PPS 10-70% PTFE": {"Cost (USD/kg)": (7.63, 14.17), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (50, 100), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (40, 40), "Shrinkage (%)": (0.2, 2.0), "Glass Transition Temperature (°C)": (90, 90), "Tensile Strength (MPa)": (11, 160), "Flexural Modulus (GPa)": (1.31, 15), "Density (kg/m3)": (1420, 2030)},
        "PPS 10-30% ARAMID FIBER": {"Cost (USD/kg)": (7.63, 14.17), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (10, 15), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (40, 40), "Shrinkage (%)": (0.05, 1.40), "Glass Transition Temperature (°C)": (90, 90), "Tensile Strength (MPa)": (45, 134), "Flexural Modulus (GPa)": (3.50, 2.70), "Density (kg/m3)": (1250, 1560)}
    }

properties = [
    "Cost (USD/kg)",
    "Coefficient of Thermal Expansion (CTE) (µstrain/°C)",
    "Interfacial Properties with Carbon Fiber (IFSS, MPa)",
    "Shrinkage (%)",
    "Glass Transition Temperature (°C)",
    "Tensile Strength (MPa)",
    "Flexural Modulus (GPa)",
    "Density (kg/m3)"
]

option = st.radio("Choose how you'd like to proceed:", [
    "Use embedded dataset",
    "Add manual entry",
    "Upload dataset from Excel"
])

if option == "Add manual entry":
    new_entry = {}
    composite_name = st.text_input("Enter the name of the new composite")
    for prop in properties:
        col1, col2 = st.columns(2)
        with col1:
            min_val = st.number_input(f"Min {prop}", key=f"min_{prop}")
        with col2:
            max_val = st.number_input(f"Max {prop}", key=f"max_{prop}")
        new_entry[prop] = (min_val, max_val)

    if st.button("Add composite to dataset"):
        if composite_name and all(isinstance(val, tuple) for val in new_entry.values()):
            st.session_state.datasets[composite_name] = new_entry
            st.success(f"{composite_name} added successfully.")

elif option == "Upload dataset from Excel":
    st.info("""📄 Please download the template, fill in your data, and upload it back.

- Include values for all properties.
- Do **not change column names**.

📥 You can download the blank Excel file using the button below.""")

    st.download_button(
        label="📥 Download Excel Template",
        data=generate_excel_template(),
        file_name="composite_template.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    uploaded_file = st.file_uploader("Upload your completed Excel file here", type=["xlsx"])
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        for idx, row in df.iterrows():
            name = row["Name"]
            entry = {}
            for prop in properties:
                entry[prop] = (row[f"{prop} min"], row[f"{prop} max"])
            st.session_state.datasets[name] = entry
        st.success("All composites from Excel uploaded successfully.")

st.subheader("Select the Properties You Want to Filter")

selected_filters = {}

for prop in properties:
    if st.checkbox(f"Filter by {prop}"):
        col1, col2 = st.columns([1, 2])
        with col1:
            condition = st.selectbox(f"Condition for {prop}", ["smaller than", "larger than", "equal to"], key=f"cond_{prop}")
        with col2:
            value = st.number_input(f"Value for {prop}", key=f"val_{prop}")
        selected_filters[prop] = (condition, value)

matching_polymers = []

for polymer, properties_dict in st.session_state.datasets.items():
    match = True
    for prop, (condition, user_val) in selected_filters.items():
        min_val, max_val = properties_dict[prop]

        if condition == "smaller than":
            if not (min_val <= user_val <= max_val or max_val < user_val):
                match = False
                break

        elif condition == "larger than":
            if not (min_val <= user_val <= max_val or min_val > user_val):
                match = False
                break

        elif condition == "equal to":
            if not (min_val <= user_val <= max_val):
                match = False
                break

    if match:
        matching_polymers.append(polymer)

st.subheader("Matching Composites")
if matching_polymers:
    for name in matching_polymers:
        st.write(f"✅ {name}")
else:
    st.warning("No matching composites found.")

if matching_polymers:
    if st.button("Show detailed table of matching composites"):
        table_data = {}
        for name in matching_polymers:
            prop_vals = {}
            for prop, (min_val, max_val) in st.session_state.datasets[name].items():
                prop_vals[prop] = f"{min_val}–{max_val}"
            table_data[name] = prop_vals
        df = pd.DataFrame(table_data)
        st.dataframe(df)

if st.button("🔢 Score and rank matching composites"):
    st.subheader("Set importance (weight) for each selected property")

    weights = {}
    total_weight = 0

    for prop in selected_filters.keys():
        weight = st.number_input(
            f"Weight for '{prop}' (0–100)",
            min_value=0,
            max_value=100,
            value=0,
            step=1,
            key=f"weight_{prop}"
        )
        weights[prop] = weight
        total_weight += weight

    st.markdown(f"🧮 **Total weight: {total_weight}/100**")
    if total_weight != 100:
        st.warning("⚠️ Total weight must be exactly 100 to proceed.")
    else:
        # Skor hesaplama
        scores = {}

        for name in matching_polymers:
            total_score = 0
            for prop, (condition, user_val) in selected_filters.items():
                min_val, max_val = st.session_state.datasets[name][prop]
                weight = weights[prop]

                if min_val == max_val or user_val is None:
                    continue

                # Normalize uygunluk skoru (0 ile 1 arası)
                if user_val < min_val or user_val > max_val:
                    score = 0
                else:
                    center = (min_val + max_val) / 2
                    score = 1 - abs(user_val - center) / (max_val - min_val)

                total_score += score * weight

            # Toplam puanı 100'e ölçekle
            final_score = round(total_score, 2)
            scores[name] = final_score

        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        st.subheader("🏆 Ranked Composites by 100-Point Weighted Score")
        for i, (name, score) in enumerate(sorted_scores, 1):
            st.write(f"{i}. **{name}** — Score: {score:.2f} / 100")
