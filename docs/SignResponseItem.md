# SignResponseItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | The id you supplied for this file. | [optional] 
**file_name** | **str** | The file&#39;s name, echoed back. | [optional] 
**file_type** | **str** | The type the service resolved for it. | [optional] 
**object_key** | **str** | The stored object&#39;s key — this is the value to pass later as a content &#x60;uri&#x60; on /api/v2/memory/add or a document ingest. | [optional] 
**object_url** | **str** | Present in the response struct for parity with the find endpoint, but not populated on the sign path (omitted from the JSON).  | [optional] 
**object_signed_info** | [**SignedInfo**](SignedInfo.md) | Where and how to upload the bytes. | [optional] 

## Example

```python
from everos_cloud.models.sign_response_item import SignResponseItem

# TODO update the JSON string below
json = "{}"
# create an instance of SignResponseItem from a JSON string
sign_response_item_instance = SignResponseItem.from_json(json)
# print the JSON string representation of the object
print(SignResponseItem.to_json())

# convert the object into a dict
sign_response_item_dict = sign_response_item_instance.to_dict()
# create an instance of SignResponseItem from a dict
sign_response_item_from_dict = SignResponseItem.from_dict(sign_response_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


