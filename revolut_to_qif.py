#!/usr/bin/env python3
import csv
import argparse
from pathlib import Path
from datetime import datetime

def convert_csv_to_qif(csv_file, verbose=False):
    """Convert Revolut Business CSV to QIF format"""
    csv_path = Path(csv_file)
    qif_path = csv_path.with_suffix('.qif')
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        if verbose:
            print(f"CSV Headers: {reader.fieldnames}")
            print("-" * 50)
        
        with open(qif_path, 'w', encoding='utf-8') as qif:
            qif.write("!Type:Bank\n")
            
            for row in reader:
                if verbose:
                    print(f"Processing: {row}")
                
                # Parse date (use completed date)
                date_str = row['Date completed (UTC)']
                date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                qif_date = date_obj.strftime('%m/%d/%Y')
                
                # Get amount (use Total amount)
                amount = float(row['Total amount'])
                
                # Get description
                description = row['Description']
                if row['Reference']:
                    description += f" - {row['Reference']}"
                
                # Write QIF transaction
                qif.write(f"D{qif_date}\n")
                qif.write(f"T{amount:.2f}\n")
                qif.write(f"P{description}\n")
                qif.write("^\n")
    
    print(f"Converted {csv_path} to {qif_path}")

def main():
    parser = argparse.ArgumentParser(description='Convert Revolut Business CSV to QIF format')
    parser.add_argument('csv_file', help='Path to the CSV file')
    parser.add_argument('-v', '--verbose', action='store_true', help='Print CSV data for debugging')
    
    args = parser.parse_args()
    convert_csv_to_qif(args.csv_file, args.verbose)

if __name__ == '__main__':
    main()