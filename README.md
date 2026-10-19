# Sales Analysis Using Python

## Project Overview

This project analyses retail sales data to identify sales trends, top-performing regions, product categories, and opportunities for business improvement.

The analysis was completed as part of the **Syntecxhub Data Science Internship — Task 4, Project 1: Sales Analysis**.

## Objectives

- Calculate key sales performance indicators (KPIs).
- Identify the highest-performing sales regions and product categories.
- Analyse monthly sales trends.
- Visualise sales performance using charts.
- Generate a one-page PDF summary with key findings and recommendations.

## Tools and Technologies

- **Python** — data analysis and calculations
- **Pandas** — data cleaning and manipulation
- **Matplotlib** — data visualisation
- **VS Code / Jupyter Notebook** — development environment

## Dataset

The dataset contains 1,000 sales records and 14 columns, including:

- Sale date
- Sales representative
- Region
- Sales amount
- Quantity sold
- Product category
- Unit cost and unit price
- Customer type
- Discount
- Payment method
- Sales channel

The dataset was checked for missing values and duplicate records, and the sale dates were converted to datetime format for time-based analysis.

## Key Findings

| Metric | Result |
|---|---:|
| Total sales amount | R5,019,265.23 |
| Average sales amount per record | R5,019.27 |
| Total quantity sold | 25,355 |
| Number of sales records | 1,000 |
| Top-performing region | North |
| Top-performing product category | Clothing |

The North region recorded R1,369,612.51 in sales, while Clothing generated R1,313,474.36.

January 2023 had the highest monthly sales amount at R476,092.36.

**Data limitation:** January 2024 contains only three records. Its low sales total should not be directly compared with the full months of 2023. The available data also covers only one full year, so it is insufficient to establish recurring seasonal patterns.

## Visualisations

The project includes charts showing:

- Sales by region
- Sales by product category
- Monthly sales trends

A one-page PDF report summarises the key metrics, visualisations, findings, and recommendations.

## Business Recommendations

1. Investigate the strategies contributing to the North region's strong sales performance.
2. Review the performance of other regions to identify opportunities for improvement.
3. Analyse Clothing sales to identify popular products and potential growth opportunities.
4. Monitor monthly sales over additional years to establish more reliable seasonal trends.
5. Verify the completeness of the January 2024 data before drawing conclusions about declining sales.

## Project Structure

```text
Syntecxhub_Sales_Analysis/
├── data/
│   └── sales_data.csv
├── sales_analysis.ipynb
├── create_summary.py
├── sales_summary.pdf
└── README.md
```

The exact folder contents may vary depending on which project files are included in the repository.

## How to Run the Project

1. Clone or download this repository.
2. Install the required Python libraries:

   ```bash
   pip install pandas matplotlib
   ```

3. Ensure the dataset is saved at `data/sales_data.csv`.
4. Open and run `sales_analysis.ipynb` to explore the analysis.
5. Run the following command to generate the PDF summary:

   ```bash
   python create_summary.py
   ```

6. Open `sales_summary.pdf` to review the report.

## Conclusion

This project demonstrates how Python can be used to analyse sales data, calculate performance metrics, identify business trends, and communicate findings through visualisations and a concise report.

The analysis provides a starting point for data-driven decisions while recognising the limitations of the available dataset.