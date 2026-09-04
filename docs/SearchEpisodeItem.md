# SearchEpisodeItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Episode id. Use it to bind tags or to fetch this episode again. | 
**app_id** | **str** | The business-semantic scope this memory was written under. | 
**project_id** | **str** | Second half of that scope. | 
**user_id** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 
**timestamp** | **datetime** | When the remembered exchange happened (ISO 8601), not when it was extracted. | 
**sender_ids** | **List[str]** | The senders that appear in the source exchange. | [optional] 
**summary** | **str** | Short summary of the episode — what a result list should show. | 
**subject** | **str** | What the episode is about, in a few words. | 
**episode** | **str** | The episode&#39;s stored narrative body. This is the indexed, searchable text. | 
**readable_episode** | **str** |  | [optional] 
**type** | **str** | How the episode was produced — \&quot;Conversation\&quot; or \&quot;AgentConversation\&quot;. | 
**atomic_facts** | [**List[SearchAtomicFactItem]**](SearchAtomicFactItem.md) | The facts extracted from this episode, each with its own relevance score. | [optional] 
**tags** | **List[str]** | Tags attached through /api/v2/memory/tag/*. | [optional] 
**score** | **float** | Relevance of this episode to the query. What the number means depends on &#x60;method&#x60;: the hybrid path fuses its two routes into a probability in 0.0–1.0 (which is what &#x60;min_score&#x60; filters on), while keyword and vector pass the underlying engine&#39;s own score through — BM25 has no upper bound and vector similarity depends on the metric. So compare scores within one method, not across methods. | 

## Example

```python
from everos_cloud.models.search_episode_item import SearchEpisodeItem

# TODO update the JSON string below
json = "{}"
# create an instance of SearchEpisodeItem from a JSON string
search_episode_item_instance = SearchEpisodeItem.from_json(json)
# print the JSON string representation of the object
print(SearchEpisodeItem.to_json())

# convert the object into a dict
search_episode_item_dict = search_episode_item_instance.to_dict()
# create an instance of SearchEpisodeItem from a dict
search_episode_item_from_dict = SearchEpisodeItem.from_dict(search_episode_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


