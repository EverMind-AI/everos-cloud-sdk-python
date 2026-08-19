# TagBindInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory_type** | **str** |  | 
**memory_ids** | **List[str]** |  | 
**tags** | **List[str]** |  | 

## Example

```python
from everos_cloud.models.tag_bind_input import TagBindInput

# TODO update the JSON string below
json = "{}"
# create an instance of TagBindInput from a JSON string
tag_bind_input_instance = TagBindInput.from_json(json)
# print the JSON string representation of the object
print(TagBindInput.to_json())

# convert the object into a dict
tag_bind_input_dict = tag_bind_input_instance.to_dict()
# create an instance of TagBindInput from a dict
tag_bind_input_from_dict = TagBindInput.from_dict(tag_bind_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


