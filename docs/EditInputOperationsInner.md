# EditInputOperationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**action** | **str** | Always \&quot;delete\&quot; for this variant. | 
**type** | **str** | Which profile item this edit targets — \&quot;explicit_info\&quot; (a stated fact, needing &#x60;category&#x60; + &#x60;description&#x60;) or \&quot;implicit_traits\&quot; (an inferred trait, needing &#x60;trait&#x60; + &#x60;description&#x60;). | 
**data** | [**Data1**](Data1.md) |  | 
**item_id** | **str** | The item to delete. Its prefix must match the item type (\&quot;ei_\&quot; / \&quot;it_\&quot;) followed by 24 hex characters. | 

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


