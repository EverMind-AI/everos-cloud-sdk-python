# GetData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**episodes** | [**List[EpisodeItem]**](EpisodeItem.md) |  | [optional] 
**profiles** | [**List[ProfileItem]**](ProfileItem.md) |  | [optional] 
**agent_cases** | [**List[AgentCaseItem]**](AgentCaseItem.md) |  | [optional] 
**agent_skills** | [**List[AgentSkillItem]**](AgentSkillItem.md) |  | [optional] 
**total_count** | **int** |  | [optional] [default to 0]
**count** | **int** |  | [optional] [default to 0]

## Example

```python
from everos_cloud_sdk.models.get_data import GetData

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


