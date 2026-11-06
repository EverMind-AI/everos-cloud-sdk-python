# SuccessEnvelopePurgeRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Request trace id (peer to data) | 
**data** | [**PurgeRequestData**](PurgeRequestData.md) | Endpoint-defined business result | 

## Example

```python
from everos_cloud.models.success_envelope_purge_request_data import SuccessEnvelopePurgeRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessEnvelopePurgeRequestData from a JSON string
success_envelope_purge_request_data_instance = SuccessEnvelopePurgeRequestData.from_json(json)
# print the JSON string representation of the object
print(SuccessEnvelopePurgeRequestData.to_json())

# convert the object into a dict
success_envelope_purge_request_data_dict = success_envelope_purge_request_data_instance.to_dict()
# create an instance of SuccessEnvelopePurgeRequestData from a dict
success_envelope_purge_request_data_from_dict = SuccessEnvelopePurgeRequestData.from_dict(success_envelope_purge_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


