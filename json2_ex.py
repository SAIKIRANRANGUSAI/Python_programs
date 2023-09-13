""""
-> SON (JavaScript Object Notation) is a popular data format used for representing structured data.
  It's common to transmit and receive data between a server and web application in JSON format.
-> should use double cotataion marks("")
-> booleans should be in lower case
-> You can convert Python objects of the following types, into JSON strings:

dict
list
tuple
string
int
float
True
False
None
"""

# Convert from Python to JSON:   we should use .dump()
#You can parse a JSON string using json.loads() method. The method returns a dictionary.

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)