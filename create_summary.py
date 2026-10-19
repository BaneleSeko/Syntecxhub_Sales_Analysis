
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Load your sales dataset
df = pd.read_csv("data/sales_data.csv")
df["Sale_Date"] = pd.to_datetime(df["Sale_Date"], errors="coerce")

# Calculate KPIs
total_sales = df["Sales_Amount"].sum()
average_sales = df["Sales_Amount"].mean()
total_quantity = df["Quantity_Sold"].sum()
transactions = len(df)

# Prepare summaries
region_sales = df.groupby("Region")["Sales_Amount"].sum().sort_values()
category_sales = df.groupby("Product_Category")["Sales_Amount"].sum().sort_values()
monthly_sales = (
    df.set_index("Sale_Date")["Sales_Amount"]
    .resample("MS").sum()
)

top_region = region_sales.idxmax()
top_category = category_sales.idxmax()
best_month = monthly_sales.idxmax()

# Create a one-page PDF
with PdfPages("sales_summary.pdf") as pdf:
    fig = plt.figure(figsize=(16, 11))
    fig.suptitle(
        "SALES ANALYSIS — EXECUTIVE SUMMARY",
        fontsize=22, fontweight="bold", y=0.97
    )

    fig.text(
        0.5, 0.925,
        "Syntecxhub Data Science Project | Retail Sales Analysis",
        ha="center", fontsize=12
    )

    # KPI cards
    kpis = [
        ("TOTAL SALES", f"R{total_sales:,.2f}"),
        ("AVERAGE PER RECORD", f"R{average_sales:,.2f}"),
        ("QUANTITY SOLD", f"{total_quantity:,}"),
        ("SALES RECORDS", f"{transactions:,}")
    ]

    for i, (label, value) in enumerate(kpis):
        x = 0.06 + i * 0.23
        fig.text(
            x, 0.84, f"{label}\n{value}",
            fontsize=13, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.8", alpha=0.12),
            ha="left", va="center"
        )

    # Chart 1: Regional sales
    ax1 = fig.add_axes([0.07, 0.49, 0.39, 0.25])
    region_sales.plot(kind="barh", ax=ax1)
    ax1.set_title("Sales by Region", fontweight="bold")
    ax1.set_xlabel("Sales Amount (R)")
    ax1.set_ylabel("")
    ax1.ticklabel_format(axis="x", style="plain")
    ax1.grid(axis="x", alpha=0.2)

    # Chart 2: Category sales
    ax2 = fig.add_axes([0.55, 0.49, 0.39, 0.25])
    category_sales.plot(kind="barh", ax=ax2)
    ax2.set_title("Sales by Product Category", fontweight="bold")
    ax2.set_xlabel("Sales Amount (R)")
    ax2.set_ylabel("")
    ax2.ticklabel_format(axis="x", style="plain")
    ax2.grid(axis="x", alpha=0.2)

    # Chart 3: Monthly trend
    ax3 = fig.add_axes([0.10, 0.20, 0.80, 0.20])
    ax3.plot(monthly_sales.index, monthly_sales.values, marker="o")
    ax3.set_title("Monthly Sales Trend", fontweight="bold")
    ax3.set_ylabel("Sales Amount (R)")
    ax3.ticklabel_format(axis="y", style="plain")
    ax3.tick_params(axis="x", rotation=30)
    ax3.grid(axis="y", alpha=0.2)

    # Key findings and recommendations
    findings = (
        f"KEY FINDINGS & RECOMMENDATIONS\n"
        f"• Leading region: {top_region} "
        f"(R{region_sales.max():,.2f} in sales).\n"
        f"• Leading category: {top_category} "
        f"(R{category_sales.max():,.2f} in sales).\n"
        f"• Highest-sales month: {best_month:%B %Y} "
        f"(R{monthly_sales.max():,.2f}).\n"
        f"• Investigate successful practices in the leading region "
        f"and category to identify opportunities for growth.\n"
        f"• January 2024 has only 3 records; verify data completeness "
        f"before comparing it with full months."
    )

    fig.text(
        0.07, 0.055, findings,
        fontsize=10, va="bottom", linespacing=1.5
    )

    fig.text(
        0.07, 0.018,
        "Note: Sales figures use Sales_Amount. Average per record is not "
        "necessarily average order value. Profit has not been calculated.",
        fontsize=8
    )

    pdf.savefig(fig, bbox_inches="tight")
    plt.close(fig)

print("Report exported successfully: sales_summary.pdf")
