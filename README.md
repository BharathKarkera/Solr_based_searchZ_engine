# Solr_based_searchZ_engine


```
 3:08PM @Bharath  ~ which -a python3
python3: aliased to /usr/local/bin/python3
/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
/usr/local/bin/python3
/usr/bin/python3
/opt/brew/bin/python3
```

Run below command to start the app:

```
sudo gunicorn --python /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages --workers 1 --bind localhost:80 --chdir ~/practice/python/search_engine2 app:app --access-logfile '-'
```


```
curl -i "http://bharathkarkera:80/search" -d "search_parameter=MDN"
```
