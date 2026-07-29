# EditInputOperationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**action** | **str** |  | 
**type** | **str** |  | 
**data** | [**Data1**](Data1.md) |  | 
**item_id** | **str** |  | 

## Example

```python
from everos_cloud.models.edit_input_operations_inner import EditInputOperationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of EditInputOperationsInner from a JSON string
edit_input_operations_inner_instance = EditInputOperationsInner.from_json(json)
# print the JSON string representation of the object
print(EditInputOperationsInner.to_json())

# convert the object into a dict
edit_input_operations_inner_dict = edit_input_operations_inner_instance.to_dict()
# create an instance of EditInputOperationsInner from a dict
edit_input_operations_inner_from_dict = EditInputOperationsInner.from_dict(edit_input_operations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


