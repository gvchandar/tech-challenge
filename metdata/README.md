Challenge 2
===========

We need to write code that will query the meta data of an instance within aws and provide a json formatted output. <br />
The choice of language and implementation is up to you.


Installing
----------
This program runs on Python 2.7.x<br />
Install requests and json python libraries<br />
pip install requests<br />
pip install json<br />
For better key/value pair display install jq library<br />


Testing
----------
chmod 755 metadata.py <br />
If no command line argument is provided, the system prints dump of all key values pair in JSON formatted<br />
./metadata.py <br />
To get better display of the output , pipe the output to jq<br />
./metadata.py  | jq <br />

To get value of a  key, pass the key as command line argument<br />
e.g<br />
./metadata.py hostname<br />

