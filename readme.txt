#python solution for auto generating static landingpage 

this should ideally be done in a puppet/salt solution using grains and pillars ( modules and manifests)

this is a single use script but built in a way to be easily changed and accept additional arguements

it is hard coded to accept only 1 user arguement and if none present default to testquiz

in the method sbcontents the server block body shows an example of how to use this in way to auto config seperate enviornments using regex for servername

to run this script download the python script contained within ./techquiz
then run
chmod u+x ./techquiz.py
./techquiz.py

