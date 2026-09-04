# TagBindInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory_type** | **str** | The type of the memories being tagged. \&quot;episode\&quot; is what this phase supports; agent cases and skills onboard later without an API change. | 
**memory_ids** | **List[str]** | The memories to tag, by id (1–200 per request). Ids come from /api/v2/memory/get or /api/v2/memory/search. | 
**tags** | **List[str]** | Tags to add (1–100 per request, each 1–32 characters). Tags the memories already carry are left in place. | 

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


