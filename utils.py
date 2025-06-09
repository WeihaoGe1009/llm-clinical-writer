import pandas as pd
import json

def excel_to_json(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file)
        data = {}
        extras = {}

        for col in df.columns:
            key = col.strip().lower().replace(" ", "_")
            value = df.iloc[0][col]

            if key in ["design", "arms", "allocation", "blinding", "duration"]:
                data[key] = value
            else:
                extras[key] = value

        if extras:
            data["extras"] = extras

        return data
    except Exception as e:
        return {"error": str(e)}

