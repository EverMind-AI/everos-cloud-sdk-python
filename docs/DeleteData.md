# DeleteData

Which scope filters were applied and how many memory records were deleted across all memory types.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | **List[str]** | Scope filters used, e.g. [&#39;user_id&#39;] or [&#39;user_id&#39;, &#39;session_id&#39;] | [optional] 
**count** | **int** | Total memory records deleted | [optional] [default to 0]
**rebuild_required** | **bool** | True when derived memories built from the deleted ones were kept and may still contain their content; call /memory/rebuild to regenerate them. | [optional] [default to False]
**targets** | **List[str]** | What /memory/rebuild would regenerate; empty when nothing. | [optional] 

## Example

```python
from everos_cloud.models.delete_data import DeleteData

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteData from a JSON string
delete_data_instance = DeleteData.from_json(json)
# print the JSON string representation of the object
print(DeleteData.to_json())

# convert the object into a dict
delete_data_dict = delete_data_instance.to_dict()
# create an instance of DeleteData from a dict
delete_data_from_dict = DeleteData.from_dict(delete_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


