# PurgeRequestInput

Step 1: ask for a purge. Nothing is deleted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | &#x60;space&#x60; purges the whole memory space; &#x60;app&#x60; one app in it (&#x60;app_id&#x60;); &#x60;project&#x60; one project of one app (&#x60;app_id&#x60; + &#x60;project_id&#x60;). | 
**app_id** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 

## Example

```python
from everos_cloud.models.purge_request_input import PurgeRequestInput

# TODO update the JSON string below
json = "{}"
# create an instance of PurgeRequestInput from a JSON string
purge_request_input_instance = PurgeRequestInput.from_json(json)
# print the JSON string representation of the object
print(PurgeRequestInput.to_json())

# convert the object into a dict
purge_request_input_dict = purge_request_input_instance.to_dict()
# create an instance of PurgeRequestInput from a dict
purge_request_input_from_dict = PurgeRequestInput.from_dict(purge_request_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


