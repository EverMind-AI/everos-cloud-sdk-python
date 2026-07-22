# SuccessEnvelopeGetData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Request trace id (peer to data) | 
**data** | [**GetData**](GetData.md) | Endpoint-defined business result | 

## Example

```python
from everos_cloud_sdk.models.success_envelope_get_data import SuccessEnvelopeGetData

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessEnvelopeGetData from a JSON string
success_envelope_get_data_instance = SuccessEnvelopeGetData.from_json(json)
# print the JSON string representation of the object
print(SuccessEnvelopeGetData.to_json())

# convert the object into a dict
success_envelope_get_data_dict = success_envelope_get_data_instance.to_dict()
# create an instance of SuccessEnvelopeGetData from a dict
success_envelope_get_data_from_dict = SuccessEnvelopeGetData.from_dict(success_envelope_get_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


