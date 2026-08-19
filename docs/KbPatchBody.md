# KbPatchBody

PATCH request BODY (kb_id rides the path, not the body).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from everos_cloud.models.kb_patch_body import KbPatchBody

# TODO update the JSON string below
json = "{}"
# create an instance of KbPatchBody from a JSON string
kb_patch_body_instance = KbPatchBody.from_json(json)
# print the JSON string representation of the object
print(KbPatchBody.to_json())

# convert the object into a dict
kb_patch_body_dict = kb_patch_body_instance.to_dict()
# create an instance of KbPatchBody from a dict
kb_patch_body_from_dict = KbPatchBody.from_dict(kb_patch_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


