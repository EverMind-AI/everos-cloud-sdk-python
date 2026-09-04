# DocData

A document as returned to clients. ``topic_count`` = the node_count (>0 = ingested).  Contract note — ``topic_count`` vs ``GET .../topics``: the count is of REAL topics and excludes the synthetic document-root node, while the topics list INCLUDES it. So ``len(topics) == topic_count + 1`` for an ingested document. See ``TopicListData``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document id (bare primary key) | 
**kb_id** | **str** | The knowledge base this document belongs to. | 
**category_id** | **str** | The category it is filed under; empty when it is uncategorized. | [optional] [default to '']
**category_name** | **str** |  | [optional] 
**title** | **str** | The document&#39;s title. | 
**summary** | **str** |  | [optional] 
**source_name** | **str** |  | [optional] 
**source_type** | **str** |  | [optional] 
**tags** | [**List[TagRef]**](TagRef.md) | Distinct opaque ids from the document&#39;s read-only topic-tag union. Cloud leaves name unset; KHS may validate and expand display names. This document aggregate is read-only and carries no topic ownership field. | 
**topic_count** | **int** | Number of real topics extracted (0 &#x3D; not ingested yet / ingest failed). EXCLUDES the synthetic document-root node, so &#x60;GET .../topics&#x60; — which includes it — returns exactly one more item than this | [optional] [default to 0]
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from everos_cloud.models.doc_data import DocData

# TODO update the JSON string below
json = "{}"
# create an instance of DocData from a JSON string
doc_data_instance = DocData.from_json(json)
# print the JSON string representation of the object
print(DocData.to_json())

# convert the object into a dict
doc_data_dict = doc_data_instance.to_dict()
# create an instance of DocData from a dict
doc_data_from_dict = DocData.from_dict(doc_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


