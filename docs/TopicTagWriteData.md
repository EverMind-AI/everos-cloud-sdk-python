# TopicTagWriteData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic_id** | **str** | The topic whose tag snapshot was written. | 
**requested** | **int** | Stable-distinct request id count; not vocabulary-validity count | 
**tag_ids** | **List[str]** | Complete materialized topic tag snapshot after the accepted write | 
**version** | **int** | Current topic tag version | 
**truncated** | **bool** | Whether distinct input exceeded the store limit | 
**limit** | **int** | Materialized topic tag limit | 
**dropped_count** | **int** | Distinct requested ids omitted by stable truncation | 

## Example

```python
from everos_cloud.models.topic_tag_write_data import TopicTagWriteData

# TODO update the JSON string below
json = "{}"
# create an instance of TopicTagWriteData from a JSON string
topic_tag_write_data_instance = TopicTagWriteData.from_json(json)
# print the JSON string representation of the object
print(TopicTagWriteData.to_json())

# convert the object into a dict
topic_tag_write_data_dict = topic_tag_write_data_instance.to_dict()
# create an instance of TopicTagWriteData from a dict
topic_tag_write_data_from_dict = TopicTagWriteData.from_dict(topic_tag_write_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


