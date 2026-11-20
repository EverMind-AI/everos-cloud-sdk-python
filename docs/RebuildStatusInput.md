# RebuildStatusInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | From /memory/rebuild | 

## Example

```python
from everos_cloud.models.rebuild_status_input import RebuildStatusInput

# TODO update the JSON string below
json = "{}"
# create an instance of RebuildStatusInput from a JSON string
rebuild_status_input_instance = RebuildStatusInput.from_json(json)
# print the JSON string representation of the object
print(RebuildStatusInput.to_json())

# convert the object into a dict
rebuild_status_input_dict = rebuild_status_input_instance.to_dict()
# create an instance of RebuildStatusInput from a dict
rebuild_status_input_from_dict = RebuildStatusInput.from_dict(rebuild_status_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


