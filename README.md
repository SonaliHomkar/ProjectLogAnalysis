Log Analysis

This project is aimed to generate following reports from news database which can be used by management for analysis
1. What are the most popular three articles of all time
2. Who are the most popular article authors of all time
3. On which days did more than 1% of requests lead to errors


Getting Started
1. Go to https://github.com/SonaliHomkar/ProjectLogAnalysis
2. Download or clone the entire folder
3. On your vagrant machine copy the entire folder
4. Download the newsdata.sql using section "Download the data" on the following link
	https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/262a84d7-86dc-487d-98f9-648aa7ca5a0f/concepts/a9cf98c8-0325-4c68-b972-58d5957f1a91
		
	

Prerequisites
1. Vagrant 
2. Virtual box
3. python3
4. News database should be set up on vagrant machine

Installing
1. Add line following line in the Vagrantfile to add the port to server

 	config.vm.network "forwarded_port", guest: 5000, host: 5000
2. Please compile the file LogQuery.py using compiler python3
3. Compile LogAnalysis.py using compiler python3
4. It should start the server and display the following message
 	* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 	* Restarting with stat
 	* Debugger is active!
 	* Debugger PIN: 925-200-313

 	

Running the tests
1. Open the browser and type http://localhost:5000/
   It should open the page with heading "News Reports" with the following option to generate the report
 	a. What are the most popular three articles of all time?  View (button)
	b. Who are the most popular article authors of all time? View (button)
	c. On which days did more than 1% of requests lead to errors? View (button)
2. Clicking on View button of each report should display the report

 




