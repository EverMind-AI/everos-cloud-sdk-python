# TopicFilterItem

Slim item for the KB-wide tag-filter endpoint.  This is deliberately separate from :class:`TopicListItem`: the document-tree API may hydrate content and exposes timestamps, while the cross-service tag-filter wire is frozen without those fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Topic (node) id | 
**doc_id** | **str** | Owning document id | [optional] [default to '']
**kb_id** | **str** | Owning knowledge base id | [optional] [default to '']
**name** | **str** | Topic title | 
**type** | **str** | Structural role of the topic — \&quot;root\&quot; for the synthetic document-root node, \&quot;section\&quot; for a real topic. | [optional] [default to 'section']
**depth** | **int** | Depth in the document tree — 0 is the document root, 1 a top-level topic. | [optional] [default to 0]
**seq** | **int** | Depth-first position within the document. Use it as an ordering, not as an index to compute with. | [optional] [default to 0]
**parent_id** | **str** |  | [optional] 
**summary** | **str** | Retrieval-oriented summary covering this topic and everything under it. | [optional] [default to '']
**tag_ids** | **List[str]** | Opaque final materialized semantic tag ids (maximum 50) | 
**version** | **int** | Current topic tag CAS version | 

## Example

```python
from everos_cloud.models.topic_filter_item import TopicFilterItem

# TODO update the JSON string below
json = "{}"
# create an instance of TopicFilterItem from a JSON string
topic_filter_item_instance = TopicFilterItem.from_json(json)
# print the JSON string representation of the object
print(TopicFilterItem.to_json())

# convert the object into a dict
topic_filter_item_dict = topic_filter_item_instance.to_dict()
# create an instance of TopicFilterItem from a dict
topic_filter_item_from_dict = TopicFilterItem.from_dict(topic_filter_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


