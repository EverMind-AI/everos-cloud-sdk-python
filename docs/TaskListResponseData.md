# TaskListResponseData

The page of tasks, with its paging counters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[TaskItem]**](TaskItem.md) |  | 
**page** | **int** |  | 
**page_size** | **int** |  | 
**total** | **int** |  | 

## Example

```python
from everos_cloud.models.task_list_response_data import TaskListResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of TaskListResponseData from a JSON string
task_list_response_data_instance = TaskListResponseData.from_json(json)
# print the JSON string representation of the object
print(TaskListResponseData.to_json())

# convert the object into a dict
task_list_response_data_dict = task_list_response_data_instance.to_dict()
# create an instance of TaskListResponseData from a dict
task_list_response_data_from_dict = TaskListResponseData.from_dict(task_list_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


