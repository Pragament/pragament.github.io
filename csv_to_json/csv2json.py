import argparse
import csv
import json
import sys
from pathlib import Path

def csv_to_json(csv_path: Path, json_path: Path) -> None:
    """Convert a CSV file to JSON.

    Reads the CSV file assuming the first row contains headers and writes a JSON
    file containing a list of objects, each object representing a row.
    """
    if not csv_path.is_file():
        sys.stderr.write(f"Error: CSV file '{csv_path}' does not exist.\n")
        sys.exit(1)
    try:
        with csv_path.open(newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)
    except Exception as e:
        sys.stderr.write(f"Failed to read CSV: {e}\n")
        sys.exit(1)
    try:
        with json_path.open('w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4, ensure_ascii=False)
    except Exception as e:
        sys.stderr.write(f"Failed to write JSON: {e}\n")
        sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert one or more CSV files to a single JSON file.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "csv_files",
        type=Path,
        nargs="+",
        help="Path(s) to input CSV file(s).",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Path for the output JSON file. If omitted, the JSON file will be created next to the first CSV with the same base name.",
    )
    args = parser.parse_args()

    # Mapping from original CSV columns to desired JSON keys
    SELECTED_COLUMNS = {
        "Email Address": "Email",
        "Name": "Name",
        "Your GitHub account name/ID? If you do not have a GitHub account, type N/A.": "GitHub",
        "Your LinkedIn profile URL. If you do not have a LinkedIn profile, type N/A.": "LinkedIn",
        "Academic year end date": "AcademicYearEnd",
        "Which job/internship(s) are you interested in?": "Role",
    }

    # Aggregate rows by Name, merging email addresses
    aggregated = {}
    for csv_path in args.csv_files:
        if not csv_path.is_file():
            sys.stderr.write(f"Error: CSV file '{csv_path}' does not exist.\n")
            sys.exit(1)
        try:
            with csv_path.open(newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    name = row.get("Name", "").strip()
                    if not name:
                        continue
                    email_raw = row.get("Email Address", "")
                    emails = [e.strip() for e in email_raw.split(",") if e.strip()]
                    entry = aggregated.get(name, {
                        "Email": "",
                        "Name": name,
                        "GitHub": "",
                        "LinkedIn": "",
                        "AcademicYearEnd": "",
                        "Role": "",
                    })
                    # Merge emails, ensure uniqueness
                    existing_emails = set(e.strip() for e in entry["Email"].split(",") if e.strip())
                    existing_emails.update(emails)
                    entry["Email"] = ",".join(sorted(existing_emails))
                    # Fill other fields if they are empty
                    for src, dst in SELECTED_COLUMNS.items():
                        if dst in ["Email", "Name"]:
                            continue
                        if not entry[dst]:
                            entry[dst] = row.get(src, "").strip()
                    aggregated[name] = entry
        except Exception as e:
            sys.stderr.write(f"Failed to read CSV '{csv_path}': {e}\n")
            sys.exit(1)

    # Convert aggregation dict to list for JSON output
    output_data = list(aggregated.values())

    json_path = args.output
    if json_path is None:
        json_path = args.csv_files[0].with_suffix('.json')

    try:
        with json_path.open('w', encoding='utf-8') as jsonfile:
            json.dump(output_data, jsonfile, indent=4, ensure_ascii=False)
        print(f"Successfully converted {len(args.csv_files)} CSV file(s) to '{json_path}'.")
    except Exception as e:
        sys.stderr.write(f"Failed to write JSON: {e}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
