# TopicListItem

Node-tree overview item. ``content`` only when the caller asks for it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Topic (node) id | 
**doc_id** | **str** | Owning document id | [optional] [default to '']
**kb_id** | **str** | Owning knowledge base id | [optional] [default to '']
**name** | **str** | Node title. For the document-root item (&#x60;type&#x3D;root&#x60;) this is the document title, i.e. the same value as the document&#39;s &#x60;title&#x60; | 
**type** | **str** | Structural role: &#x60;root&#x60; &#x3D; the document-root container (exactly one per document, &#x60;depth&#x3D;0&#x60;, &#x60;parent_id&#x3D;null&#x60;, empty body), &#x60;section&#x60; &#x3D; a real topic, &#x60;element&#x60; &#x3D; rich media (reserved, not produced yet). Filter on this rather than on &#x60;depth&#x3D;&#x3D;0&#x60; to tell the root apart from real topics | [optional] [default to 'section']
**depth** | **int** | Tree depth: 0 &#x3D; document root, 1 &#x3D; a top-level topic | [optional] [default to 0]
**seq** | **int** | DFS position within the document (0 &#x3D; the root). Items are already returned in this order — use the order, do not do arithmetic on the value | [optional] [default to 0]
**parent_id** | **str** |  | [optional] 
**summary** | **str** | Retrieval-oriented summary covering this node AND its subtree. On the root item it is the document-level summary | [optional] [default to '']
**content** | **str** |  | [optional] 
**tag_ids** | **List[str]** | Opaque final materialized semantic tag ids (maximum 50) | [optional] 
**version** | **int** | Current topic tag CAS version | [optional] [default to 0]
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from everos_cloud.models.topic_list_item import TopicListItem

# TODO update the JSON string below
json = "{}"
# create an instance of TopicListItem from a JSON string
topic_list_item_instance = TopicListItem.from_json(json)
# print the JSON string representation of the object
print(TopicListItem.to_json())

# convert the object into a dict
topic_list_item_dict = topic_list_item_instance.to_dict()
# create an instance of TopicListItem from a dict
topic_list_item_from_dict = TopicListItem.from_dict(topic_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


