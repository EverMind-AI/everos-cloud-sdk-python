# EditData

Response payload for a successful profile edit request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The user whose profile was edited. | 
**version** | **int** | The profile&#39;s version after this edit. It advances every time the profile changes. | 
**applied** | **int** | How many of the submitted operations took effect. | 
**results** | [**List[EditResultItem]**](EditResultItem.md) | Per-operation outcome, in submission order — check this rather than assuming all applied. | [optional] 
**profile** | **Dict[str, object]** | The profile as it stands after the edit, so no follow-up read is needed. | [optional] 

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


