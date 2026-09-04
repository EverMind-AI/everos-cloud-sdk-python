# Data

The item to add. Its required keys depend on `type`; other keys (evidence, sources, basis, …) ride through untouched.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | What kind of fact this is, e.g. \&quot;hobby\&quot;. Required, non-empty. | 
**description** | **str** | What the trait means and how it shows up, up to 4000 characters. | 
**trait** | **str** | The inferred trait&#39;s name. Required, non-empty. | 

## Example

```python
from everos_cloud.models.data import Data

# TODO update the JSON string below
json = "{}"
# create an instance of Data from a JSON string
data_instance = Data.from_json(json)
# print the JSON string representation of the object
print(Data.to_json())

# convert the object into a dict
data_dict = data_instance.to_dict()
# create an instance of Data from a dict
data_from_dict = Data.from_dict(data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


