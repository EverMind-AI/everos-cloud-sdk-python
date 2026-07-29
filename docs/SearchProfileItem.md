# SearchProfileItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**app_id** | **str** |  | 
**project_id** | **str** |  | 
**user_id** | **str** |  | 
**profile_data** | **Dict[str, object]** |  | [optional] 
**score** | **float** |  | [optional] 

## Example

```python
from everos_cloud.models.search_profile_item import SearchProfileItem

# TODO update the JSON string below
json = "{}"
# create an instance of SearchProfileItem from a JSON string
search_profile_item_instance = SearchProfileItem.from_json(json)
# print the JSON string representation of the object
print(SearchProfileItem.to_json())

# convert the object into a dict
search_profile_item_dict = search_profile_item_instance.to_dict()
# create an instance of SearchProfileItem from a dict
search_profile_item_from_dict = SearchProfileItem.from_dict(search_profile_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


