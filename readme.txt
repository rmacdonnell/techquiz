#python solution for auto generating static landingpage 

this should ideally be done in a puppet/salt solution using grains and pillars ( modules and manifests)

this is a single use script but built in a way to be easily changed and accept additional arguements and expand functionality

it is hard coded to accept only 1 user arguement and if none present default to testquiz

can be changed to put serverblock in nginx site 
Example:
within "def sbcontents(self,site):" is #server_name 
uncomment this to have this script base its creation off of hostheader using regex lookups
you will currently get warnings about dual port 8888 blocks if you test this without that consideration 
as multiple blocks are attempting to listen for the same thing on the same port 
as they are looking at seperate roots you would have seperate html content
in certain scenarios knowing and being able to introduce this is beneficial.


to run this script download the python script contained within ./techquiz
then run
chmod u+x ./techquiz.py
./techquiz.py

