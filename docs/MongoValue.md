# MongoValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from everos_cloud.models.mongo_value import MongoValue

# TODO update the JSON string below
json = "{}"
# create an instance of MongoValue from a JSON string
mongo_value_instance = MongoValue.from_json(json)
# print the JSON string representation of the object
print(MongoValue.to_json())

# convert the object into a dict
mongo_value_dict = mongo_value_instance.to_dict()
# create an instance of MongoValue from a dict
mongo_value_from_dict = MongoValue.from_dict(mongo_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


