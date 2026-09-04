# DeleteOperation

Delete an existing profile item by ``item_id`` (carries no ``data``).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**action** | **str** | Always \&quot;delete\&quot; for this variant. | 
**type** | **str** | Which profile item this edit targets — \&quot;explicit_info\&quot; or \&quot;implicit_traits\&quot;. It must match the &#x60;item_id&#x60; prefix. | 
**item_id** | **str** | The item to delete. Its prefix must match the item type (\&quot;ei_\&quot; / \&quot;it_\&quot;) followed by 24 hex characters. | 

## Example

```python
from everos_cloud.models.delete_operation import DeleteOperation

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteOperation from a JSON string
delete_operation_instance = DeleteOperation.from_json(json)
# print the JSON string representation of the object
print(DeleteOperation.to_json())

# convert the object into a dict
delete_operation_dict = delete_operation_instance.to_dict()
# create an instance of DeleteOperation from a dict
delete_operation_from_dict = DeleteOperation.from_dict(delete_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


