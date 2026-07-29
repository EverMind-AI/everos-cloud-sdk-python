# SignRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_list** | [**List[SignObjectItem]**](SignObjectItem.md) | Objects to sign for upload. At most 50 per request (&#x60;status: 1007&#x60; if exceeded). Each &#x60;fileId&#x60; must be unique within the request (&#x60;status: 1009&#x60; on duplicates).  | 

## Example

```python
from everos_cloud.models.sign_request import SignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SignRequest from a JSON string
sign_request_instance = SignRequest.from_json(json)
# print the JSON string representation of the object
print(SignRequest.to_json())

# convert the object into a dict
sign_request_dict = sign_request_instance.to_dict()
# create an instance of SignRequest from a dict
sign_request_from_dict = SignRequest.from_dict(sign_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


