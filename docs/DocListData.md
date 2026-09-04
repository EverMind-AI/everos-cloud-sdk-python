# DocListData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documents** | [**List[DocData]**](DocData.md) | This page of documents. | [optional] 
**total** | **int** | How many documents match, across all pages. | [optional] [default to 0]

## Example

```python
from everos_cloud.models.doc_list_data import DocListData

# TODO update the JSON string below
json = "{}"
# create an instance of DocListData from a JSON string
doc_list_data_instance = DocListData.from_json(json)
# print the JSON string representation of the object
print(DocListData.to_json())

# convert the object into a dict
doc_list_data_dict = doc_list_data_instance.to_dict()
# create an instance of DocListData from a dict
doc_list_data_from_dict = DocListData.from_dict(doc_list_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


