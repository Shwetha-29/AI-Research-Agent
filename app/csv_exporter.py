import csv
import os


def save_to_csv(companies):

    os.makedirs("data", exist_ok=True)

    with open(
        "data/results.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "company",
                "description",
                "source_url"
            ]
        )

        writer.writeheader()

        for company in companies:

            writer.writerow({
                "company": company.get("company", ""),
                "description": company.get("description", ""),
                "source_url": company.get("source_url", "")
            })

    print("\nCSV saved successfully: data/results.csv")