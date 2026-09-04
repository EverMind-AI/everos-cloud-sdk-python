# TagRef

Opaque semantic tag reference; its containing topic conveys ownership.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Opaque semantic tag id. | 
**name** | **str** |  | [optional] 

## Example

```python
from everos_cloud.models.tag_ref import TagRef

# TODO update the JSON string below
json = "{}"
# create an instance of TagRef from a JSON string
tag_ref_instance = TagRef.from_json(json)
# print the JSON string representation of the object
print(TagRef.to_json())

# convert the object into a dict
tag_ref_dict = tag_ref_instance.to_dict()
# create an instance of TagRef from a dict
tag_ref_from_dict = TagRef.from_dict(tag_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


