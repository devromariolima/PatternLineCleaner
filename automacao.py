import csv

# Abrir os arquivos CSV
with open('%MG_Rev09.csv', 'r', encoding='utf-8') as input_file, open('THM TRANSPORTE E LOGISTICA LTDA.csv', 'w', encoding='utf-8', newline='') as output_file:
    reader = csv.reader(input_file, delimiter=';')
    writer = csv.writer(output_file, delimiter=';')

    # Escrever o cabeçalho
    header = next(reader)
    writer.writerow(header)

    # Filtrar as linhas
    for row in reader:
        if row[-1] != 'THM TRANSPORTE E LOGISTICA LTDA':
            writer.writerow(row)

print("Linhas removidas com sucesso!")
