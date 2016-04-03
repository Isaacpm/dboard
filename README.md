Script to automate grid search and hyperparamter optimization with the deep learning software www.deepdetect.com.
It stores the data into 4 Elasticsearch indexes for easy comparison of results with Kibana visualizations.
Tested with python 3.5.
Minimal knowledge of Elasticsearch and DeepDetect is required.

Usage:
	The initial part of the script is used to set a series of lists with parameters which will be combined in all possible combinations, then run serially.
	It connects to a local dede and elasticsearch instances in their default ports.
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
	Once the parameters are set the script can be run from the command line as any other python script.

Elasticsearch and Data Visualization:
	The script indexes into 4 ES indexes:
		confusion_matrix: This index contains the information of the confusion matrix
		job_data: This index contains the information gathered from the historical data output for the service training, it's indexed when the service training has finished and the datapoints are pulled at regular intervals. This is preferred to compare services against each other as all data points are consistent in their iteration.
		job_data_tracking: This index contains the information pulled regularly from the service training run, the scripts requests information every 10 seconds and indexes the data. This index can be used to trak the evolution of services until the final job history is pulled.
		job_summary: This index contains a summary for each service, with total running time, iterations and cmdiag output.
	All this data can be visualized in Kibana.
	For a better visualization, it is recommended to create a template for the indexes and set either a multifield with one field not analyzed for the text fields or set the field to not analyzed and an analyzed multifield.

Example:
	The following is an example of parameters that can be used for a grid search for the solver type ADAM.
		solver_type_list = ['ADAM']
		layers_list = [[600,600],[700,700],[800,800]]
		iterations_list = [15000]
		base_lr_list = [0.05]
		template_list = ["mlp"]
		activation_list = ["relu","prelu"]
		test_split_list = [0.2]
		min_count_list = [2]
		min_word_length_list = [2]
		batch_size_list = [100,200,300,400,500]
		test_interval_list = [200]
	After setting the parameters and making sure dede and ES/Kibana are running, the only thing left is to run the script and track the results in kibana.