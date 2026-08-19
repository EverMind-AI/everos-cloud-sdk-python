# TagUnbindInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory_type** | **str** |  | 
**memory_ids** | **List[str]** |  | 
**tags** | **List[str]** |  | 

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


