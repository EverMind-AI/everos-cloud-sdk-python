# KbDeleteData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Deleted knowledge base id | 
**deleted** | **bool** | True if a live kb was soft-deleted; False if absent (idempotent) | 

## Example

```python
from everos_cloud.models.kb_delete_data import KbDeleteData

# TODO update the JSON string below
json = "{}"
# create an instance of KbDeleteData from a JSON string
kb_delete_data_instance = KbDeleteData.from_json(json)
# print the JSON string representation of the object
print(KbDeleteData.to_json())

# convert the object into a dict
kb_delete_data_dict = kb_delete_data_instance.to_dict()
# create an instance of KbDeleteData from a dict
kb_delete_data_from_dict = KbDeleteData.from_dict(kb_delete_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


