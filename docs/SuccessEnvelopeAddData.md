# SuccessEnvelopeAddData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Request trace id (peer to data) | 
**data** | [**AddData**](AddData.md) | Endpoint-defined business result | 

## Example

```python
from everos_cloud_sdk.models.success_envelope_add_data import SuccessEnvelopeAddData

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessEnvelopeAddData from a JSON string
success_envelope_add_data_instance = SuccessEnvelopeAddData.from_json(json)
# print the JSON string representation of the object
print(SuccessEnvelopeAddData.to_json())

# convert the object into a dict
success_envelope_add_data_dict = success_envelope_add_data_instance.to_dict()
# create an instance of SuccessEnvelopeAddData from a dict
success_envelope_add_data_from_dict = SuccessEnvelopeAddData.from_dict(success_envelope_add_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


