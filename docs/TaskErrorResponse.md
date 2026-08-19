# TaskErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**TaskErrorResponseError**](TaskErrorResponseError.md) |  | 

## Example

```python
from everos_cloud.models.task_error_response import TaskErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaskErrorResponse from a JSON string
task_error_response_instance = TaskErrorResponse.from_json(json)
# print the JSON string representation of the object
print(TaskErrorResponse.to_json())

# convert the object into a dict
task_error_response_dict = task_error_response_instance.to_dict()
# create an instance of TaskErrorResponse from a dict
task_error_response_from_dict = TaskErrorResponse.from_dict(task_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


