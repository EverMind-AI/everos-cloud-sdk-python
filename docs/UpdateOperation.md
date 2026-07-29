# UpdateOperation

Update an existing profile item (partial ``data`` shallow-merge).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**action** | **str** |  | 
**type** | **str** |  | 
**item_id** | **str** |  | 
**data** | [**Data1**](Data1.md) |  | 

## Example

```python
from everos_cloud.models.update_operation import UpdateOperation

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOperation from a JSON string
update_operation_instance = UpdateOperation.from_json(json)
# print the JSON string representation of the object
print(UpdateOperation.to_json())

# convert the object into a dict
update_operation_dict = update_operation_instance.to_dict()
# create an instance of UpdateOperation from a dict
update_operation_from_dict = UpdateOperation.from_dict(update_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


