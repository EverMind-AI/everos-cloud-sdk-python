# SearchAgentCaseItem


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
**score** | **float** |  | 

## Example

```python
from everos_cloud.models.search_agent_case_item import SearchAgentCaseItem

# TODO update the JSON string below
json = "{}"
# create an instance of SearchAgentCaseItem from a JSON string
search_agent_case_item_instance = SearchAgentCaseItem.from_json(json)
# print the JSON string representation of the object
print(SearchAgentCaseItem.to_json())

# convert the object into a dict
search_agent_case_item_dict = search_agent_case_item_instance.to_dict()
# create an instance of SearchAgentCaseItem from a dict
search_agent_case_item_from_dict = SearchAgentCaseItem.from_dict(search_agent_case_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


