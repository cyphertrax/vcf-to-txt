# VCF to TXT Converter

This Python script allows you to convert `.vcf` (vCard) contact files into readable `.txt` format. It automatically processes all `.vcf` files in the current directory and generates `.txt` files containing the contact information in a well-structured format.

## Features

- Processes `.vcf` files in the current directory.
- Extracts relevant contact information such as:
  - Name
  - Phone Numbers
  - Email
  - Country
  - Last Modified Date
  - Starred status
  - Last Call (if available)
- Outputs the contact information into `.txt` files.
- Sorted by contact name in ascending order.

## Prerequisites

This script requires Python 3.x. You don't need to install any additional packages as it uses built-in Python libraries.

## How to Use

1. Download or clone this repository.
2. Place your `.vcf` files in the same directory as the script.
3. Run the script by executing the following command in your terminal:

   ```bash
   python vcf_to_txt.py
