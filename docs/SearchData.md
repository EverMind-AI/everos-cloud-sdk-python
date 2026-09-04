# SearchData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**episodes** | [**List[SearchEpisodeItem]**](SearchEpisodeItem.md) | Matching episodes, for a user owner. Always present, empty when not applicable. | [optional] 
**profiles** | [**List[SearchProfileItem]**](SearchProfileItem.md) | The user&#39;s profile, when &#x60;include_profile&#x60; asked for it. | [optional] 
**agent_cases** | [**List[SearchAgentCaseItem]**](SearchAgentCaseItem.md) | Matching agent cases, for an agent owner. | [optional] 
**agent_skills** | [**List[SearchAgentSkillItem]**](SearchAgentSkillItem.md) | Matching agent skills, for an agent owner. | [optional] 
**unprocessed_messages** | [**List[UnprocessedMessageDTO]**](UnprocessedMessageDTO.md) | Raw buffered messages not yet extracted. Returned only when the request filtered on a single &#x60;session_id&#x60;, so a caller can see what is still in flight. | [optional] 

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


