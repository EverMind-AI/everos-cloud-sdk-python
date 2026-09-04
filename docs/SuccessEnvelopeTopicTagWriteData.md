# SuccessEnvelopeTopicTagWriteData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Request trace id (peer to data) | 
**data** | [**TopicTagWriteData**](TopicTagWriteData.md) | Endpoint-defined business result | 

## Example

```python
from everos_cloud.models.success_envelope_topic_tag_write_data import SuccessEnvelopeTopicTagWriteData

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessEnvelopeTopicTagWriteData from a JSON string
success_envelope_topic_tag_write_data_instance = SuccessEnvelopeTopicTagWriteData.from_json(json)
# print the JSON string representation of the object
print(SuccessEnvelopeTopicTagWriteData.to_json())

# convert the object into a dict
success_envelope_topic_tag_write_data_dict = success_envelope_topic_tag_write_data_instance.to_dict()
# create an instance of SuccessEnvelopeTopicTagWriteData from a dict
success_envelope_topic_tag_write_data_from_dict = SuccessEnvelopeTopicTagWriteData.from_dict(success_envelope_topic_tag_write_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


