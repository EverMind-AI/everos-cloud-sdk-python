# SearchEpisodeItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**app_id** | **str** |  | 
**project_id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | 
**sender_ids** | **List[str]** |  | [optional] 
**summary** | **str** |  | 
**subject** | **str** |  | 
**episode** | **str** |  | 
**type** | **str** |  | 
**atomic_facts** | [**List[SearchAtomicFactItem]**](SearchAtomicFactItem.md) |  | [optional] 
**score** | **float** |  | 

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


