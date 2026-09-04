# AddOperation

Add a new profile item (``item_id`` forbidden — the server mints it).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**action** | **str** | Always \&quot;add\&quot; for this variant. | 
**type** | **str** | Which profile item this edit targets — \&quot;explicit_info\&quot; (a stated fact, needing &#x60;category&#x60; + &#x60;description&#x60;) or \&quot;implicit_traits\&quot; (an inferred trait, needing &#x60;trait&#x60; + &#x60;description&#x60;). | 
**data** | [**Data**](Data.md) |  | 

## Example

```python
from everos_cloud.models.add_operation import AddOperation

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


