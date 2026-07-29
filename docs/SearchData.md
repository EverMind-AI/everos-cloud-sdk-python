# SearchData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**episodes** | [**List[SearchEpisodeItem]**](SearchEpisodeItem.md) |  | [optional] 
**profiles** | [**List[SearchProfileItem]**](SearchProfileItem.md) |  | [optional] 
**agent_cases** | [**List[SearchAgentCaseItem]**](SearchAgentCaseItem.md) |  | [optional] 
**agent_skills** | [**List[SearchAgentSkillItem]**](SearchAgentSkillItem.md) |  | [optional] 
**unprocessed_messages** | [**List[UnprocessedMessageDTO]**](UnprocessedMessageDTO.md) |  | [optional] 

## Example

```python
from everos_cloud.models.search_data import SearchData

# TODO update the JSON string below
json = "{}"
# create an instance of SearchData from a JSON string
search_data_instance = SearchData.from_json(json)
# print the JSON string representation of the object
print(SearchData.to_json())

# convert the object into a dict
search_data_dict = search_data_instance.to_dict()
# create an instance of SearchData from a dict
search_data_from_dict = SearchData.from_dict(search_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


