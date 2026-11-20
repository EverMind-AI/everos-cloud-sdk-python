# RebuildStatusData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | 
**status** | **str** |  | 
**targets** | **List[str]** |  | [optional] 
**progress** | [**RebuildProgress**](RebuildProgress.md) |  | 
**error** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**finished_at** | **datetime** |  | [optional] 

## Example

```python
from everos_cloud.models.rebuild_status_data import RebuildStatusData

# TODO update the JSON string below
json = "{}"
# create an instance of RebuildStatusData from a JSON string
rebuild_status_data_instance = RebuildStatusData.from_json(json)
# print the JSON string representation of the object
print(RebuildStatusData.to_json())

# convert the object into a dict
rebuild_status_data_dict = rebuild_status_data_instance.to_dict()
# create an instance of RebuildStatusData from a dict
rebuild_status_data_from_dict = RebuildStatusData.from_dict(rebuild_status_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


