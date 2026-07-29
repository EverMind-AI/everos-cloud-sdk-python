# EditData

Response payload for a successful profile edit request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**version** | **int** |  | 
**applied** | **int** |  | 
**results** | [**List[EditResultItem]**](EditResultItem.md) |  | [optional] 
**profile** | **Dict[str, object]** |  | [optional] 

## Example

```python
from everos_cloud.models.edit_data import EditData

# TODO update the JSON string below
json = "{}"
# create an instance of EditData from a JSON string
edit_data_instance = EditData.from_json(json)
# print the JSON string representation of the object
print(EditData.to_json())

# convert the object into a dict
edit_data_dict = edit_data_instance.to_dict()
# create an instance of EditData from a dict
edit_data_from_dict = EditData.from_dict(edit_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


