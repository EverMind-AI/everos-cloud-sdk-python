# DocumentContext

The parent document a hit belongs to (rolled up for display).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc_id** | **str** |  | 
**title** | **str** |  | [optional] [default to '']
**summary** | **str** |  | [optional] 

## Example

```python
from everos_cloud.models.document_context import DocumentContext

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentContext from a JSON string
document_context_instance = DocumentContext.from_json(json)
# print the JSON string representation of the object
print(DocumentContext.to_json())

# convert the object into a dict
document_context_dict = document_context_instance.to_dict()
# create an instance of DocumentContext from a dict
document_context_from_dict = DocumentContext.from_dict(document_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


