# KbCreateInput

POST /knowledge_bases request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name | 
**description** | **str** | Description | [optional] [default to '']
**owner_id** | **str** |  | [optional] 

## Example

```python
from everos_cloud.models.kb_create_input import KbCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of KbCreateInput from a JSON string
kb_create_input_instance = KbCreateInput.from_json(json)
# print the JSON string representation of the object
print(KbCreateInput.to_json())

# convert the object into a dict
kb_create_input_dict = kb_create_input_instance.to_dict()
# create an instance of KbCreateInput from a dict
kb_create_input_from_dict = KbCreateInput.from_dict(kb_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


