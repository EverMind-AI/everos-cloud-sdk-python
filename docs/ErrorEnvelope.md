# ErrorEnvelope

v1 error envelope (spec §1): ``{request_id, error:{code,message}}``.  Used by ``global_exception_handler`` for both HTTPException (carrying the domain code via ``InvocationHttpError``) and unhandled exceptions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Request trace id | 
**error** | [**ErrorBody**](ErrorBody.md) | Error detail (code + message) | 

## Example

```python
from everos_cloud.models.error_envelope import ErrorEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorEnvelope from a JSON string
error_envelope_instance = ErrorEnvelope.from_json(json)
# print the JSON string representation of the object
print(ErrorEnvelope.to_json())

# convert the object into a dict
error_envelope_dict = error_envelope_instance.to_dict()
# create an instance of ErrorEnvelope from a dict
error_envelope_from_dict = ErrorEnvelope.from_dict(error_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


