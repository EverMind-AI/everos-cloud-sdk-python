# EditInput

Bulk profile edit request [Cloud-only].  Carries 1–50 ``EditOperation`` items targeting a single user's profile. ``memory_type`` is pinned to ``\"profile\"``; ``source`` is server-set and not accepted from the client.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | [optional] [default to 'default']
**project_id** | **str** |  | [optional] [default to 'default']
**user_id** | **str** |  | 
**memory_type** | **str** |  | [optional] [default to 'profile']
**operations** | [**List[EditInputOperationsInner]**](EditInputOperationsInner.md) |  | 

## Example

```python
from everos_cloud_sdk.models.edit_input import EditInput

# TODO update the JSON string below
json = "{}"
# create an instance of EditInput from a JSON string
edit_input_instance = EditInput.from_json(json)
# print the JSON string representation of the object
print(EditInput.to_json())

# convert the object into a dict
edit_input_dict = edit_input_instance.to_dict()
# create an instance of EditInput from a dict
edit_input_from_dict = EditInput.from_dict(edit_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


