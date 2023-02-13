import flask
import subprocess
import redis
import pysolr
import pprint
import json
import flask_cors

app=flask.Flask(__name__)
app.config["DEBUG"]=True
app.config["TOKEN"]="bharathkarkera"
app.secret_key = 'bharathkarkera'
app.config['CORS_HEADERS'] = 'Content-Type'

redis=redis.Redis(host='localhost',port=6379)

@app.route('/',methods=["GET"])
def index_fun():
    flask.flash("Search for a site...")
    return flask.render_template("index.html")


@app.route("/search", methods=["POST","GET"])
def greet():
    redis.incr("hits")
    first_part='unset GREP_OPTIONS ; unset GREP_COLOR ; cat /Users/bharathkarkera/practice/python/search_engine2/URL_list.txt |grep -i "'
    sec_part=flask.request.form['search_parameter']
    #sec_part=flask.request.form['search-box']
    third_part='" |sed G > /Users/bharathkarkera/practice/python/search_engine2/raw_result.txt'
    args = first_part+sec_part+third_part
    print(args)
    result=subprocess.run(args,capture_output=True, shell=True)

    args ='/bin/bash /Users/bharathkarkera/practice/python/search_engine2/html_former.sh'
    result=subprocess.run(args,capture_output=True, shell=True)

    flask.flash("Showing results for : "+str(flask.request.form['search_parameter'])+"(  "+str(int(redis.get("hits")))+"th hit to the site !  )")
    return  flask.render_template("test.html"),{"Refresh":"10; url=http://localhost:80"}

@flask_cors.cross_origin(origin='*',headers=['access-control-allow-origin','Content-Type'])
@app.route("/autopopulate",methods=["GET","POST"])
def auto_populate_fun():
    query=flask.request.args["q"].lower()
    print(f"query for autocomplete: {query}")
    search_engine_collection=pysolr.Solr("http://localhost:8983/solr/search_engine_collection")
    q=f"name:*{query}* OR URL:*{query}*"
    rows=10
    filtered_results=search_engine_collection.search(q,**{'rows':rows})
    pprint.pprint(filtered_results.docs)

    name_list=[]
    for i in filtered_results.docs:
        name_list.append(str(i['name'][0]))

    print(json.dumps(name_list))
    return json.dumps(name_list)



#app.run(host="0.0.0.0")
#cat URL_list.txt | sed 's/-->/~/g' | cut -d '~' -f 1|sed -E '/^$/d' | sed -E 's/^(.*) $/"\1"/g' | tr '\n' ','
#cat URL_list.txt| sed 's/-->/|/g' | tr -d ' ' > document.txt
#with open("/Users/bharathkarkera/practice/python/search_engine2/document.txt","r") as read_file_obj:
#   with open("/Users/bharathkarkera/practice/python/search_engine2/document.csv","w") as write_file_obj:
#      csv.writer(write_file_obj,delimiter=',').writerows(csv.reader(read_file_obj,delimiter='|'))
#solr create -c search_engine_collection -p 8983
#curl -i 'http://localhost:8983/solr/search_engine_collection/update?commit=true' --data-binary @/Users/bharathkarkera/practice/python/search_engine2/document.csv -H 'Content-type:application/csv'
#search_engine_collection=pysolr.Solr("http://localhost:8983/solr/search_engine_collection")
#all_results=search_engine_collection.search("*:*")
#pprint.pprint(all_results.docs)
#curl -vi "http://localhost:8983/solr/admin/cores?action=UNLOAD&deleteInstanceDir=true&core=search_engine_collection"
#query="apple"
#q=f"name:*{query}* OR URL:*{query}*"
#rows=10
#filtered_results=search_engine_collection.search(q,**{'rows':rows})
#pprint.pprint(filtered_results.docs)
#curl -i "http://bharathkarkera:80/autopopulate?q=git
# curl -i "http://bharathkarkera:80/search" -d "search_parameter=MDN"
