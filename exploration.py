import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv("dCRDC2013_14.csv", encoding="Latin-1")
    
    count_JJ = data["JJ"].value_counts()
    count_magnet = data["SCH_STATUS_MAGNET"].value_counts()
    
    table_JJ = pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="JJ", aggfunc="sum")
    table_magnet = pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="SCH_STATUS_MAGNET", aggfunc="sum")
    
    print(count_JJ)
    print(count_magnet)
    print(table_JJ)
    print(table_magnet)