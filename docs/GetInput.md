# GetInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | [optional] [default to 'default']
**project_id** | **str** |  | [optional] [default to 'default']
**user_id** | **str** |  | [optional] 
**agent_id** | **str** |  | [optional] 
**memory_type** | **str** |  | 
**page** | **int** |  | [optional] [default to 1]
**page_size** | **int** |  | [optional] [default to 20]
**sort_by** | **str** |  | [optional] [default to 'timestamp']
**sort_order** | **str** |  | [optional] [default to 'desc']
**filters** | [**FilterNode**](FilterNode.md) |  | [optional] 

## Example

```python
from everos_cloud.models.get_input import GetInput

# TODO update the JSON string below
json = "{}"
# create an instance of GetInput from a JSON string
get_input_instance = GetInput.from_json(json)
# print the JSON string representation of the object
print(GetInput.to_json())

# convert the object into a dict
get_input_dict = get_input_instance.to_dict()
# create an instance of GetInput from a dict
get_input_from_dict = GetInput.from_dict(get_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


