"""
Script to create the required dede elasticsearch index templates
The templates set the creation of a .raw not analyzed field for each string field with less than 256 characters and an alias for each main data index.
The aliases will be used to access the data from a single point of query, as the different services create their own indices.
"""
from elasticsearch import Elasticsearch


#Get ES server IP from config file
config_file = open('deepgrid.conf','r')

for line in config_file:
    if line.startswith('es_server'):
        es_server = line.split(':')[1].strip()

es_server = config_dict.get('es_server')

#Connect to local ES cluster
es = Elasticsearch(es_server, request_timeout=60)

#Index templates configuration
job_data_template = {"order": 0,"template": "dede_job_data*", "settings": {}, "mappings": { "_default_": { "dynamic_templates": [{ "strings": { "mapping": { "type": "string", "fields": { "raw": { "index": "not_analyzed", "ignore_above": 256, "type": "string"}}},"match_mapping_type": "string"}}]}},"aliases": {"dede_job_data": {}}}

job_summary_template = {"order": 0, "template": "dede_job_summary*", "settings": {}, "mappings": {"_default_": {"dynamic_templates": [{"strings": {"mapping": {"type": "string", "fields": {"raw": {"index": "not_analyzed", "ignore_above": 256, "type": "string"}}}, "match_mapping_type": "string"}}]}}, "aliases": {"dede_job_summary": {}}}


job_tracking_template = {"order": 0,"template": "dede_job_tracking*","settings": {},"mappings": {"_default_": {"dynamic_templates": [{"strings": {"mapping": {"type": "string", "fields": {"raw": {"index": "not_analyzed", "ignore_above": 256, "type": "string"}}}, "match_mapping_type": "string"}}]}}, "aliases": {"dede_job_tracking": {}}}

job_matrix_template = {"order": 0,"template": "dede_job_matrix*","settings": {},"mappings": {"_default_": {"dynamic_templates": [{"strings": {"mapping": {"type": "string", "fields": {"raw": {"index": "not_analyzed","ignore_above": 256,"type": "string"}}}, "match_mapping_type": "string"}}]}}, "aliases": {"dede_job_matrix": {}}}

#Create templates
es.indices.put_template(name="dede_job_data", body=job_data_template)
es.indices.put_template(name="dede_job_summary", body=job_summary_template)
es.indices.put_template(name="dede_job_data", body=job_tracking_template)
es.indices.put_template(name="dede_job_data", body=job_matrix_template)