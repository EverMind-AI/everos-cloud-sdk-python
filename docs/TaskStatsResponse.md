# TaskStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TaskStatsResponseData**](TaskStatsResponseData.md) |  | 
**request_id** | **str** |  | [optional] 

## Example

```python
from everos_cloud.models.task_stats_response import TaskStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaskStatsResponse from a JSON string
task_stats_response_instance = TaskStatsResponse.from_json(json)
# print the JSON string representation of the object
print(TaskStatsResponse.to_json())

# convert the object into a dict
task_stats_response_dict = task_stats_response_instance.to_dict()
# create an instance of TaskStatsResponse from a dict
task_stats_response_from_dict = TaskStatsResponse.from_dict(task_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


