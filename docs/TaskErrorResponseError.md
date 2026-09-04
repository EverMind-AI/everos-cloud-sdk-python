# TaskErrorResponseError

What went wrong, with a machine-readable code and a message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Error code, e.g. invalid_request, not_found, unavailable | 
**message** | **str** |  | 
**type** | **str** | Error class, carrying the HTTP status text (BadRequest, NotFound, ...) | 

## Example

```python
from everos_cloud.models.task_error_response_error import TaskErrorResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of TaskErrorResponseError from a JSON string
task_error_response_error_instance = TaskErrorResponseError.from_json(json)
# print the JSON string representation of the object
print(TaskErrorResponseError.to_json())

# convert the object into a dict
task_error_response_error_dict = task_error_response_error_instance.to_dict()
# create an instance of TaskErrorResponseError from a dict
task_error_response_error_from_dict = TaskErrorResponseError.from_dict(task_error_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


