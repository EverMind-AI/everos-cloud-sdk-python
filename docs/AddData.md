# AddData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_count** | **int** |  | 
**status** | **str** | \&quot;queued\&quot; — async enqueue accepted (HTTP 202). \&quot;accumulated\&quot;/\&quot;extracted\&quot; — synchronous write outcome (HTTP 200, async_mode&#x3D;false). | 

## Example

```python
from everos_cloud.models.add_data import AddData

# TODO update the JSON string below
json = "{}"
# create an instance of AddData from a JSON string
add_data_instance = AddData.from_json(json)
# print the JSON string representation of the object
print(AddData.to_json())

# convert the object into a dict
add_data_dict = add_data_instance.to_dict()
# create an instance of AddData from a dict
add_data_from_dict = AddData.from_dict(add_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


