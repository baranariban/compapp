import streamlit as st

if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("Unauthorized access. Please log in.")
    st.stop()

st.title("CompApp: Composite Application")
st.markdown("### :red[by Ali Baran Arıban]")
st.title("Composite Selector")
st.write("Click on the properties you want in your composite/polymer. Then fill in the blank spaces with the maximum or the minimum limits of the parameters you desire. The application will provide you a list of composites which are suitable for your project's requirements. You will also have a chance to compare these composites with total grades out of 100.")

datasets = {
    "PEEK UNFILLED": {"Cost (USD/kg)": (7.63, 14.17), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (40, 60), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (80, 80), "Shrinkage (%)": (1.1, 1.1), "Glass Transition Temperature (°C)": (143, 143), "Tensile Strength (MPa)": (70, 100), "Flexural Modulus (GPa)": (3.7, 3.9), "Density (kg/m3)": (1270, 1320)},
    "PEEK 30% GF": {"Cost (USD/kg)": (7.63, 14.17), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (15, 20), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (80, 80), "Shrinkage (%)": (0.2, 1.0), "Glass Transition Temperature (°C)": (143, 143), "Tensile Strength (MPa)": (150, 180), "Flexural Modulus (GPa)": (9, 10.3), "Density (kg/m3)": (1490, 1540)},
    "PEEK 30% CF": {"Cost (USD/kg)": (7.63, 14.17), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (15, 40), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (80, 80), "Shrinkage (%)": (0.1, 0.4), "Glass Transition Temperature (°C)": (143, 143), "Tensile Strength (MPa)": (200, 220), "Flexural Modulus (GPa)": (13, 20), "Density (kg/m3)": (1440, 1440)},
    "PEEK 5-60% GF": {"Cost (USD/kg)": (7.63, 14.17), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (3.24, 99.7), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (80, 80), "Shrinkage (%)": (0.05, 0.5), "Glass Transition Temperature (°C)": (143, 178), "Tensile Strength (MPa)": (80, 220), "Flexural Modulus (GPa)": (3.80, 55), "Density (kg/m3)": (1300, 1930)},
    "PEEK 10-60% CF": {"Cost (USD/kg)": (7.63, 14.17), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (1.80, 60), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (80, 80), "Shrinkage (%)": (0, 2.2), "Glass Transition Temperature (°C)": (143, 170), "Tensile Strength (MPa)": (75, 2070), "Flexural Modulus (GPa)": (2.12, 159), "Density (kg/m3)": (1320, 1900)},
    "PEEK 5-45% PTFE": {"Cost (USD/kg)": (7.63, 14.17), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (9, 65), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (80, 80), "Shrinkage (%)": (0.1, 2.5), "Glass Transition Temperature (°C)": (143, 170), "Tensile Strength (MPa)": (64, 155), "Flexural Modulus (GPa)": (2.41, 14), "Density (kg/m3)": (1320, 1690)},
    "PEEK ARAMID FIBER FILLED": {"Cost (USD/kg)": (7.63, 14.17), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (5, 10), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (80, 80), "Shrinkage (%)": (0.05, 1.5), "Glass Transition Temperature (°C)": (143, 170), "Tensile Strength (MPa)": (75, 193), "Flexural Modulus (GPa)": (4.83, 22.8), "Density (kg/m3)": (1310, 1500)},
    "PESU UNFILLED": {"Cost (USD/kg)": (7.63, 13.08), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (27, 60), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (50, 50), "Shrinkage (%)": (0.6, 0.7), "Glass Transition Temperature (°C)": (210, 230), "Tensile Strength (MPa)": (70, 95), "Flexural Modulus (GPa)": (2.4, 2.9), "Density (kg/m3)": (1370, 1400)},
    "PESU 10% GF": {"Cost (USD/kg)": (7.63, 13.08), "Coefficient of Thermal Expansion (CTE) (µstrain/°C)": (25, 50.4), "Interfacial Properties with Carbon Fiber (IFSS, MPa)": (50, 50), "Shrinkage (%)": (0.1, 0.8), "Glass Transition Temperature (°C)": (225, 225), "Tensile Strength (MPa)": (66.9, 135), "Flexural Modulus (GPa)": (3.45, 8.62), "Density (kg/m3)": (1390, 1580)},
}

all_properties = set()

for dataset in datasets.values():
    all_properties.update(dataset.keys())

if "selected_properties" not in st.session_state:
    st.session_state.selected_properties = set()

for prop in sorted(all_properties):
    if st.button(f"Filter by {prop}"):
        if prop in st.session_state.selected_properties:
            st.session_state.selected_properties.remove(prop)
        else:
            st.session_state.selected_properties.add(prop)

user_inputs = {}

for prop in st.session_state.selected_properties:
    user_inputs[prop] = st.number_input(f"Enter value for property {prop}:", min_value=0.00, step=0.01)

matching_datasets = []
for dataset, properties in datasets.items():
    match = True
    for prop in st.session_state.selected_properties:
        if not (properties[prop][0] <= user_inputs[prop] <= properties[prop][1]):
            match = False
            break  

    if match:
        matching_datasets.append(dataset)

if matching_datasets:
    result = f"The input values match with dataset(s): **{', '.join(matching_datasets)}**"
elif st.session_state.selected_properties:
    result = "No dataset includes the selected values."
else:
    result = "Please select at least one property to filter by."

st.write(result)
