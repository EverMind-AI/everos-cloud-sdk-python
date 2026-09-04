# SearchAgentSkillItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Agent-skill id. | 
**app_id** | **str** | The business-semantic scope this skill was written under. | 
**project_id** | **str** | Second half of that scope. | 
**agent_id** | **str** | The agent that owns this skill. | 
**name** | **str** | The skill&#39;s name. | 
**description** | **str** | What the skill is for, in a sentence. | 
**content** | **str** | The skill itself — the reusable procedure, ready to put in a prompt. | 
**confidence** | **float** | How much the distillation trusts this skill. Nominally 0.0–1.0, defaulting to 0.0 before anything scores it; the range is not enforced on the write path. Nothing in retrieval filters on it today, and how it divides labour with &#x60;maturity_score&#x60; is still open — so do not build a threshold on it yet. | 
**maturity_score** | **float** | How well-established the skill is. Nominally 0.0–1.0 and unenforced, and — unlike the other two scores — its default is 0.6 rather than 0.0, chosen so an unscored skill starts mid-optimistic. The cost is that an unscored 0.6 is indistinguishable from a scored 0.6: there is no \&quot;not evaluated\&quot; sentinel, and maturity scoring is skipped by default. Filtering near 0.6 is therefore unreliable. | 
**source_case_ids** | **List[str]** | The agent cases this skill was distilled from. Fetch them for the underlying evidence. | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**score** | **float** | Relevance of this skill to the query. | 

## Example

```python
from everos_cloud.models.search_agent_skill_item import SearchAgentSkillItem

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


