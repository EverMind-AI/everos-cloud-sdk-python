# ContentItem

A single content element (appendix A). Current phase: only ``type=\"text\"``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | What this item is: \&quot;text\&quot;, \&quot;image\&quot;, \&quot;audio\&quot;, \&quot;doc\&quot;, \&quot;pdf\&quot;, \&quot;html\&quot; or \&quot;email\&quot;. It selects how the content is parsed, so it must match the payload. | 
**text** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**var_base64** | **str** |  | [optional] 
**uri** | **str** |  | [optional] 
**ext** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**source_info** | **Dict[str, object]** |  | [optional] 
**extras** | **Dict[str, object]** |  | [optional] 

## Example

```python
from everos_cloud.models.content_item import ContentItem

# TODO update the JSON string below
json = "{}"
# create an instance of ContentItem from a JSON string
content_item_instance = ContentItem.from_json(json)
# print the JSON string representation of the object
print(ContentItem.to_json())

# convert the object into a dict
content_item_dict = content_item_instance.to_dict()
# create an instance of ContentItem from a dict
content_item_from_dict = ContentItem.from_dict(content_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


