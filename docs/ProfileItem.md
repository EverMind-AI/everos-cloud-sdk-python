# ProfileItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Profile id. | 
**app_id** | **str** | The business-semantic scope this profile was written under. | 
**project_id** | **str** | Second half of that scope. | 
**user_id** | **str** | The user this profile describes. | 
**profile_data** | **Dict[str, object]** | The profile itself — the explicit_info and implicit_traits items maintained by extraction and by /api/v2/memory/edit. Each item&#39;s id is what an edit operation targets. | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from everos_cloud.models.profile_item import ProfileItem

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileItem from a JSON string
profile_item_instance = ProfileItem.from_json(json)
# print the JSON string representation of the object
print(ProfileItem.to_json())

# convert the object into a dict
profile_item_dict = profile_item_instance.to_dict()
# create an instance of ProfileItem from a dict
profile_item_from_dict = ProfileItem.from_dict(profile_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


