# DocPatchData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**updated_fields** | **List[str]** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from everos_cloud.models.doc_patch_data import DocPatchData

# TODO update the JSON string below
json = "{}"
# create an instance of DocPatchData from a JSON string
doc_patch_data_instance = DocPatchData.from_json(json)
# print the JSON string representation of the object
print(DocPatchData.to_json())

# convert the object into a dict
doc_patch_data_dict = doc_patch_data_instance.to_dict()
# create an instance of DocPatchData from a dict
doc_patch_data_from_dict = DocPatchData.from_dict(doc_patch_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


