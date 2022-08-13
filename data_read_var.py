import re
import os
import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()

data_file = open("database.txt", "r")
data_lines = data_file.readlines()

#sample_table = []
variant_table = []


def listToString(my_list):
    string_output = "\t".join([str(i) for i in my_list])
    return string_output


def checkList(value, my_list):
    for i in my_list:
        if value in i:
            return True
    return False

var_count = 0

for line in data_lines:
    data = line.split("\t")
    mutation_status = data[12]

    #sample_table_list = []
    variant_table_list = []

    if (mutation_status != "Negative"):
        var_count = var_count + 1
        sample_table_list = [data[2], "Positive", data[1], data[3], data[5], data[4], data[7], data[6], data[10],
                             data[11], data[0], data[8], data[9]]
        variant_table_list = [data[2], var_count, data[12], data[13], data[14], data[15], data[16], data[17], data[18], data[19],
                              data[20], data[21], data[22], data[23], data[24], data[25], data[26], data[27], data[28],
                              data[29]]
        # sql_samples = "INSERT INTO Samples (CD_num, Mutation_Status, Run_num, PG_num, DNA_num, DNA_barcode, RNA_num, RNA_barcode, Receive_date, Result_date, Fusion_status, Panel, Sample_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
        # cur.execute(sql_samples, tuple(sample_table_list))
        # con.commit()
        #sample_table.append(sample_table_list)
        variant_table.append(variant_table_list)
    else:
        sample_table_list = [data[2], "Negative", data[1], data[3], data[5], data[4], data[7], data[6], data[10],
                             data[11], data[0], data[8], data[9]]

        # sql_samples = "INSERT INTO Samples (CD_num, Mutation_Status, Run_num, PG_num, DNA_num, DNA_barcode, RNA_num, RNA_barcode, Receive_date, Result_date, Fusion_status, Panel, Sample_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
        # cur.execute(sql_samples, tuple(sample_table_list))
        # con.commit()
        #sample_table.append(sample_table_list)

    #sample_table.append(sample_table_list)
    #variant_table.append(variant_table_list)
# con.close()
# sample_file = open("samples.txt", "w")
# variant_file = open("variants.txt", "w")

#updated_sample_list = [sample_table[0]]

#for i in sample_table:
    #value = i[0]
    #if (checkList(value, updated_sample_list) == False):
        #updated_sample_list.append(i.copy())

count = 0
for i in variant_table:
    print("working on case " + str(count))
    count = count + 1
    sql_variants = "INSERT INTO Variants (CD_num, Variant_num, Locus, Genotype, Ref, Obs, Type, Gene, Exon, Length, Variant_class, Gene_class, Coverage, Freq, Coding, AA_change, Transcript, Variant_effect, Variant_ID, Read_count) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
    cur.execute(sql_variants, tuple(i))
    con.commit()

#count = 0
#for i in updated_sample_list:
    #print("working on case " + str(count))
    #count = count + 1
    #sql_samples = "INSERT INTO Samples (CD_num, Mutation_Status, Run_num, PG_num, DNA_num, DNA_barcode, RNA_num, RNA_barcode, Receive_date, Result_date, Fusion_status, Panel, Sample_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
    #cur.execute(sql_samples, tuple(i))
    #con.commit()

con.close()

# for i in sample_table:
# output = listToString(i)
# sample_file.write(output + "\n")

# for i in variant_table:
# output = listToString(i)
# variant_file.write(output + "\n")

# sample_file.close()
# variant_file.close()
# data_file.close()
