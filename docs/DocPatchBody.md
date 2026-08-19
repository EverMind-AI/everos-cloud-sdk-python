# DocPatchBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**category_id** | **str** |  | [optional] 

## Example

```python
from everos_cloud.models.doc_patch_body import DocPatchBody

# TODO update the JSON string below
json = "{}"
# create an instance of DocPatchBody from a JSON string
doc_patch_body_instance = DocPatchBody.from_json(json)
# print the JSON string representation of the object
print(DocPatchBody.to_json())

# convert the object into a dict
doc_patch_body_dict = doc_patch_body_instance.to_dict()
# create an instance of DocPatchBody from a dict
doc_patch_body_from_dict = DocPatchBody.from_dict(doc_patch_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


