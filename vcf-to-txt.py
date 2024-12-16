import os
from datetime import datetime

def vcf_to_txt(vcf_file, txt_file):
    try:
        with open(vcf_file, 'r') as vcf, open(txt_file, 'w') as txt:
            contacts = []  # List to store all contacts
            contact = {}

            for line in vcf:
                line = line.strip()
                if line.startswith("BEGIN:VCARD"):
                    contact = {}
                elif line.startswith("FN:"):
                    contact['Name'] = line[3:]
                elif line.startswith("TEL;"):
                    number_type = line.split(':')[0].split('=')[-1].strip()
                    number = line.split(':')[1].strip()
                    if 'Phone Numbers' not in contact:
                        contact['Phone Numbers'] = []
                    contact['Phone Numbers'].append(f"({number_type}) {number}")
                elif line.startswith("EMAIL:"):
                    contact['Email'] = line[6:]
                elif line.startswith("COUNTRYISO:"):
                    contact['Country'] = line.split(":")[1].strip()
                elif line.startswith("X-OPPO-MODIFY-DATE:"):
                    # Convert timestamp to a human-readable date
                    timestamp = int(line.split(":")[1].strip())
                    contact['Last Modified'] = datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M')
                elif line.startswith("X-OPPO-STARRED:"):
                    contact['Starred'] = 'Yes' if line.split(":")[1].strip() == '1' else 'No'
                elif line.startswith("OPPO_RECENT_CALL:"):
                    call_data = line.split(":")[1].strip()
                    contact['Last Call'] = call_data if call_data != "NULL" else None
                elif line.startswith("END:VCARD"):
                    # Append the contact to the contacts list
                    contacts.append(contact)
                    contact = {}

            # Sort contacts by Name in ascending order
            contacts.sort(key=lambda x: x.get('Name', '').lower())

            # Write sorted contacts to the text file
            for contact in contacts:
                txt.write(f"Name: {contact.get('Name', 'N/A')}\n")
                
                if 'Phone Numbers' in contact:
                    txt.write(f"Phone Numbers: {', '.join(contact['Phone Numbers'])}\n")
                else:
                    txt.write(f"Phone Numbers: N/A\n")
                
                # Only write the Email field if it is present
                if 'Email' in contact:
                    txt.write(f"Email: {contact['Email']}\n")
                
                # Write Country if available
                if 'Country' in contact:
                    txt.write(f"Country: {contact['Country']}\n")

                # Write Last Modified if available
                if 'Last Modified' in contact:
                    txt.write(f"Last Modified: {contact['Last Modified']}\n")

                # Write Starred status if available
                if 'Starred' in contact:
                    txt.write(f"Starred: {contact['Starred']}\n")

                # Only write Last Call if there is a valid value
                if 'Last Call' in contact and contact['Last Call']:
                    txt.write(f"Last Call: {contact['Last Call']}\n")
                
                txt.write("\n")  # This adds a newline after each contact

    except Exception as e:
        print(f"Error: {e}")

def process_vcf_files_in_directory(directory):
    # Scan the directory for .vcf files
    vcf_files = [f for f in os.listdir(directory) if f.endswith('.vcf')]
    
    if not vcf_files:
        print("No VCF files found in the directory.")
        return

    for vcf_file in vcf_files:
        txt_file = vcf_file.replace('.vcf', '_TextFile.txt')  # Automatically create output filename
        print(f"Processing {vcf_file}...")
        vcf_to_txt(vcf_file, txt_file)
        print(f"Contacts successfully saved to {txt_file}")

if __name__ == "__main__":
    # Automatically process all .vcf files in the current directory
    process_vcf_files_in_directory(os.getcwd())
