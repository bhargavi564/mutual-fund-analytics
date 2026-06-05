#SCRIPT
 
import requests
import pandas as pd

funds = {
    "SBI_Bluechip":119551,
    "ICICI_Bluechip":120503,
    "Nippon_LargeCap":118632,
    "Axis_Bluechip":119092,
    "Kotak_Bluechip":120841
}

for fund_name, code in funds.items():
    print(f"Fetching data for {fund_name}...")

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame(data["data"])

    df.to_csv(
        f"data/raw/{fund_name}.csv",
        index=False
    )

    print(f"{fund_name} saved successfully")
 
 
#Fund Master Exploration     
#Analysis performed

fund_master = pd.read_csv(
    "data/raw/fund_master.csv"
)

print("Fund Houses")
print(fund_master["fund_house"].unique())

print("Categories")
print(fund_master["category"].unique())

print("Sub Categories")
print(fund_master["subcategory"].unique())

print("Risk Grades")
print(fund_master["risk_grade"].unique())


#Validation Script

fund_master_codes = set(
    fund_master["amfi_code"]
)

nav_history_codes = set(
    nav_history["amfi_code"]
)

missing_codes = fund_master_codes - nav_history_codes

print("Missing Codes:", len(missing_codes))

print(missing_codes)
