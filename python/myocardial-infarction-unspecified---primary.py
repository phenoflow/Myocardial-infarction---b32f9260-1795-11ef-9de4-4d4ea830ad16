# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"G301.00","system":"readv2"},{"code":"9507","system":"readv2"},{"code":"59032","system":"readv2"},{"code":"32272","system":"readv2"},{"code":"63467","system":"readv2"},{"code":"55401","system":"readv2"},{"code":"52705","system":"readv2"},{"code":"26972","system":"readv2"},{"code":"32854","system":"readv2"},{"code":"41221","system":"readv2"},{"code":"40429","system":"readv2"},{"code":"68357","system":"readv2"},{"code":"1677","system":"readv2"},{"code":"34803","system":"readv2"},{"code":"12139","system":"readv2"},{"code":"46017","system":"readv2"},{"code":"17872","system":"readv2"},{"code":"46112","system":"readv2"},{"code":"23892","system":"readv2"},{"code":"46276","system":"readv2"},{"code":"13571","system":"readv2"},{"code":"28736","system":"readv2"},{"code":"62626","system":"readv2"},{"code":"29643","system":"readv2"},{"code":"8935","system":"readv2"},{"code":"68748","system":"readv2"},{"code":"30330","system":"readv2"},{"code":"2491","system":"readv2"},{"code":"1678","system":"readv2"},{"code":"7783","system":"readv2"},{"code":"96838","system":"readv2"},{"code":"3704","system":"readv2"},{"code":"26975","system":"readv2"},{"code":"30421","system":"readv2"},{"code":"14897","system":"readv2"},{"code":"241","system":"readv2"},{"code":"14898","system":"readv2"},{"code":"61670","system":"readv2"},{"code":"14658","system":"readv2"},{"code":"41835","system":"readv2"},{"code":"29758","system":"readv2"},{"code":"5387","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('myocardial-infarction-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["myocardial-infarction-unspecified---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["myocardial-infarction-unspecified---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["myocardial-infarction-unspecified---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
