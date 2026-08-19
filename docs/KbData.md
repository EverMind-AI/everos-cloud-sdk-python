# KbData

A knowledge base as returned to clients (create / get / list item / patch).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Knowledge base id (bare primary key) | 
**name** | **str** |  | 
**description** | **str** |  | [optional] [default to '']
**owner_id** | **str** |  | [optional] 
**document_count** | **int** |  | [optional] [default to 0]
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from everos_cloud.models.kb_data import KbData

# TODO update the JSON string below
json = "{}"
# create an instance of KbData from a JSON string
kb_data_instance = KbData.from_json(json)
# print the JSON string representation of the object
print(KbData.to_json())

# convert the object into a dict
kb_data_dict = kb_data_instance.to_dict()
# create an instance of KbData from a dict
kb_data_from_dict = KbData.from_dict(kb_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


