Challenge 2
===========

We need to write code that will query the meta data of an instance within aws and provide a json formatted output. 
The choice of language and implementation is up to you.


Installing
----------
This program runs on Python 2.7.x
Install requests and json libraries
pip install requests
pip install json
For better key/value pair display install jq library


Testing
----------
chmod 755 metadata.py 
If no command line argument is provided, the system prints dump of all key values pair in JSON formatted
./metadata.py 
To get better display of the output , pipe the output to jq
./metadata.py  | jq

To get value of a  key, pass the key as command line argument
e.g
./metadata.py hostname

