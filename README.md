# Dayton Housing Condition Survey

Add latitudes and longitudes for properties listed in the Dayton Housing
Condition Survey for future geocoding and analysis.

## Setup

1. Download the Dayton Housing Condition Survey from the [survey website](https://dayton-housing-condition-survey-daytonohio.hub.arcgis.com/).  Click on the "Explore Table" button under
"Dayton Housing Condition Survey Table".  To download a CSV file, follow
the directions by clicking on "..." at the top right of the view and select
"Download source data".  Change the file name to "housing_survey2023.csv"
2. Using the [Code for Dayton Geocoder](https://github.com/codefordayton/geocoder/tree/main) repository, generate "output.csv"
with the command `python process_shapefile.py`{.bash} as described in
the [README file](https://github.com/codefordayton/geocoder/blob/main/README.md).
3. If you do not have [uv](https://docs.astral.sh/uv/getting-started/installation/) installed, create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```
and install the required package:
```bash
pip install pandas
```

## Usage

If you have [uv](https://docs.astral.sh/uv/getting-started/installation/) installed:
```bash
uv run --with pandas python main.py
```

If you do not have uv installed:
```bash
python main.py
```
This will produce a CSV file "hcs_and_centroids.csv".
