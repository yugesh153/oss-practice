import argparse
import pandas as pd
from rich.console import Console
from rich.table import Table

parser = argparse.ArgumentParser(description="Filter a CSV file and save the result.")
parser.add_argument("csv_path", help="path to the CSV file")
args = parser.parse_args()

df = pd.read_csv(args.csv_path)
# Filter servers where CPU usage is greater than 50
result = df[df["cpu"] > 50]

table = Table(title=f"{len(result)} rows from {args.csv_path}")
for col in result.columns:
    table.add_column(col)
for row in result.itertuples(index=False):
    table.add_row(*[str(value) for value in row])
Console().print(table)

result.to_excel("result.xlsx", index=False)
print("Saved result.xlsx")