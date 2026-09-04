# GetInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | Scope to read from, defaulting to \&quot;default\&quot;. Must match the pair used on write. | [optional] [default to 'default']
**project_id** | **str** | Second half of the scope, defaulting to \&quot;default\&quot;. | [optional] [default to 'default']
**user_id** | **str** |  | [optional] 
**agent_id** | **str** |  | [optional] 
**memory_type** | **str** | Which kind of memory to list: \&quot;episode\&quot; (narrative summaries of past sessions), \&quot;profile\&quot; (stable identity and preferences), \&quot;agent_case\&quot; (a distilled past trajectory) or \&quot;agent_skill\&quot; (a reusable skill). It must match the owner — the mismatched pairings are rejected with 422. | 
**page** | **int** | 1-based page number. | [optional] [default to 1]
**page_size** | **int** | Items per page, 1 to 100 (default 20). | [optional] [default to 20]
**sort_by** | **str** | Order by \&quot;timestamp\&quot; (when the memory happened, default) or \&quot;updated_at\&quot; (when it was last written). Profiles and agent skills have no temporal column and always sort by \&quot;updated_at\&quot;. | [optional] [default to 'timestamp']
**sort_order** | **str** | \&quot;desc\&quot; (default, newest first) or \&quot;asc\&quot;. | [optional] [default to 'desc']
**with_readable_episode** | **bool** | Attach a human-readable rendering to each returned episode, for display only. Ignored for every non-episode &#x60;memory_type&#x60; rather than rejected. | [optional] [default to False]
**filters** | [**FilterNode**](FilterNode.md) |  | [optional] 

## Example

```python
from everos_cloud.models.get_input import GetInput

# TODO update the JSON string below
json = "{}"
# create an instance of GetInput from a JSON string
get_input_instance = GetInput.from_json(json)
# print the JSON string representation of the object
print(GetInput.to_json())

# convert the object into a dict
get_input_dict = get_input_instance.to_dict()
# create an instance of GetInput from a dict
get_input_from_dict = GetInput.from_dict(get_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


