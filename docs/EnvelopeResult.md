# EnvelopeResult

The response payload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional] 

## Example

```python
from everos_cloud.models.envelope_result import EnvelopeResult

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeResult from a JSON string
envelope_result_instance = EnvelopeResult.from_json(json)
# print the JSON string representation of the object
print(EnvelopeResult.to_json())

# convert the object into a dict
envelope_result_dict = envelope_result_instance.to_dict()
# create an instance of EnvelopeResult from a dict
envelope_result_from_dict = EnvelopeResult.from_dict(envelope_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


