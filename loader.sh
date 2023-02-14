#! /bin/bash 

curl -vi "http://localhost:8983/solr/admin/cores?action=UNLOAD&deleteInstanceDir=true&core=search_engine_collection"


/usr/local/bin/python3 << EOF 

import csv 

with open("/Users/bharathraj.karkera/python_test/Solr_based_searchZ_engine-main/document.txt","r") as read_file_obj:
   with open("/Users/bharathraj.karkera/python_test/Solr_based_searchZ_engine-main/document.csv","w") as write_file_obj:
      csv.writer(write_file_obj,delimiter=',').writerows(csv.reader(read_file_obj,delimiter='|'))

EOF

solr create -c search_engine_collection -p 8983

curl -i 'http://localhost:8983/solr/search_engine_collection/update?commit=true' --data-binary @/Users/bharathraj.karkera/python_test/Solr_based_searchZ_engine-main/document.csv -H 'Content-type:application/csv'
