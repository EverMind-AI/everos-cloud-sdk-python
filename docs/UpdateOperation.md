# UpdateOperation

Update an existing profile item (partial ``data`` shallow-merge).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**action** | **str** | Always \&quot;update\&quot; for this variant. | 
**type** | **str** | Which profile item this edit targets — \&quot;explicit_info\&quot; or \&quot;implicit_traits\&quot;. It must match the &#x60;item_id&#x60; prefix. | 
**item_id** | **str** | The item to update. Its prefix must match the item type — \&quot;ei_\&quot; for explicit_info, \&quot;it_\&quot; for implicit_traits — followed by 24 hex characters. | 
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


