# SuccessEnvelopeRebuildStatusData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Request trace id (peer to data) | 
**data** | [**RebuildStatusData**](RebuildStatusData.md) | Endpoint-defined business result | 

## Example

```python
from everos_cloud.models.success_envelope_rebuild_status_data import SuccessEnvelopeRebuildStatusData

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessEnvelopeRebuildStatusData from a JSON string
success_envelope_rebuild_status_data_instance = SuccessEnvelopeRebuildStatusData.from_json(json)
# print the JSON string representation of the object
print(SuccessEnvelopeRebuildStatusData.to_json())

# convert the object into a dict
success_envelope_rebuild_status_data_dict = success_envelope_rebuild_status_data_instance.to_dict()
# create an instance of SuccessEnvelopeRebuildStatusData from a dict
success_envelope_rebuild_status_data_from_dict = SuccessEnvelopeRebuildStatusData.from_dict(success_envelope_rebuild_status_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


