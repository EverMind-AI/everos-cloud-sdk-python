# RelatedTagUsageListData

Complete non-zero usage result for the requested candidate tag ids.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[RelatedTagUsageItem]**](RelatedTagUsageItem.md) | One entry per requested tag id that is actually in use, sorted by id. | 
**total** | **int** | Number of returned distinct tag ids | 

## Example

```python
from everos_cloud.models.related_tag_usage_list_data import RelatedTagUsageListData

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedTagUsageListData from a JSON string
related_tag_usage_list_data_instance = RelatedTagUsageListData.from_json(json)
# print the JSON string representation of the object
print(RelatedTagUsageListData.to_json())

# convert the object into a dict
related_tag_usage_list_data_dict = related_tag_usage_list_data_instance.to_dict()
# create an instance of RelatedTagUsageListData from a dict
related_tag_usage_list_data_from_dict = RelatedTagUsageListData.from_dict(related_tag_usage_list_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


