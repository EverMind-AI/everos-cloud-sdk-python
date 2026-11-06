# PurgeStepData

One store of one purge step, e.g. ``mongo:v2_episodes`` or ``es:episode``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store** | **str** |  | 
**state** | **str** |  | 
**deleted** | **int** |  | [optional] [default to 0]
**error** | **str** |  | [optional] 

## Example

```python
from everos_cloud.models.purge_step_data import PurgeStepData

# TODO update the JSON string below
json = "{}"
# create an instance of PurgeStepData from a JSON string
purge_step_data_instance = PurgeStepData.from_json(json)
# print the JSON string representation of the object
print(PurgeStepData.to_json())

# convert the object into a dict
purge_step_data_dict = purge_step_data_instance.to_dict()
# create an instance of PurgeStepData from a dict
purge_step_data_from_dict = PurgeStepData.from_dict(purge_step_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


