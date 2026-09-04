# TopicFilterListData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topics** | [**List[TopicFilterItem]**](TopicFilterItem.md) | The matching topics, one page of them. | 
**total** | **int** | How many topics satisfy the all-tags-on-one-topic condition in total, counted before paging. | 

## Example

```python
from everos_cloud.models.topic_filter_list_data import TopicFilterListData

# TODO update the JSON string below
json = "{}"
# create an instance of TopicFilterListData from a JSON string
topic_filter_list_data_instance = TopicFilterListData.from_json(json)
# print the JSON string representation of the object
print(TopicFilterListData.to_json())

# convert the object into a dict
topic_filter_list_data_dict = topic_filter_list_data_instance.to_dict()
# create an instance of TopicFilterListData from a dict
topic_filter_list_data_from_dict = TopicFilterListData.from_dict(topic_filter_list_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


