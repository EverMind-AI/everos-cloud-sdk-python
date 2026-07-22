# SearchAgentSkillItem


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
**score** | **float** |  | 

## Example

```python
from everos_cloud_sdk.models.search_agent_skill_item import SearchAgentSkillItem

# TODO update the JSON string below
json = "{}"
# create an instance of SearchAgentSkillItem from a JSON string
search_agent_skill_item_instance = SearchAgentSkillItem.from_json(json)
# print the JSON string representation of the object
print(SearchAgentSkillItem.to_json())

# convert the object into a dict
search_agent_skill_item_dict = search_agent_skill_item_instance.to_dict()
# create an instance of SearchAgentSkillItem from a dict
search_agent_skill_item_from_dict = SearchAgentSkillItem.from_dict(search_agent_skill_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


