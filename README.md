# python-revolut-business-csv-to-freeagent

Converts Revolut Business CSV exports to QIF format for importing into FreeAgent.

## Usage

```bash
python revolut_to_qif.py <csv_file> [-v]
```

- `<csv_file>`: Path to your Revolut Business CSV export
- `-v, --verbose`: Optional flag to print CSV data during processing for debugging

The QIF file will be created in the same directory as the input CSV.

## Example

```bash
python revolut_to_qif.py sample-data/transaction-statement_01-Jun-2025_30-Jun-2025.csv -v
```