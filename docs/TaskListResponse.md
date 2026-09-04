# TaskListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TaskListResponseData**](TaskListResponseData.md) |  | 
**request_id** | **str** | Id of this request — quote it when reporting a problem. | [optional] 

## Example

```python
from everos_cloud.models.task_list_response import TaskListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaskListResponse from a JSON string
task_list_response_instance = TaskListResponse.from_json(json)
# print the JSON string representation of the object
print(TaskListResponse.to_json())

# convert the object into a dict
task_list_response_dict = task_list_response_instance.to_dict()
# create an instance of TaskListResponse from a dict
task_list_response_from_dict = TaskListResponse.from_dict(task_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


