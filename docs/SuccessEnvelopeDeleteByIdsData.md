# SuccessEnvelopeDeleteByIdsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Request trace id (peer to data) | 
**data** | [**DeleteByIdsData**](DeleteByIdsData.md) | Endpoint-defined business result | 

## Example

```python
from everos_cloud.models.success_envelope_delete_by_ids_data import SuccessEnvelopeDeleteByIdsData

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessEnvelopeDeleteByIdsData from a JSON string
success_envelope_delete_by_ids_data_instance = SuccessEnvelopeDeleteByIdsData.from_json(json)
# print the JSON string representation of the object
print(SuccessEnvelopeDeleteByIdsData.to_json())

# convert the object into a dict
success_envelope_delete_by_ids_data_dict = success_envelope_delete_by_ids_data_instance.to_dict()
# create an instance of SuccessEnvelopeDeleteByIdsData from a dict
success_envelope_delete_by_ids_data_from_dict = SuccessEnvelopeDeleteByIdsData.from_dict(success_envelope_delete_by_ids_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


