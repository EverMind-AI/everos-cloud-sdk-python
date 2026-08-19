# DocDeleteData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Deleted document id | 
**deleted** | **bool** | True if a live document was soft-deleted; False if absent | 
**deleted_topics** | **int** | Nodes cascaded (P5; 0 for now) | [optional] [default to 0]

## Example

```python
from everos_cloud.models.doc_delete_data import DocDeleteData

# TODO update the JSON string below
json = "{}"
# create an instance of DocDeleteData from a JSON string
doc_delete_data_instance = DocDeleteData.from_json(json)
# print the JSON string representation of the object
print(DocDeleteData.to_json())

# convert the object into a dict
doc_delete_data_dict = doc_delete_data_instance.to_dict()
# create an instance of DocDeleteData from a dict
doc_delete_data_from_dict = DocDeleteData.from_dict(doc_delete_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


