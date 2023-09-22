# jsonapi
Extended JSONEncoder and JSONDecoder to support serialize and deserialize complex and range object in python.

# Set up instructions
1. unzip the .tar.gz file
2. cd to the file that contains setup.py
3. Run: python setup.py build
4. Run: python setup.py install

# Sample Code

```Python

import json
import jsonapi

data = {
    "complex_num": complex(1, 2),
    "range_obj": range(1, 10, 2)
}

#Serializing
serialized_data = json.dumps(data, cls=MyEncoder)
print(serialized_data)

#Deserializing
deserialized_data = json.loads(serialized_data, cls=MyDecoder)
print(deserialized_data)

```


