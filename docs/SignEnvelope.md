# SignEnvelope

Response envelope for the sign endpoint. The `result.data` shape depends on `status`:  - `status: 0` (success) — `result.data` is a `SignResponse`, as   modelled below. - `status: 2018` (validation failed) — `result.data` is a plain   string carrying the validator error message, not a `SignResponse`. - all other non-zero statuses — `result.data` is `null`.  Generated clients should treat `result.data` as populated only when `status` is 0. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | &#x60;\&quot;OK\&quot;&#x60; on success, otherwise a human-readable error message decoded from the business error.  | [optional] 
**request_id** | **str** | Id of this request — quote it when reporting a problem. | [optional] 
**status** | **int** | Business status code; 0 means success | [optional] 
**result** | [**SignEnvelopeAllOfResult**](SignEnvelopeAllOfResult.md) |  | [optional] 

## Example

```python
from everos_cloud.models.sign_envelope import SignEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SignEnvelope from a JSON string
sign_envelope_instance = SignEnvelope.from_json(json)
# print the JSON string representation of the object
print(SignEnvelope.to_json())

# convert the object into a dict
sign_envelope_dict = sign_envelope_instance.to_dict()
# create an instance of SignEnvelope from a dict
sign_envelope_from_dict = SignEnvelope.from_dict(sign_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


