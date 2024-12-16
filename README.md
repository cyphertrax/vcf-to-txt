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
   
     ```bash
   https://github.com/cyphertrax/vcf-to-txt.git
2. Place your `.vcf` files in the same directory as the script.
3. Run the script by executing the following command in your terminal:

   ```bash
   python vcf-to-txt.py
4.The script will automatically generate .txt files for each .vcf file found in the directory. Each .txt file will contain the contact details extracted from the corresponding .vcf file.

Example: If you have contact.vcf, the script will generate contact_output.txt.

##Input 
BEGIN:VCARD
VERSION:2.1
FN:Aman
TEL;CELL:+919202928394
EMAIL:aman@example.com
COUNTRYISO:IN
END:VCARD


##Output
Name: Aman
Phone Numbers: (CELL) +919202928394
Email: aman@example.com
Country: IN
Last Modified: 2023-10-17 14:27
