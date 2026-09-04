# RelatedTagUsageBody

Candidate tag ids for ``POST /knowledge_bases/{kb_id}/tags``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_ids** | **List[str]** | Candidate opaque tag ids to check against the current live tree | 

## Example

```python
from everos_cloud.models.related_tag_usage_body import RelatedTagUsageBody

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedTagUsageBody from a JSON string
related_tag_usage_body_instance = RelatedTagUsageBody.from_json(json)
# print the JSON string representation of the object
print(RelatedTagUsageBody.to_json())

# convert the object into a dict
related_tag_usage_body_dict = related_tag_usage_body_instance.to_dict()
# create an instance of RelatedTagUsageBody from a dict
related_tag_usage_body_from_dict = RelatedTagUsageBody.from_dict(related_tag_usage_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


