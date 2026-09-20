# DeleteByIdsInput

Soft-delete the named memory records [Cloud-only].

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory_type** | **str** | Kind of the memories being deleted. Only \&quot;episode\&quot; is accepted today. | 
**memory_ids** | **List[str]** | 1 to 50 memory ids. Every one must be well-formed; duplicates are collapsed. | 
**reason** | [**Reason**](Reason.md) |  | [optional] 

## Example

```python
from everos_cloud.models.delete_by_ids_input import DeleteByIdsInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteByIdsInput from a JSON string
delete_by_ids_input_instance = DeleteByIdsInput.from_json(json)
# print the JSON string representation of the object
print(DeleteByIdsInput.to_json())

# convert the object into a dict
delete_by_ids_input_dict = delete_by_ids_input_instance.to_dict()
# create an instance of DeleteByIdsInput from a dict
delete_by_ids_input_from_dict = DeleteByIdsInput.from_dict(delete_by_ids_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


