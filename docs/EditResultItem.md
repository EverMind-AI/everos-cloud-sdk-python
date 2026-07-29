# EditResultItem

Per-operation outcome returned in ``EditData.results``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op_index** | **int** |  | 
**action** | **str** |  | 
**type** | **str** |  | 
**status** | **str** |  | 
**item_id** | **str** |  | [optional] 
**new_item_id** | **str** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from everos_cloud.models.edit_result_item import EditResultItem

# TODO update the JSON string below
json = "{}"
# create an instance of EditResultItem from a JSON string
edit_result_item_instance = EditResultItem.from_json(json)
# print the JSON string representation of the object
print(EditResultItem.to_json())

# convert the object into a dict
edit_result_item_dict = edit_result_item_instance.to_dict()
# create an instance of EditResultItem from a dict
edit_result_item_from_dict = EditResultItem.from_dict(edit_result_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


