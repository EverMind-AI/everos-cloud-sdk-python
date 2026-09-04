# SignObjectItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | Your own id for this file. It comes back on the matching response item. | 
**file_name** | **str** | The file&#39;s name, used to derive its type and preserved for display. | 
**file_type** | **str** | Media class. Default size limits per type: image&#x3D;10MB, file&#x3D;100MB, video&#x3D;500MB. These are defaults and may be overridden per token (via the token&#39;s &#x60;file_limits&#x60;); the effective limit is enforced by S3 through the presigned POST &#x60;content-length-range&#x60; condition, and surfaced as &#x60;objectSignedInfo.maxSize&#x60;.  | 

## Example

```python
from everos_cloud.models.sign_object_item import SignObjectItem

# TODO update the JSON string below
json = "{}"
# create an instance of SignObjectItem from a JSON string
sign_object_item_instance = SignObjectItem.from_json(json)
# print the JSON string representation of the object
print(SignObjectItem.to_json())

# convert the object into a dict
sign_object_item_dict = sign_object_item_instance.to_dict()
# create an instance of SignObjectItem from a dict
sign_object_item_from_dict = SignObjectItem.from_dict(sign_object_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


