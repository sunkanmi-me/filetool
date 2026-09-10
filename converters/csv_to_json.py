import csv
import json


def csv_to_json(input_file, output_file):

    # Read the CSV file
    with open(
        input_file,
        newline="",
        encoding="utf-8"
    ) as csv_file:

        reader = csv.DictReader(csv_file)

        rows = list(reader)

    # Write the JSON file
    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as json_file:

        json.dump(
            rows,
            json_file,
            indent=4
        )