# SuccessEnvelopeSearchData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Request trace id (peer to data) | 
**data** | [**SearchData**](SearchData.md) | Endpoint-defined business result | 

## Example

```python
from everos_cloud_sdk.models.success_envelope_search_data import SuccessEnvelopeSearchData

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessEnvelopeSearchData from a JSON string
success_envelope_search_data_instance = SuccessEnvelopeSearchData.from_json(json)
# print the JSON string representation of the object
print(SuccessEnvelopeSearchData.to_json())

# convert the object into a dict
success_envelope_search_data_dict = success_envelope_search_data_instance.to_dict()
# create an instance of SuccessEnvelopeSearchData from a dict
success_envelope_search_data_from_dict = SuccessEnvelopeSearchData.from_dict(success_envelope_search_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


