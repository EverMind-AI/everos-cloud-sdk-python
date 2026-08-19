# TaskItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**error** | **str** | Failure reason; present only when status is failed | [optional] 
**error_code** | **str** |  | [optional] 
**finished_at** | **datetime** | Completion time; absent while the task is not in a terminal state | [optional] 
**id** | **str** | Task id (the request&#39;s X-Request-Id), not a database primary key | 
**object** | **str** | Resource type produced by the task (frozen field, cannot express a batch) | [optional] 
**object_id** | **str** |  | [optional] 
**status** | **str** |  | 
**task_type** | **str** |  | [optional] 

## Example

```python
from everos_cloud.models.task_item import TaskItem

# TODO update the JSON string below
json = "{}"
# create an instance of TaskItem from a JSON string
task_item_instance = TaskItem.from_json(json)
# print the JSON string representation of the object
print(TaskItem.to_json())

# convert the object into a dict
task_item_dict = task_item_instance.to_dict()
# create an instance of TaskItem from a dict
task_item_from_dict = TaskItem.from_dict(task_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


