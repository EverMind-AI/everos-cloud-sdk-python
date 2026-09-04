# SearchAgentCaseItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Agent-case id. | 
**app_id** | **str** | The business-semantic scope this case was written under. | 
**project_id** | **str** | Second half of that scope. | 
**agent_id** | **str** | The agent that owns this case. | 
**session_id** | **str** | The session whose trajectory the case was distilled from. | 
**task_intent** | **str** | What the agent was trying to do in that trajectory. | 
**approach** | **str** | How it went about it — the reusable part of the case. | 
**quality_score** | **float** | How good this case is judged to be. Nominally 0.0–1.0 with 0.5 as the no-opinion default, but the value is the extractor&#39;s own and nothing on the write path enforces the range — treat an out-of-range number as possible. One threshold is real: a case scoring below 0.2 is never distilled into a skill. | 
**key_insight** | **str** |  | [optional] 
**timestamp** | **datetime** | When the trajectory happened (ISO 8601). | 
**score** | **float** | Relevance of this case to the query. | 

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


