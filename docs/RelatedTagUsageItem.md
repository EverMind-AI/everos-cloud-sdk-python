# RelatedTagUsageItem

One opaque tag id and its distinct live-document usage in the current KB.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Opaque semantic tag id | 
**document_count** | **int** | Distinct live documents using this tag | 

## Example

```python
from everos_cloud.models.related_tag_usage_item import RelatedTagUsageItem

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedTagUsageItem from a JSON string
related_tag_usage_item_instance = RelatedTagUsageItem.from_json(json)
# print the JSON string representation of the object
print(RelatedTagUsageItem.to_json())

# convert the object into a dict
related_tag_usage_item_dict = related_tag_usage_item_instance.to_dict()
# create an instance of RelatedTagUsageItem from a dict
related_tag_usage_item_from_dict = RelatedTagUsageItem.from_dict(related_tag_usage_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


