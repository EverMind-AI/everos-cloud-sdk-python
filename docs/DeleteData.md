# DeleteData

Delete result (mirrors v1 ``DeleteMemoriesResult``): which scope filters were applied + how many mongo records were soft-deleted across all memory types.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | **List[str]** | Scope filters used, e.g. [&#39;user_id&#39;] or [&#39;user_id&#39;, &#39;session_id&#39;] | [optional] 
**count** | **int** | Total memory records soft-deleted | [optional] [default to 0]

## Example

```python
from everos_cloud_sdk.models.delete_data import DeleteData

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


