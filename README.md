# Pie Chart Creator App

A quick and easy web application for creating pie charts on the go!

## Features

- 📝 **Manual Data Entry** - Add labels and values directly
- 📤 **CSV Import** - Upload data from CSV files
- 🎨 **Customization** - Change titles, toggle percentages and legends
- 📊 **Data Summary** - View results in a table
- 📥 **Download** - Export charts as PNG or data as CSV

## Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/pie-chart-creator.git
cd pie-chart-creator
```

2. Create a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Start the app with:
```bash
streamlit run MyApp/pie_chart_app.py
```

Then open your browser to `http://localhost:8501`

## Files

- `MyApp/pie_chart_app.py` - Main Streamlit application
- `MyApp/MyTest` - Sample script for generating static pie charts

## Requirements

- Python 3.9+
- streamlit
- matplotlib
- pandas
