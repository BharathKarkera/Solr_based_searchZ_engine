import csv 

with open("/Users/bharathraj.karkera/python_test/search_engine/URL_list.txt","r") as read_file_obj:
   with open("/Users/bharathraj.karkera/python_test/Solr_based_searchZ_engine-main/document.csv","w") as write_file_obj:
      csv.writer(write_file_obj,delimiter=',').writerows(csv.reader(read_file_obj,delimiter='|'))
