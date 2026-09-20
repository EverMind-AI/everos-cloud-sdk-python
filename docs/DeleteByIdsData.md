# DeleteByIdsData

Result of a by-ids soft delete. A 200 means the request was applied; ids that were already gone are a no-op, not a failure, so a re-sent batch is safe.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory_type** | **str** | The memory type the request named. | 
**success** | **bool** | Always true on a 200 — the batch was applied. Failures use the error envelope instead. | 

## Example

```python
from everos_cloud.models.delete_by_ids_data import DeleteByIdsData

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteByIdsData from a JSON string
delete_by_ids_data_instance = DeleteByIdsData.from_json(json)
# print the JSON string representation of the object
print(DeleteByIdsData.to_json())

# convert the object into a dict
delete_by_ids_data_dict = delete_by_ids_data_instance.to_dict()
# create an instance of DeleteByIdsData from a dict
delete_by_ids_data_from_dict = DeleteByIdsData.from_dict(delete_by_ids_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


