# TaskItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | When the task was accepted. | [optional] 
**error** | **str** | Failure reason; present only when status is failed | [optional] 
**error_code** | **str** | Machine-readable failure code, alongside the human-readable &#x60;error&#x60;. | [optional] 
**finished_at** | **datetime** | Completion time; absent while the task is not in a terminal state | [optional] 
**id** | **str** | Task id (the request&#39;s X-Request-Id), not a database primary key | 
**object** | **str** | Resource type produced by the task (frozen field, cannot express a batch) | [optional] 
**object_id** | **str** | Id of the resource the task produced, once there is one. | [optional] 
**status** | **str** | Where the task is: \&quot;queued\&quot;, \&quot;processing\&quot;, \&quot;pending\&quot;, \&quot;success\&quot; or \&quot;failed\&quot;. Treat it as an open set — a value you do not recognise is terminal only when &#x60;finished_at&#x60; is set. | 
**task_type** | **str** | Async interface that produced the task, e.g. memory_add / knowledge_document / batch_import | [optional] 

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


