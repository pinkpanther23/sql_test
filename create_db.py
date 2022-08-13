import re
import os
import sqlite3

con = sqlite3.connect('test.db')

cur = con.cursor()

sample_table = ''' CREATE TABLE Samples (
                    CD_num varchar(255) NOT NULL,
                    Mutation_status varchar(255),
                    Run_num varchar(255) NOT NULL,
                    PG_num varchar(255),
                    DNA_num varchar(255),
                    DNA_barcode int,
                    RNA_num varchar(255),
                    RNA_barcode int,
                    Receive_date DATE,
                    Result_date DATE,
                    Fusion_status varchar(255),
                    Panel varchar(255),
                    Sample_type varchar(255),
                    CONSTRAINT PK_Samples PRIMARY KEY (CD_num)
                    ); '''

variant_table = '''CREATE TABLE Variants (
                    CD_num varchar(255) NOT NULL,
                    Variant_num int,
                    Locus varchar(255),
                    Genotype varchar(255),
                    Ref varchar(255),
                    Obs varchar(255),
                    Type varchar(255),
                    Gene varchar(255),
                    Exon int,
                    Length int,
                    Variant_class varchar(255),
                    Gene_class varchar(255),
                    Coverage int,
                    Freq float(8),
                    Coding varchar(765),
                    AA_change varchar(765),
                    Transcript varchar(255),
                    Variant_effect varchar(255),
                    Variant_ID varchar(255),
                    Read_count int,
                    CONSTRAINT PK_Variants PRIMARY KEY (Variant_num),
                    CONSTRAINT FK_VariantsSamples FOREIGN KEY (CD_num) REFERENCES Samples(CD_num)
                    );'''

OKR_table = '''CREATE TABLE OKR (
                    CD_num varchar(255) NOT NULL,
                    OKR_num int,
		    Gene varchar(255),
                    Variant varchar(255),
                    Tier_AML varchar(255),
		    Tier_CML varchar(255),
		    Tier_MDS varchar(255),
                    Coverage int,
                    Freq float(8),
                    Coding varchar(765),
                    AA_change varchar(765),
                    Transcript varchar(255),
                    Variant_effect varchar(255),
                    Variant_ID varchar(255),
                    Read_count int,
                    CONSTRAINT PK_Variants PRIMARY KEY (Variant_num),
                    CONSTRAINT FK_VariantsSamples FOREIGN KEY (CD_num) REFERENCES Samples(CD_num)
                    );'''

cur.execute(sample_table)
cur.execute(variant_table)

con.commit()
con.close()