import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="Pie Chart Creator", layout="centered")
st.title("🥧 Quick Pie Chart Creator by B.Reiner")

# Sidebar for data input
st.sidebar.header("Add Your Data")

# Input method selection
input_method = st.sidebar.radio("Choose input method:", ["Manual Entry", "Upload CSV"])

data = {}

if input_method == "Manual Entry":
    # Number of entries
    num_entries = st.sidebar.number_input("How many entries?", min_value=1, max_value=10, value=3)
    
    st.sidebar.subheader("Enter Data")
    for i in range(num_entries):
        col1, col2 = st.sidebar.columns(2)
        with col1:
            label = st.text_input(f"Label {i+1}", f"Item {i+1}", key=f"label_{i}")
        with col2:
            value = st.number_input(f"Value {i+1}", min_value=0.1, value=25.0, key=f"value_{i}")
        
        if label:
            data[label] = value

else:  # Upload CSV
    uploaded_file = st.sidebar.file_uploader("Upload CSV file", type=['csv'])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.sidebar.write("File preview:")
        st.sidebar.dataframe(df.head())
        
        # Extract data from CSV
        if len(df.columns) >= 2:
            label_col = df.columns[0]
            value_col = df.columns[1]
            for idx, row in df.iterrows():
                data[str(row[label_col])] = float(row[value_col])

# Chart customization
st.sidebar.markdown("---")
st.sidebar.subheader("Chart Settings")
title = st.sidebar.text_input("Chart Title", "Data Distribution")
show_legend = st.sidebar.checkbox("Show Legend", value=True)
show_percentages = st.sidebar.checkbox("Show Percentages", value=True)

# Create and display pie chart
if data:
    labels = list(data.keys())
    sizes = list(data.values())
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    autopct = '%1.1f%%' if show_percentages else None
    wedges, texts, autotexts = ax.pie(
        sizes, 
        labels=labels, 
        autopct=autopct,
        startangle=90,
        textprops={'fontsize': 10}
    )
    
    ax.set_title(title, fontsize=14, fontweight='bold')
    
    if show_legend:
        ax.legend(wedges, labels, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    
    st.pyplot(fig)
    
    # Display data table
    st.subheader("Data Summary")
    df_display = pd.DataFrame({
        'Label': labels,
        'Value': sizes,
        'Percentage': [f"{(v/sum(sizes)*100):.1f}%" for v in sizes]
    })
    st.dataframe(df_display, use_container_width=True)
    
    # Download options
    st.subheader("Download")
    col1, col2 = st.columns(2)
    with col1:
        plt.savefig('pie_chart.png', dpi=300, bbox_inches='tight')
        with open('pie_chart.png', 'rb') as f:
            st.download_button("📥 Download as PNG", f, "pie_chart.png", "image/png")
    
    with col2:
        csv = df_display.to_csv(index=False)
        st.download_button("📊 Download as CSV", csv, "pie_chart_data.csv", "text/csv")
else:
    st.info("👈 Please add data using the sidebar to create a pie chart!")
