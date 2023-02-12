# Solr_based_searchZ_engine

Run below command to start the app:

sudo gunicorn --python /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages --workers 1 --bind localhost:80 --chdir ~/practice/python/search_engine2 app:app --access-logfile '-'
