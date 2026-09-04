# SuccessEnvelopeTopicFilterListData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Request trace id (peer to data) | 
**data** | [**TopicFilterListData**](TopicFilterListData.md) | Endpoint-defined business result | 

## Example

```python
from everos_cloud.models.success_envelope_topic_filter_list_data import SuccessEnvelopeTopicFilterListData

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessEnvelopeTopicFilterListData from a JSON string
success_envelope_topic_filter_list_data_instance = SuccessEnvelopeTopicFilterListData.from_json(json)
# print the JSON string representation of the object
print(SuccessEnvelopeTopicFilterListData.to_json())

# convert the object into a dict
success_envelope_topic_filter_list_data_dict = success_envelope_topic_filter_list_data_instance.to_dict()
# create an instance of SuccessEnvelopeTopicFilterListData from a dict
success_envelope_topic_filter_list_data_from_dict = SuccessEnvelopeTopicFilterListData.from_dict(success_envelope_topic_filter_list_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


