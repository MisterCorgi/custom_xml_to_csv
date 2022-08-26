import xml.etree.ElementTree as Xet
import pandas as pd
import sys
#### This xml_to_csv utility extracts selected pairs of keys from xml
#### The tool is a bit more specialized than the standard xml to csv tool

def main(*args):
    key0 = args[0][1]
    key0n = args[0][0]
    key1 = args[1][1]
    key1n = args[1][0] 
    search = args[2][1] # FIND search INSIDE key0 AND MATCH WITH key1
    if(args[3][0] == "rootname"):
        rootname=args[3][1]
    else:
        exit()
    cols = [key0n, key1n]
    rows = []

    # We need to extract: key0, search
    # Match the name with key1
    xmlparse = Xet.parse('sample.xml')
    root = xmlparse.getroot()

    for entry in root.find(rootname):
        first_key = entry[2].find(key0).find(search).text
        second_key = [key[0].text for key in entry[3]]
        for keys in second_key:
            rows.append({
                        key0n: int(keys),
                        key1n: first_key
                        })

    df = pd.DataFrame(rows, columns=cols)
    
    # Writing dataframe to csv
    df.to_csv('output.csv', index=False)



if __name__=="__main__":
    args = [arg.split('=') for arg in sys.argv[1:]]
    # args = sys.argv[1:]
    main(*args) 