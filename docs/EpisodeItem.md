# EpisodeItem


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
**atomic_facts** | [**List[AtomicFactItem]**](AtomicFactItem.md) |  | [optional] 

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


