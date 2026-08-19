# TaskStatsResponseDataByStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed** | **int** |  | 
**processing** | **int** |  | 
**queued** | **int** |  | 
**success** | **int** |  | 

## Example

```python
from everos_cloud.models.task_stats_response_data_by_status import TaskStatsResponseDataByStatus

# TODO update the JSON string below
json = "{}"
# create an instance of TaskStatsResponseDataByStatus from a JSON string
task_stats_response_data_by_status_instance = TaskStatsResponseDataByStatus.from_json(json)
# print the JSON string representation of the object
print(TaskStatsResponseDataByStatus.to_json())

# convert the object into a dict
task_stats_response_data_by_status_dict = task_stats_response_data_by_status_instance.to_dict()
# create an instance of TaskStatsResponseDataByStatus from a dict
task_stats_response_data_by_status_from_dict = TaskStatsResponseDataByStatus.from_dict(task_stats_response_data_by_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


