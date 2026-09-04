# SearchInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | Scope to search in, defaulting to \&quot;default\&quot;. Must match the pair used on write. | [optional] [default to 'default']
**project_id** | **str** | Second half of the scope, defaulting to \&quot;default\&quot;. | [optional] [default to 'default']
**user_id** | **str** |  | [optional] 
**agent_id** | **str** |  | [optional] 
**query** | **str** | The natural-language query to retrieve against. | 
**method** | **str** | Retrieval strategy. \&quot;keyword\&quot; is lexical, \&quot;vector\&quot; is embedding similarity, \&quot;hybrid\&quot; (default) combines both, and \&quot;agentic\&quot; lets the engine run a multi-round LLM-guided retrieval — more thorough, slower. | [optional] [default to 'hybrid']
**top_k** | **int** | Maximum number of hits. Either -1 (the default, letting the engine decide) or a value from 1 to 100; anything else is rejected with 422. | [optional] [default to -1]
**radius** | **float** |  | [optional] 
**min_score** | **float** |  | [optional] 
**include_profile** | **bool** | Also return the user&#39;s profile alongside the hits, saving a second call. Ignored for an agent owner, whose results carry no profiles. | [optional] [default to False]
**with_readable_episode** | **bool** | Attach a human-readable rendering of each episode to the returned items, for display only — it is not indexed, filterable or scored, and callers fall back to &#x60;episode&#x60; when it is null. Ignored for an agent owner. | [optional] [default to False]
**enable_llm_rerank** | **bool** | Opt-in LLM rerank, and only for hybrid agent_case / agent_skill retrieval. The episode hybrid path has its own fact eviction and ignores this, as do keyword, vector and agentic. | [optional] [default to False]
**filters** | [**FilterNode**](FilterNode.md) |  | [optional] 

## Example

```python
from everos_cloud.models.search_input import SearchInput

# TODO update the JSON string below
json = "{}"
# create an instance of SearchInput from a JSON string
search_input_instance = SearchInput.from_json(json)
# print the JSON string representation of the object
print(SearchInput.to_json())

# convert the object into a dict
search_input_dict = search_input_instance.to_dict()
# create an instance of SearchInput from a dict
search_input_from_dict = SearchInput.from_dict(search_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


