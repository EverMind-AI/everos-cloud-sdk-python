# FlushInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | [optional] [default to 'default']
**project_id** | **str** |  | [optional] [default to 'default']
**session_id** | **str** |  | 

## Example

```python
from everos_cloud_sdk.models.flush_input import FlushInput

# TODO update the JSON string below
json = "{}"
# create an instance of FlushInput from a JSON string
flush_input_instance = FlushInput.from_json(json)
# print the JSON string representation of the object
print(FlushInput.to_json())

# convert the object into a dict
flush_input_dict = flush_input_instance.to_dict()
# create an instance of FlushInput from a dict
flush_input_from_dict = FlushInput.from_dict(flush_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


