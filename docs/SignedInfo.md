# SignedInfo

Presigned POST form data for direct-to-S3 upload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL to POST the file to. | [optional] 
**fields** | **Dict[str, str]** | Form fields that must accompany the upload, exactly as given, with the file itself last. | [optional] 
**max_size** | **int** | Maximum file size in bytes | [optional] 

## Example

```python
from everos_cloud.models.signed_info import SignedInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SignedInfo from a JSON string
signed_info_instance = SignedInfo.from_json(json)
# print the JSON string representation of the object
print(SignedInfo.to_json())

# convert the object into a dict
signed_info_dict = signed_info_instance.to_dict()
# create an instance of SignedInfo from a dict
signed_info_from_dict = SignedInfo.from_dict(signed_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


