# TopicDetailData

Full topic (node), with content transparently restored (inline or from S3).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Topic id. | 
**doc_id** | **str** | The document this topic was extracted from. | 
**kb_id** | **str** | The knowledge base that document belongs to. | 
**type** | **str** | Structural role of this topic node | 
**category_id** | **str** | The category the document is filed under; empty when uncategorized. | [optional] [default to '']
**category_name** | **str** |  | [optional] 
**name** | **str** | The topic&#39;s title. | 
**depth** | **int** | Depth in the document tree — 0 is the document root, 1 a top-level topic. | [optional] [default to 0]
**seq** | **int** | Depth-first position within the document. Use it as an ordering, not as an index to compute with. | [optional] [default to 0]
**summary** | **str** | Retrieval-oriented summary covering this topic and everything under it. | [optional] [default to '']
**content** | **str** |  | [optional] 
**labels** | **List[str]** | Labels attached to the topic during extraction. | [optional] 
**parent_id** | **str** |  | [optional] 
**children_ids** | **List[str]** | The topics directly beneath this one. | [optional] 
**metadata** | **Dict[str, object]** | Extraction metadata carried alongside the topic. | [optional] 
**tag_ids** | **List[str]** | Opaque final materialized semantic tag ids (maximum 50) | 
**version** | **int** | Current topic tag CAS version | 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from everos_cloud.models.topic_detail_data import TopicDetailData

# TODO update the JSON string below
json = "{}"
# create an instance of TopicDetailData from a JSON string
topic_detail_data_instance = TopicDetailData.from_json(json)
# print the JSON string representation of the object
print(TopicDetailData.to_json())

# convert the object into a dict
topic_detail_data_dict = topic_detail_data_instance.to_dict()
# create an instance of TopicDetailData from a dict
topic_detail_data_from_dict = TopicDetailData.from_dict(topic_detail_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


