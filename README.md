# Sales Data Analysis

A Python project that loads, cleans, and analyzes a sales dataset to extract actionable business insights and visualize key metrics.

## Features

- Loads and cleans raw CSV sales data (handles missing values, duplicates, and type conversion)
- Computes key business metrics: best region, best product, best customer, and monthly revenue trends
- Visualizes results with bar charts and line charts using Matplotlib
- Modular structure with separated concerns across `loader`, `metrics`, and `visualizer` modules

## Project Structure

```
sales_analysis/
│
├── data/
│   └── sales_data.csv
│
├── outputs/
│   ├── region-chart.png
│   ├── product-chart.png
│   ├── customer-chart.png
|   ├── month-chart.png
|   └── month-plot.png
│
├── src/
│   ├── __init__.py
│   ├── loader.py
│   ├── metrics.py
│   └── visualizer.py
│
└── main.py
```

## How to Run

1. Clone the repository
2. Install dependencies:
```
pip install pandas matplotlib
```
3. Run the project:
```
python main.py
```

## Libraries Used

- [Pandas](https://pandas.pydata.org/) — data loading, cleaning, and analysis
- [Matplotlib](https://matplotlib.org/) — data visualization
