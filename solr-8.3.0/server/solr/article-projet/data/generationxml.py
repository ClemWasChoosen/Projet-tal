import os
import csv

# Permet de creer le dossier pour indexer les fichiers
temp_folder = 'temp_files'
if not os.path.exists(temp_folder):
    os.makedirs(temp_folder)

# Compteur pour le nom des fichiers
file_counter = 1

with open('train.tsv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t')
    for row in reader:
        category = row['category']
        headline = row['headline']
        text = row['text']
        url = row['url']

        temp_file_name = os.path.join(temp_folder, f'temp{file_counter:05d}.xml')

        # Creation des fichiers temporaires de la forme tempXXXXX.xml
        with open(temp_file_name, 'w', encoding='utf-8') as xmlfile:
            xmlfile.write(f'<add>\n')
            xmlfile.write(f'  <doc>\n')
            xmlfile.write(f'    <field name="category">{category}</field>\n')
            xmlfile.write(f'    <field name="headline">{headline}</field>\n')
            xmlfile.write(f'    <field name="text">{text}</field>\n')
            xmlfile.write(f'    <field name="url">{url}</field>\n')
            # Ajouter d'autres champs si nécessaire
            xmlfile.write(f'  </doc>\n')
            xmlfile.write(f'</add>\n')

        file_counter += 1


