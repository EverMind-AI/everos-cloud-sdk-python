# SuccessEnvelopeFlushData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Request trace id (peer to data) | 
**data** | [**FlushData**](FlushData.md) | Endpoint-defined business result | 

## Example

```python
from everos_cloud_sdk.models.success_envelope_flush_data import SuccessEnvelopeFlushData

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessEnvelopeFlushData from a JSON string
success_envelope_flush_data_instance = SuccessEnvelopeFlushData.from_json(json)
# print the JSON string representation of the object
print(SuccessEnvelopeFlushData.to_json())

# convert the object into a dict
success_envelope_flush_data_dict = success_envelope_flush_data_instance.to_dict()
# create an instance of SuccessEnvelopeFlushData from a dict
success_envelope_flush_data_from_dict = SuccessEnvelopeFlushData.from_dict(success_envelope_flush_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


