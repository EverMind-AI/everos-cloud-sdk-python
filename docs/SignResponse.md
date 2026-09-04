# SignResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_list** | [**List[SignResponseItem]**](SignResponseItem.md) | One signed entry per requested file, in the same order. | [optional] 

## Example

```python
from everos_cloud.models.sign_response import SignResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SignResponse from a JSON string
sign_response_instance = SignResponse.from_json(json)
# print the JSON string representation of the object
print(SignResponse.to_json())

# convert the object into a dict
sign_response_dict = sign_response_instance.to_dict()
# create an instance of SignResponse from a dict
sign_response_from_dict = SignResponse.from_dict(sign_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


