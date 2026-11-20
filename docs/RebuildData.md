# RebuildData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**status** | **str** | queued: a job was started. already_running: the owner&#39;s running job is returned instead of starting another. nothing_to_do: nothing is marked stale (and force is false). dry_run: what would be rebuilt. | 
**targets** | **List[str]** | What the job rebuilds (or would) | [optional] 
**estimated_episodes** | **int** | Episodes a profile rebuild re-reads (a cost hint; 0 without profile) | [optional] [default to 0]

## Example

```python
from everos_cloud.models.rebuild_data import RebuildData

# TODO update the JSON string below
json = "{}"
# create an instance of RebuildData from a JSON string
rebuild_data_instance = RebuildData.from_json(json)
# print the JSON string representation of the object
print(RebuildData.to_json())

# convert the object into a dict
rebuild_data_dict = rebuild_data_instance.to_dict()
# create an instance of RebuildData from a dict
rebuild_data_from_dict = RebuildData.from_dict(rebuild_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


