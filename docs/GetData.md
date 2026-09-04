# GetData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**episodes** | [**List[EpisodeItem]**](EpisodeItem.md) | Episodes, when &#x60;memory_type&#x60; was \&quot;episode\&quot;. Empty otherwise. | [optional] 
**profiles** | [**List[ProfileItem]**](ProfileItem.md) | Profiles, when &#x60;memory_type&#x60; was \&quot;profile\&quot;. Empty otherwise. | [optional] 
**agent_cases** | [**List[AgentCaseItem]**](AgentCaseItem.md) | Agent cases, when &#x60;memory_type&#x60; was \&quot;agent_case\&quot;. Empty otherwise. | [optional] 
**agent_skills** | [**List[AgentSkillItem]**](AgentSkillItem.md) | Agent skills, when &#x60;memory_type&#x60; was \&quot;agent_skill\&quot;. Empty otherwise. | [optional] 
**total_count** | **int** | How many memories match the request in total, across all pages. | [optional] [default to 0]
**count** | **int** | How many are in this page. | [optional] [default to 0]

## Example

```python
from everos_cloud.models.get_data import GetData

# TODO update the JSON string below
json = "{}"
# create an instance of GetData from a JSON string
get_data_instance = GetData.from_json(json)
# print the JSON string representation of the object
print(GetData.to_json())

# convert the object into a dict
get_data_dict = get_data_instance.to_dict()
# create an instance of GetData from a dict
get_data_from_dict = GetData.from_dict(get_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


