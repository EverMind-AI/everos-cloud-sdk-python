# TopicDetailData

Full topic (node), with content transparently restored (inline or from S3).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**doc_id** | **str** |  | 
**kb_id** | **str** |  | 
**category_id** | **str** |  | [optional] [default to '']
**category_name** | **str** |  | [optional] 
**name** | **str** |  | 
**depth** | **int** |  | [optional] [default to 0]
**seq** | **int** |  | [optional] [default to 0]
**summary** | **str** |  | [optional] [default to '']
**content** | **str** |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**children_ids** | **List[str]** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
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


