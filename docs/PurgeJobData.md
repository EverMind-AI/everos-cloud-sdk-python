# PurgeJobData

A purge job as the caller sees it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | 
**status** | **str** |  | 
**scope** | **str** |  | 
**app_id** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**started_at** | **datetime** |  | [optional] 
**heartbeat_at** | **datetime** |  | [optional] 
**finished_at** | **datetime** |  | [optional] 
**steps** | [**List[PurgeStepData]**](PurgeStepData.md) |  | [optional] 

## Example

```python
from everos_cloud.models.purge_job_data import PurgeJobData

# TODO update the JSON string below
json = "{}"
# create an instance of PurgeJobData from a JSON string
purge_job_data_instance = PurgeJobData.from_json(json)
# print the JSON string representation of the object
print(PurgeJobData.to_json())

# convert the object into a dict
purge_job_data_dict = purge_job_data_instance.to_dict()
# create an instance of PurgeJobData from a dict
purge_job_data_from_dict = PurgeJobData.from_dict(purge_job_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


