# custom_xml_to_csv
I created this script to extract a few keys from an xml file and put it inside a csv.
You need 4 arguments that are pairs separated by an = sign.
So it would be something like: custom_xml_to_csv.py key0name=key0 key1name=key1 searchname=search rootname=rootname
Where:
- key0 is the first column in the csv
- key1 is the second column in the csv
- search is a sub-key inside key0
- rootname is the desired root inside the xml file as this only works with relatively shallow xml

Maybe I'll change this but for now it did what it needed to do
