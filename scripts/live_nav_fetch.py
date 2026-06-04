import requests
import pandas as pd

amfi_code = "125497"

url = f"https://api.mfapi.in/mf/{amfi_code}"

response = requests.get(url)

data = response.json()

nav_data = pd.DataFrame(data["data"])

nav_data.to_csv(
    "data/raw/hdfc_top100_live_nav.csv",
    index=False
)

print("NAV data saved successfully")