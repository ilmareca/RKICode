import os
import json
import csv
import xml.etree.ElementTree as ET
import logging

# Configurar el logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Directory containing the data
base_dir = '/export/data_ml4ds/bacteria_id/relevant_datasets/10.5281/RKI_ROOT'

# Dictionary to store the aggregated data
data = {}

# Traverse the directory structure and count the samples
logging.info('Starting to traverse the directory structure.')
for genus in sorted(os.listdir(base_dir)):
    genus_dir = os.path.join(base_dir, genus)
    if os.path.isdir(genus_dir):
        logging.info(f'Processing genus: {genus}')
        for species in sorted(os.listdir(genus_dir)):
            species_dir = os.path.join(genus_dir, species)
            if os.path.isdir(species_dir):
                logging.info(f'Processing species: {species}')
                count = 0
                for externId in sorted(os.listdir(species_dir)):
                    externId_dir = os.path.join(species_dir, externId)
                    if os.path.isdir(externId_dir):
                        for targetPosition in sorted(os.listdir(externId_dir)):
                            targetPosition_dir = os.path.join(externId_dir, targetPosition)
                            if os.path.isdir(targetPosition_dir):
                                count += len(os.listdir(targetPosition_dir))
                if genus not in data:
                    data[genus] = {}
                species = species.split()[-1].capitalize()
                data[genus][species] = count
                logging.info(f'Count for {genus} {species}: {count}')

# Create the output XML structure
logging.info('Creating the output XML structure.')
root = ET.Element('Results')
for genus_name in sorted(data.keys()):
    genus_elem = ET.SubElement(root, 'Genus', name=genus_name)
    for species_name in sorted(data[genus_name].keys()):
        species_elem = ET.SubElement(genus_elem, 'Species', name=species_name)
        species_elem.text = str(data[genus_name][species_name])

# Write the output XML to a file
output_file = 'report.xml'
tree = ET.ElementTree(root)
tree.write(output_file, encoding='utf-8', xml_declaration=True)
logging.info(f'XML report written to {output_file}')

# Write the output CSV to a file
csv_file = 'report.csv'
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Genus', 'Species', 'Count'])
    for genus_name in sorted(data.keys()):
        for species_name in sorted(data[genus_name].keys()):
            writer.writerow([genus_name, species_name, data[genus_name][species_name]])
logging.info(f'CSV report written to {csv_file}')

# Write the output JSON to a file
json_file = 'report.json'
with open(json_file, mode='w') as file:
    json.dump(data, file, indent=4, sort_keys=True)
logging.info(f'JSON report written to {json_file}')
