import pandas as pd


def main():
    try:
        # read in the output data from the shapefile
        df = pd.read_csv("output.csv", low_memory=False)
    except FileNotFoundError:
        raise SystemExit("Error: file output.csv not found")

    df = df[["TAXPINNO", "latitude", "longitude"]]

    try:
        # read housing condition survey (HCS) data
        hcs = pd.read_csv("housing_survey2023.csv", low_memory=False)
    except FileNotFoundError:
        raise SystemExit("Error: file housing_survey2023.csv not found")

    # add latitude and longitude to HCS data
    hcs = pd.merge(df, hcs, on="TAXPINNO", how="right")

    hcs.to_csv("hcs_and_centroids.csv", index=False)


if __name__ == "__main__":
    main()
