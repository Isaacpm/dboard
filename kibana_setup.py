"""
Script to create the required dede kibana index patterns
The index patterns used the main aliases created by each index at creation time.
Kibana must be installed before running the script
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

#Prepare index pattern bodies

job_matrix = {
          "title": "confusion_matrix",
          "fields": '[{"name":"department_output","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"_source","type":"_source","count":0,"scripted":false,"indexed":false,"analyzed":false,"doc_values":false},{"name":"layers","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"service_name","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":true,"doc_values":false},{"name":"round_number","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":true,"doc_values":false},{"name":"solver_type.raw","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"solver_type","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":true,"doc_values":false},{"name":"total_iterations","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"description","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":true,"doc_values":false},{"name":"department_name","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":true,"doc_values":false},{"name":"round_number.raw","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"service_name.raw","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"base_lr","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"description.raw","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"_index","type":"string","count":0,"scripted":false,"indexed":false,"analyzed":false,"doc_values":false},{"name":"department_name.raw","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"running_time","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"_id","type":"string","count":0,"scripted":false,"indexed":false,"analyzed":false,"doc_values":false},{"name":"_type","type":"string","count":0,"scripted":false,"indexed":false,"analyzed":false,"doc_values":false},{"name":"_score","type":"number","count":0,"scripted":false,"indexed":false,"analyzed":false,"doc_values":false}]'
      }

      }

job_data_tracking_pattern = {
          "title": "job_tracking",
          "fields": '[{"name":"_source","type":"_source","count":0,"scripted":false,"indexed":false,"analyzed":false,"doc_values":false},{"name":"test_split","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"layers","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"service_name","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":true,"doc_values":false},{"name":"accp","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"iteration","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"mcll","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"solver_type","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":true,"doc_values":false},{"name":"solver_type.raw","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"total_iterations","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"description","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":true,"doc_values":false},{"name":"f1","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"min_count","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"activation","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":true,"doc_values":false},{"name":"template","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":true,"doc_values":false},{"name":"service_name.raw","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"precision","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"base_lr","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"description.raw","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"_index","type":"string","count":0,"scripted":false,"indexed":false,"analyzed":false,"doc_values":false},{"name":"batch_size","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"template.raw","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"test_interval","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"activation.raw","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"train_loss","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"min_word_length","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"recall","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"running_time","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"_id","type":"string","count":0,"scripted":false,"indexed":false,"analyzed":false,"doc_values":false},{"name":"_type","type":"string","count":0,"scripted":false,"indexed":false,"analyzed":false,"doc_values":false},{"name":"_score","type":"number","count":0,"scripted":false,"indexed":false,"analyzed":false,"doc_values":false}]'
      }

job_data_pattern = {
          "title": "job_data",
          "fields": '[{"name":"train_loss.raw","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"_source","type":"_source","count":0,"scripted":false,"indexed":false,"analyzed":false,"doc_values":false},{"name":"test_split","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"layers","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"service_name","type":"string","count":1,"scripted":false,"indexed":true,"analyzed":true,"doc_values":false},{"name":"accp","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"iteration","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"mcll","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"solver_type","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":true,"doc_values":false},{"name":"solver_type.raw","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"total_iterations","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"description","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":true,"doc_values":false},{"name":"f1","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"min_count","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"activation","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":true,"doc_values":false},{"name":"template","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":true,"doc_values":false},{"name":"service_name.raw","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"precision","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"base_lr","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"description.raw","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"_index","type":"string","count":0,"scripted":false,"indexed":false,"analyzed":false,"doc_values":false},{"name":"batch_size","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"template.raw","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"test_interval","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"activation.raw","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"train_loss","type":"string","count":0,"scripted":false,"indexed":true,"analyzed":true,"doc_values":false},{"name":"min_word_length","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"recall","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"running_time","type":"number","count":0,"scripted":false,"indexed":true,"analyzed":false,"doc_values":true},{"name":"_id","type":"string","count":0,"scripted":false,"indexed":false,"analyzed":false,"doc_values":false},{"name":"_type","type":"string","count":0,"scripted":false,"indexed":false,"analyzed":false,"doc_values":false},{"name":"_score","type":"number","count":0,"scripted":false,"indexed":false,"analyzed":false,"doc_values":false}]'
      }

#Index pattern documents in the .kibana index
es.index(index=".kibana", doc_type="index-pattern", id="job_matrix",body=job_matrix)
es.index(index=".kibana", doc_type="index-pattern", id="job_tracking",body=job_data_tracking_pattern)
es.index(index=".kibana", doc_type="index-pattern", id="job_data",body=job_data_pattern)

#Prepare visualizations bodies

services_parameters = {
      "title": "services_parameters",
      "visState": "{\"title\":\"services_parameters\",\"type\":\"table\",\"params\":{\"perPage\":5,\"showPartialRows\":false,\"showMeticsAtAllLevels\":false},\"aggs\":[{\"id\":\"1\",\"type\":\"cardinality\",\"schema\":\"metric\",\"params\":{\"field\":\"service_name.raw\",\"customLabel\":\"Count\"}},{\"id\":\"2\",\"type\":\"terms\",\"schema\":\"bucket\",\"params\":{\"field\":\"service_name.raw\",\"size\":0,\"order\":\"desc\",\"orderBy\":\"1\",\"customLabel\":\"Service Name\"}},{\"id\":\"3\",\"type\":\"terms\",\"schema\":\"bucket\",\"params\":{\"field\":\"solver_type.raw\",\"size\":0,\"order\":\"desc\",\"orderBy\":\"1\",\"customLabel\":\"Solver\"}},{\"id\":\"4\",\"type\":\"terms\",\"schema\":\"bucket\",\"params\":{\"field\":\"activation.raw\",\"size\":0,\"order\":\"desc\",\"orderBy\":\"1\",\"customLabel\":\"Activation\"}},{\"id\":\"5\",\"type\":\"terms\",\"schema\":\"bucket\",\"params\":{\"field\":\"template.raw\",\"size\":0,\"order\":\"desc\",\"orderBy\":\"1\",\"customLabel\":\"Template\"}},{\"id\":\"6\",\"type\":\"terms\",\"schema\":\"bucket\",\"params\":{\"field\":\"base_lr\",\"size\":0,\"order\":\"desc\",\"orderBy\":\"1\",\"customLabel\":\"LR\"}},{\"id\":\"7\",\"type\":\"terms\",\"schema\":\"bucket\",\"params\":{\"field\":\"layers\",\"size\":5,\"order\":\"desc\",\"orderBy\":\"1\",\"customLabel\":\"Layers\"}},{\"id\":\"8\",\"type\":\"terms\",\"schema\":\"bucket\",\"params\":{\"field\":\"batch_size\",\"size\":0,\"order\":\"desc\",\"orderBy\":\"1\",\"customLabel\":\"Batch Size\"}}],\"listeners\":{}}",
      "uiStateJSON": "{}",
      "description": "",
      "version": 1,
      "kibanaSavedObjectMeta": {
        "searchSourceJSON": "{\"index\":\"dede_job_data\",\"query\":{\"query_string\":{\"analyze_wildcard\":true,\"query\":\"*\"}},\"filter\":[]}"
      }
  }

job_data_leaderboard = {
          "title": "job_data_leaderboard",
          "visState": "{\"title\":\"job_data_leaderboard\",\"type\":\"table\",\"params\":{\"perPage\":5,\"showMeticsAtAllLevels\":false,\"showPartialRows\":false},\"aggs\":[{\"id\":\"2\",\"type\":\"max\",\"schema\":\"metric\",\"params\":{\"field\":\"precision\",\"customLabel\":\"Max Precision\"}},{\"id\":\"3\",\"type\":\"terms\",\"schema\":\"bucket\",\"params\":{\"field\":\"service_name.raw\",\"size\":0,\"order\":\"desc\",\"orderBy\":\"2\",\"customLabel\":\"Service Name\"}},{\"id\":\"5\",\"type\":\"max\",\"schema\":\"metric\",\"params\":{\"field\":\"accp\",\"customLabel\":\"Max ACCP\"}},{\"id\":\"7\",\"type\":\"max\",\"schema\":\"metric\",\"params\":{\"field\":\"f1\",\"customLabel\":\"Max F1\"}},{\"id\":\"9\",\"type\":\"max\",\"schema\":\"metric\",\"params\":{\"field\":\"recall\",\"customLabel\":\"Max Recall\"}}],\"listeners\":{}}",
          "uiStateJSON": "{}",
          "description": "",
          "version": 1,
          "kibanaSavedObjectMeta": {
            "searchSourceJSON": "{\"index\":\"dede_job_data\",\"query\":{\"query_string\":{\"analyze_wildcard\":true,\"query\":\"*\"}},\"filter\":[]}"
          }
          }

accp_by_service_name = {
          "title": "accp_by_service_name",
          "visState": "{\"title\":\"precision_by_service_name\",\"type\":\"line\",\"params\":{\"addLegend\":true,\"addTimeMarker\":false,\"addTooltip\":true,\"defaultYExtents\":false,\"drawLinesBetweenPoints\":true,\"interpolate\":\"linear\",\"radiusRatio\":9,\"scale\":\"linear\",\"setYExtents\":false,\"shareYAxis\":true,\"showCircles\":true,\"smoothLines\":false,\"times\":[],\"yAxis\":{}},\"aggs\":[{\"id\":\"1\",\"type\":\"max\",\"schema\":\"metric\",\"params\":{\"field\":\"accp\"}},{\"id\":\"2\",\"type\":\"histogram\",\"schema\":\"segment\",\"params\":{\"field\":\"iteration\",\"interval\":200,\"extended_bounds\":{}}},{\"id\":\"3\",\"type\":\"terms\",\"schema\":\"group\",\"params\":{\"field\":\"service_name.raw\",\"size\":0,\"order\":\"desc\",\"orderBy\":\"1\"}}],\"listeners\":{}}",
          "uiStateJSON": "{}",
          "description": "",
          "version": 1,
          "kibanaSavedObjectMeta": {
            "searchSourceJSON": "{\"index\":\"dede_job_data\",\"query\":{\"query_string\":{\"analyze_wildcard\":true,\"query\":\"*\"}},\"filter\":[]}"
          }
          }


f1_by_service_name =  {
          "title": "f1_by_service_name",
          "visState": "{\"title\":\"accp_by_service_name\",\"type\":\"line\",\"params\":{\"addLegend\":true,\"addTimeMarker\":false,\"addTooltip\":true,\"defaultYExtents\":false,\"drawLinesBetweenPoints\":true,\"interpolate\":\"linear\",\"radiusRatio\":9,\"scale\":\"linear\",\"setYExtents\":false,\"shareYAxis\":true,\"showCircles\":true,\"smoothLines\":false,\"times\":[],\"yAxis\":{}},\"aggs\":[{\"id\":\"1\",\"type\":\"max\",\"schema\":\"metric\",\"params\":{\"field\":\"f1\"}},{\"id\":\"2\",\"type\":\"histogram\",\"schema\":\"segment\",\"params\":{\"field\":\"iteration\",\"interval\":200,\"extended_bounds\":{}}},{\"id\":\"3\",\"type\":\"terms\",\"schema\":\"group\",\"params\":{\"field\":\"service_name.raw\",\"size\":0,\"order\":\"desc\",\"orderBy\":\"1\"}}],\"listeners\":{}}",
          "uiStateJSON": "{}",
          "description": "",
          "version": 1,
          "kibanaSavedObjectMeta": {
            "searchSourceJSON": "{\"index\":\"dede_job_data\",\"query\":{\"query_string\":{\"analyze_wildcard\":true,\"query\":\"*\"}},\"filter\":[]}"
          }
          }

#Index visualization documents in the .kibana index
es.index(index=".kibana", doc_type="visualization",id="services_parameters", body=services_parameters)
es.index(index=".kibana", doc_type="visualization", id="job_data_leaderboard",body=job_data_leaderboard)
es.index(index=".kibana", doc_type="visualization", id="accp_by_service_name",body=accp_by_service_name)
es.index(index=".kibana", doc_type="visualization", id="f1_by_service_name",body=f1_by_service_name)


#Prepare dashboard document
services_dashboard = {"title": "Services Dashboard",
          "hits": 0,
          "description": "",
          "panelsJSON": '[{"col":1,"id":"job_data_leaderboard","panelIndex":3,"row":1,"size_x":6,"size_y":4,"type":"visualization"},{"col":7,"id":"services_parameters","panelIndex":4,"row":1,"size_x":6,"size_y":4,"type":"visualization"},{"id":"accp_by_service_name","type":"visualization","panelIndex":5,"size_x":12,"size_y":5,"col":1,"row":5},{"id":"f1_by_service_name","type":"visualization","panelIndex":6,"size_x":12,"size_y":4,"col":1,"row":10}]',
          "optionsJSON": '{"darkTheme":false}',
          "uiStateJSON": '{"P-5":{"spy":{"mode":{"name":null,"fill":false}}}}',
          "version": 1,
          "timeRestore": "false",
          "kibanaSavedObjectMeta": {
            "searchSourceJSON": '{"filter":[{"query":{"query_string":{"analyze_wildcard":true,"query":"*"}}}]}'
          }
          }
#Index dashboard document in the .kibana index
es.index(index=".kibana", doc_type="dashboard", id="Services-Dashboard",body=services_dashboard)
