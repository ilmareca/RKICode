# Bacteria Sample Count Project

This project processes a dataset of bacteria samples and generates reports in CSV, JSON, and XML formats.

## Directory Structure

- `.gitattributes`: Git attributes configuration.
- `count_samples.py`: Python script to process the data and generate reports.
- `README.md`: This file.
- `report.csv`: Generated report in CSV format.
- `report.json`: Generated report in JSON format.
- `report.xml`: Generated report in XML format.

## File Descriptions

### `count_samples.py`

This script traverses the directory structure containing the bacteria sample data, counts the samples, and generates reports in three different formats: CSV, JSON, and XML.

### `report.csv`

This file contains the sample report in CSV format. Each line represents a sample in the format `Genus,Species,Count`.

### `report.json`

This file contains the sample report in JSON format. The structure is a dictionary where the keys are the genera and the values are dictionaries with the species and their respective counts.

### `report.xml`

This file contains the sample report in XML format. The structure is an XML tree where each genus is a node containing child nodes for each species with their respective counts.

## Running the Script

To run the script and generate the reports, simply execute the following command in your terminal:

```sh
python count_samples.py
```

## Example Usage

Below is an example of a portion of the `report.json` file:

```json
{
    "Streptococcus": {
        "Agalactiae": 8,
        "Dysgalactiae": 12,
        "Mitis": 4,
        "Parasanguinis": 12,
        "Pneumoniae": 24,
        "Pyogenes": 30,
        "Salivarius": 35,
        "Sanguinis": 8
    },
    "Sutcliffiella": {
        "Cohnii": 36
    },
    "Vibrio": {
        "Alginolyticus": 12,
        "Cholerae": 218,
        "Diazotrophicus": 4,
        "Harveyi": 11
    }
}
```