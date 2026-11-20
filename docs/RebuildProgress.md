# RebuildProgress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**units_total** | **int** | Work items the job fanned out | 
**units_done** | **int** | Work items finished | 
**episodes_fed** | **int** | Episodes the profile rebuild has read so far | [optional] [default to 0]
**estimated_episodes** | **int** | Episodes the profile rebuild reads in total (approx.) | [optional] [default to 0]

## Example

```python
from everos_cloud.models.rebuild_progress import RebuildProgress

# TODO update the JSON string below
json = "{}"
# create an instance of RebuildProgress from a JSON string
rebuild_progress_instance = RebuildProgress.from_json(json)
# print the JSON string representation of the object
print(RebuildProgress.to_json())

# convert the object into a dict
rebuild_progress_dict = rebuild_progress_instance.to_dict()
# create an instance of RebuildProgress from a dict
rebuild_progress_from_dict = RebuildProgress.from_dict(rebuild_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


