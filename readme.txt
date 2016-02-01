#python solution for auto generating static landingpage 

this should ideally be implemented alongside a puppet/salt solution using grains and pillars ( modules and manifests)

it is currently hard coded to accept only a single argument and if none present defaults to testquiz

additional functionality.
generate serverblock in nginx site config 
Example:
within "def sbcontents(self,site):" is a line #server_name 
uncomment this to have this script use argument input as servername and hostheader using regex lookups 
you will get warnings about dual port 8888 blocks if you use this without that uncommented
this is becasue multiple blocks are attempting to listen for the same thing on the same port, 
since these blocks are looking at seperate roots for the index you would have seperate html content
in certain scenarios knowing and being able to introduce this is beneficial. 
you can round robin and present different data for the same endpoint

Other uses
auto generation of 301 redirects to seperate locations
present a txt file for health check from load balancer.


to run this script download the python script contained within ./techquiz
then run
chmod u+x ./techquiz.py
./techquiz.py

