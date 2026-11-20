# RebuildInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | [optional] [default to 'default']
**project_id** | **str** |  | [optional] [default to 'default']
**user_id** | **str** |  | [optional] 
**agent_id** | **str** |  | [optional] 
**targets** | **List[str]** |  | [optional] 
**force** | **bool** | Rebuild the profile / every skill cluster even when nothing is marked stale. Session summaries are only rebuilt when marked. | [optional] [default to False]
**dry_run** | **bool** | Report what would be rebuilt; start no job and spend nothing. | [optional] [default to False]

## Example

```python
from everos_cloud.models.rebuild_input import RebuildInput

# TODO update the JSON string below
json = "{}"
# create an instance of RebuildInput from a JSON string
rebuild_input_instance = RebuildInput.from_json(json)
# print the JSON string representation of the object
print(RebuildInput.to_json())

# convert the object into a dict
rebuild_input_dict = rebuild_input_instance.to_dict()
# create an instance of RebuildInput from a dict
rebuild_input_from_dict = RebuildInput.from_dict(rebuild_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


