# Envelope

Common response envelope

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | &#x60;\&quot;OK\&quot;&#x60; on success, otherwise a human-readable error message decoded from the business error.  | [optional] 
**request_id** | **str** |  | [optional] 
**status** | **int** | Business status code; 0 means success | [optional] 
**result** | [**EnvelopeResult**](EnvelopeResult.md) |  | [optional] 

## Example

```python
from everos_cloud_sdk.models.envelope import Envelope

# TODO update the JSON string below
json = "{}"
# create an instance of Envelope from a JSON string
envelope_instance = Envelope.from_json(json)
# print the JSON string representation of the object
print(Envelope.to_json())

# convert the object into a dict
envelope_dict = envelope_instance.to_dict()
# create an instance of Envelope from a dict
envelope_from_dict = Envelope.from_dict(envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


