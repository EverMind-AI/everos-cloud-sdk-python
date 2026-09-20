# SuccessEnvelopeUpdateData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Request trace id (peer to data) | 
**data** | [**UpdateData**](UpdateData.md) | Endpoint-defined business result | 

## Example

```python
from everos_cloud.models.success_envelope_update_data import SuccessEnvelopeUpdateData

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessEnvelopeUpdateData from a JSON string
success_envelope_update_data_instance = SuccessEnvelopeUpdateData.from_json(json)
# print the JSON string representation of the object
print(SuccessEnvelopeUpdateData.to_json())

# convert the object into a dict
success_envelope_update_data_dict = success_envelope_update_data_instance.to_dict()
# create an instance of SuccessEnvelopeUpdateData from a dict
success_envelope_update_data_from_dict = SuccessEnvelopeUpdateData.from_dict(success_envelope_update_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


