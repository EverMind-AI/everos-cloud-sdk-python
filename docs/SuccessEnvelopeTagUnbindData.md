# SuccessEnvelopeTagUnbindData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Request trace id (peer to data) | 
**data** | [**TagUnbindData**](TagUnbindData.md) | Endpoint-defined business result | 

## Example

```python
from everos_cloud.models.success_envelope_tag_unbind_data import SuccessEnvelopeTagUnbindData

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessEnvelopeTagUnbindData from a JSON string
success_envelope_tag_unbind_data_instance = SuccessEnvelopeTagUnbindData.from_json(json)
# print the JSON string representation of the object
print(SuccessEnvelopeTagUnbindData.to_json())

# convert the object into a dict
success_envelope_tag_unbind_data_dict = success_envelope_tag_unbind_data_instance.to_dict()
# create an instance of SuccessEnvelopeTagUnbindData from a dict
success_envelope_tag_unbind_data_from_dict = SuccessEnvelopeTagUnbindData.from_dict(success_envelope_tag_unbind_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


