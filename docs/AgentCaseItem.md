# AgentCaseItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**app_id** | **str** |  | 
**project_id** | **str** |  | 
**agent_id** | **str** |  | 
**session_id** | **str** |  | 
**task_intent** | **str** |  | 
**approach** | **str** |  | 
**quality_score** | **float** |  | 
**key_insight** | **str** |  | [optional] 
**timestamp** | **datetime** |  | 

## Example

```python
from everos_cloud_sdk.models.agent_case_item import AgentCaseItem

# TODO update the JSON string below
json = "{}"
# create an instance of AgentCaseItem from a JSON string
agent_case_item_instance = AgentCaseItem.from_json(json)
# print the JSON string representation of the object
print(AgentCaseItem.to_json())

# convert the object into a dict
agent_case_item_dict = agent_case_item_instance.to_dict()
# create an instance of AgentCaseItem from a dict
agent_case_item_from_dict = AgentCaseItem.from_dict(agent_case_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


