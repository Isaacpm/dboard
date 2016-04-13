Set of scripts to automate results gathering storage, review and decsion with the deep learning software www.deepdetect.com.
It stores the data into 3 Elasticsearch indexes for easy comparison of results with Kibana visualizations.
Tested with python 3.5, ES 2.3 and Kibana 4.5.
ES must be running before running any of the scripts
Dede installation is assumed to be in /var/deepdetect

There are three main parts, the model creation and ES/Kibana configuration and the config file which provides the settings for the scripts.

Config File
	It has two sections:
		Connection Parameters:
			IP or hostname for ES
			IP or hostname for DeepDetect

	Model parameteres:
		Not all possible parameters are present and only works with txt connectors at the moment, currently the only parameteres that can be used in the grid search are:
			solver_type_list
			layers_list
			iterations_list
			base_lr_list
			template_list
			activation_list
			test_split_list
			min_count_list
			min_word_length_list
			batch_size_list
			test_interval_list

Elasticsearch and Data Visualization:
	es_setup creates the templates which will be used by the model creation script when indexing the data. Each string field with less than 256 characteres will have a multifield .raw which won't be analyzed.
	kibana_setup creates the index patterns to access the data from the indices. The index patterns will point to the aliases of the indices, not to the indices themselves.
	ES indexing behaviour, controlled by the model creation script. Each Dede service will have its own set of indices. There will be 3 indices per service:
		-dede_job_data_SERVICE_NAME, containing the final data of the script. Data points gathered from the job history
		-dede_job_tracking_SERVICE_NAME, containing the traking of the service as the script pulls data every 10s
		-dede_job_matrix_SERVICE_NAME, containing the counfusion matrix for the service
	There are 3 main aliases:
		-dede_job_data, points to all dede_job_data_XXX indices
		-dede_job_tracking points to all dede_job_tracking_XXX indices
		-dede_job_matrix, points to all dede_job_matrix_XXX indices
	Kibana will access the data through the aliases to see the information across all services, but individual indices can be used to delete/modify/explore specific services' data.
	To execute the scripts:
	python3.5 es_setup.py
	python3.5 kibana_setup.py

Model Creation:
	Once the parameters are set in the config file the script can be run from the command line as any other python script:
	python3.5 dboard.py

Example of a config file:
	The following is an example of parameters that can be used for a grid search for the solver type ADAM.
	#Deepgrid config

	#Connection Parameters
	dede_server : localhost
	es_server : localhost

	#Services Parameters, in a semicolon separated list of values
	solver_type_list : ADAM
	layers_list : 600,600;700,700;800,800
	iterations_list : 15000
	base_lr_list : 0.05
	template_list : mlp
	activation_list : relu,prelu
	test_split_list : 0.2
	min_count_list : 2
	min_word_length_list : 2
	batch_size_list : 100,200,300,400
	test_interval_list : 200
	nclasses: 10
	root_repository : /var/models_repo


