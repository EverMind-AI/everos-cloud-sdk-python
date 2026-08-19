# SuccessEnvelopeKbListData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Request trace id (peer to data) | 
**data** | [**KbListData**](KbListData.md) | Endpoint-defined business result | 

## Example

```python
from everos_cloud.models.success_envelope_kb_list_data import SuccessEnvelopeKbListData

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessEnvelopeKbListData from a JSON string
success_envelope_kb_list_data_instance = SuccessEnvelopeKbListData.from_json(json)
# print the JSON string representation of the object
print(SuccessEnvelopeKbListData.to_json())

# convert the object into a dict
success_envelope_kb_list_data_dict = success_envelope_kb_list_data_instance.to_dict()
# create an instance of SuccessEnvelopeKbListData from a dict
success_envelope_kb_list_data_from_dict = SuccessEnvelopeKbListData.from_dict(success_envelope_kb_list_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


