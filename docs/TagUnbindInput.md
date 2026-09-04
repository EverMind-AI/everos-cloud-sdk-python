# TagUnbindInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory_type** | **str** | The type of the memories being untagged, e.g. \&quot;episode\&quot;. | 
**memory_ids** | **List[str]** | The memories to untag, by id (1–200 per request). | 
**tags** | **List[str]** | Tags to remove (1–100 per request). Tags not listed here are left in place. | 

## Example

```python
from everos_cloud.models.tag_unbind_input import TagUnbindInput

# TODO update the JSON string below
json = "{}"
# create an instance of TagUnbindInput from a JSON string
tag_unbind_input_instance = TagUnbindInput.from_json(json)
# print the JSON string representation of the object
print(TagUnbindInput.to_json())

# convert the object into a dict
tag_unbind_input_dict = tag_unbind_input_instance.to_dict()
# create an instance of TagUnbindInput from a dict
tag_unbind_input_from_dict = TagUnbindInput.from_dict(tag_unbind_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


