# TagReplaceInput

Full replacement (PUT semantics): overwrite each item's tag set with ``tags``.  ``tags`` may be empty — an empty list clears all tags on the targeted items. Duplicates collapse (tags is a set; the service dedups before ``$set``).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory_type** | **str** |  | 
**memory_ids** | **List[str]** |  | 
**tags** | **List[str]** |  | 

## Example

```python
from everos_cloud.models.tag_replace_input import TagReplaceInput

# TODO update the JSON string below
json = "{}"
# create an instance of TagReplaceInput from a JSON string
tag_replace_input_instance = TagReplaceInput.from_json(json)
# print the JSON string representation of the object
print(TagReplaceInput.to_json())

# convert the object into a dict
tag_replace_input_dict = tag_replace_input_instance.to_dict()
# create an instance of TagReplaceInput from a dict
tag_replace_input_from_dict = TagReplaceInput.from_dict(tag_replace_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


