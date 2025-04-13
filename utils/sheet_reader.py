import pandas as pd


def read_sheet(filepath, material):
    if filepath.endswith('.xlsx'):
        df = pd.read_excel(filepath)
    else:
        df = pd.read_csv(filepath)
    material = material.lower()
    filtered = df[df['Product'].str.contains(material, case=False, na=False) |
                  df['Description'].str.contains(
                      material, case=False, na=False)]
    results = [
        {
            'company': row.get('Company', 'N/A'),
            'product': row.get('Product', 'N/A'),
            'email': row.get('Email', 'N/A')
        }
        for _, row in filtered.iterrows()
    ]

    return results
