import os
import sys
import re
import pprint
import numpy as np
import pickle
from tqdm import tqdm

"""
"""
def main(BioGrid_tsv,subset):
    tsv2LL(BioGrid_tsv,subset)






def reading(name):
    with open(name, 'r') as F:
        ob_from_file = eval(F.read())
    F.close()
    return ob_from_file


def LL2csv(LL,name):
    with open(name,"w") as F:
        for L in LL:
            F.write("%s\n" %  (",").join( [str(i) for i in L]))
    F.close()

def tsv2LL(name,organism):
    D = {"ij":{}}
    methods = []
    with open(name,"r") as F:
        for line in tqdm(F):
            cols = line.split("\n")[0].split("\t")
            #print cols[15],cols[16]
            """
            0 #BioGRID Interaction ID
            1 Entrez Gene Interactor A
            2 Entrez Gene Interactor B
            3 BioGRID ID Interactor A
            4 BioGRID ID Interactor B
            5 Systematic Name Interactor A
            6 Systematic Name Interactor B
            7 Official Symbol Interactor A
            8 Official Symbol Interactor B
            9 Synonyms Interactor A
            10 Synonyms Interactor B
            11 Experimental System
            12 Experimental System Type
            13 Author
            14 Pubmed ID
            15 Organism Interactor A
            16 Organism Interactor B
            17 Throughput
            18 Score
            19 Modification
            20 Phenotypes
            21 Qualifications
            22 Tags
            23 Source Database
            """
            if organism == "Hs":
                if cols[15] == '9606':
                    if cols[16] == '9606':
                        if cols[12] == "physical":
                            bait = cols[1]
                            prey = cols[2]
                            method = cols[11]
                            methods.append(method)
                            try:
                                D["ij"][bait][prey][method] +=1
                            except KeyError:
                                try:
                                    D["ij"][bait][prey][method] = 1
                                except KeyError:
                                    try:
                                        D["ij"][bait][prey] = {}
                                        D["ij"][bait][prey][method] = 1
                                    except KeyError:
                                        D["ij"][bait] = {}
                                        D["ij"][bait][prey] = {}
                                        D["ij"][bait][prey][method] = 1
                                        #print bait,prey,method
            if organism == "Sc":
                if cols[12] == "physical":
                    if cols[15] == '559292':
                        if cols[16] == '559292':

                            bait = cols[7]
                            prey = cols[8]
                            method = cols[11]
                            methods.append(method)
                            try:
                                D["ij"][bait][prey][method] +=1
                            except KeyError:
                                try:
                                    D["ij"][bait][prey][method] = 1
                                except KeyError:
                                    try:
                                        D["ij"][bait][prey] = {}
                                        D["ij"][bait][prey][method] = 1
                                    except KeyError:
                                        D["ij"][bait] = {}
                                        D["ij"][bait][prey] = {}
                                        D["ij"][bait][prey][method] = 1
                                        #print bait,prey,method




        pprint.pprint(D)
        #pprint.pprint(list(set(methods)))
        F.close()








if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])
