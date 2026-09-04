# TaskStatsResponseData

The per-status counts and the window they cover.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**by_status** | [**TaskStatsResponseDataByStatus**](TaskStatsResponseDataByStatus.md) |  | 
**end** | **datetime** | End of the window actually aggregated | 
**start** | **datetime** | Start of the window actually aggregated, after server-side clamping | 
**total** | **int** |  | 

## Example

```python
from everos_cloud.models.task_stats_response_data import TaskStatsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of TaskStatsResponseData from a JSON string
task_stats_response_data_instance = TaskStatsResponseData.from_json(json)
# print the JSON string representation of the object
print(TaskStatsResponseData.to_json())

# convert the object into a dict
task_stats_response_data_dict = task_stats_response_data_instance.to_dict()
# create an instance of TaskStatsResponseData from a dict
task_stats_response_data_from_dict = TaskStatsResponseData.from_dict(task_stats_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


