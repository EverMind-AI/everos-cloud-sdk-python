# SuccessEnvelopeKbDeleteData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Request trace id (peer to data) | 
**data** | [**KbDeleteData**](KbDeleteData.md) | Endpoint-defined business result | 

## Example

```python
from everos_cloud.models.success_envelope_kb_delete_data import SuccessEnvelopeKbDeleteData

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessEnvelopeKbDeleteData from a JSON string
success_envelope_kb_delete_data_instance = SuccessEnvelopeKbDeleteData.from_json(json)
# print the JSON string representation of the object
print(SuccessEnvelopeKbDeleteData.to_json())

# convert the object into a dict
success_envelope_kb_delete_data_dict = success_envelope_kb_delete_data_instance.to_dict()
# create an instance of SuccessEnvelopeKbDeleteData from a dict
success_envelope_kb_delete_data_from_dict = SuccessEnvelopeKbDeleteData.from_dict(success_envelope_kb_delete_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


