# PurgeRequestData

The nonce to confirm, and what it will purge.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nonce** | **str** | Send to /purge/confirm before &#x60;expires_at&#x60;. | 
**expires_at** | **datetime** |  | 
**scope** | **str** |  | 
**app_id** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**summary** | [**PurgeSummary**](PurgeSummary.md) |  | 

## Example

```python
from everos_cloud.models.purge_request_data import PurgeRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of PurgeRequestData from a JSON string
purge_request_data_instance = PurgeRequestData.from_json(json)
# print the JSON string representation of the object
print(PurgeRequestData.to_json())

# convert the object into a dict
purge_request_data_dict = purge_request_data_instance.to_dict()
# create an instance of PurgeRequestData from a dict
purge_request_data_from_dict = PurgeRequestData.from_dict(purge_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


