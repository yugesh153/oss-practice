import argparse
from tabulate import tabulate

parser = argparse.ArgumentParser()
parser.add_argument("--name", default="World")
args = parser.parse_args()

rows = [
    ["Developer", args.name],
    ["Tool Used", "tabulate"],
    ["Status", "Complete"]
]
headers = ["Metric", "Value"]

print("--- OSS Tool Report ---")
print(tabulate(rows, headers=headers, tablefmt="grid"))
