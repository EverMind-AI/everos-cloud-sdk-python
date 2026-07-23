# SignEnvelopeAllOfResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SignResponse**](SignResponse.md) |  | [optional] 

## Example

```python
from everos_cloud_sdk.models.sign_envelope_all_of_result import SignEnvelopeAllOfResult

# TODO update the JSON string below
json = "{}"
# create an instance of SignEnvelopeAllOfResult from a JSON string
sign_envelope_all_of_result_instance = SignEnvelopeAllOfResult.from_json(json)
# print the JSON string representation of the object
print(SignEnvelopeAllOfResult.to_json())

# convert the object into a dict
sign_envelope_all_of_result_dict = sign_envelope_all_of_result_instance.to_dict()
# create an instance of SignEnvelopeAllOfResult from a dict
sign_envelope_all_of_result_from_dict = SignEnvelopeAllOfResult.from_dict(sign_envelope_all_of_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


