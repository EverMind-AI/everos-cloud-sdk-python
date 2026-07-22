# AddOperation

Add a new profile item (``item_id`` forbidden — the server mints it).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**action** | **str** |  | 
**type** | **str** |  | 
**data** | [**Data**](Data.md) |  | 

## Example

```python
from everos_cloud_sdk.models.add_operation import AddOperation

# TODO update the JSON string below
json = "{}"
# create an instance of AddOperation from a JSON string
add_operation_instance = AddOperation.from_json(json)
# print the JSON string representation of the object
print(AddOperation.to_json())

# convert the object into a dict
add_operation_dict = add_operation_instance.to_dict()
# create an instance of AddOperation from a dict
add_operation_from_dict = AddOperation.from_dict(add_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


