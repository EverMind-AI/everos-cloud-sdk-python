# AgentSkillItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**app_id** | **str** |  | 
**project_id** | **str** |  | 
**agent_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**content** | **str** |  | 
**confidence** | **float** |  | 
**maturity_score** | **float** |  | 
**source_case_ids** | **List[str]** |  | [optional] 

## Example

```python
from everos_cloud_sdk.models.agent_skill_item import AgentSkillItem

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSkillItem from a JSON string
agent_skill_item_instance = AgentSkillItem.from_json(json)
# print the JSON string representation of the object
print(AgentSkillItem.to_json())

# convert the object into a dict
agent_skill_item_dict = agent_skill_item_instance.to_dict()
# create an instance of AgentSkillItem from a dict
agent_skill_item_from_dict = AgentSkillItem.from_dict(agent_skill_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


