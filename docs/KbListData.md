# KbListData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**knowledge_bases** | [**List[KbData]**](KbData.md) |  | [optional] 
**total** | **int** |  | [optional] [default to 0]

## Example

```python
from everos_cloud.models.kb_list_data import KbListData

# TODO update the JSON string below
json = "{}"
# create an instance of KbListData from a JSON string
kb_list_data_instance = KbListData.from_json(json)
# print the JSON string representation of the object
print(KbListData.to_json())

# convert the object into a dict
kb_list_data_dict = kb_list_data_instance.to_dict()
# create an instance of KbListData from a dict
kb_list_data_from_dict = KbListData.from_dict(kb_list_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


