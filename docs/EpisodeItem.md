# EpisodeItem


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
**atomic_facts** | [**List[AtomicFactItem]**](AtomicFactItem.md) | The individual facts extracted from this episode, nested rather than returned separately. | [optional] 
**tags** | **List[str]** | Tags attached through /api/v2/memory/tag/*. | [optional] 

## Example

```python
from everos_cloud.models.episode_item import EpisodeItem

# TODO update the JSON string below
json = "{}"
# create an instance of EpisodeItem from a JSON string
episode_item_instance = EpisodeItem.from_json(json)
# print the JSON string representation of the object
print(EpisodeItem.to_json())

# convert the object into a dict
episode_item_dict = episode_item_instance.to_dict()
# create an instance of EpisodeItem from a dict
episode_item_from_dict = EpisodeItem.from_dict(episode_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


