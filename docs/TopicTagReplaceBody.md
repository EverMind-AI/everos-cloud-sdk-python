# TopicTagReplaceBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_ids** | **List[str]** | Complete materialized snapshot. Cloud stable-deduplicates the request, stores the first 50 ids, and reports any truncation. | 
**version** | **int** | Expected current topic tag_version (CAS) | 

## Example

```python
from everos_cloud.models.topic_tag_replace_body import TopicTagReplaceBody

# TODO update the JSON string below
json = "{}"
# create an instance of TopicTagReplaceBody from a JSON string
topic_tag_replace_body_instance = TopicTagReplaceBody.from_json(json)
# print the JSON string representation of the object
print(TopicTagReplaceBody.to_json())

# convert the object into a dict
topic_tag_replace_body_dict = topic_tag_replace_body_instance.to_dict()
# create an instance of TopicTagReplaceBody from a dict
topic_tag_replace_body_from_dict = TopicTagReplaceBody.from_dict(topic_tag_replace_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


