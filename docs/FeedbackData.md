# FeedbackData

The stored signal's id. Nothing about the target memory changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the stored feedback signal. The rated memory itself is unchanged. | 

## Example

```python
from everos_cloud.models.feedback_data import FeedbackData

# TODO update the JSON string below
json = "{}"
# create an instance of FeedbackData from a JSON string
feedback_data_instance = FeedbackData.from_json(json)
# print the JSON string representation of the object
print(FeedbackData.to_json())

# convert the object into a dict
feedback_data_dict = feedback_data_instance.to_dict()
# create an instance of FeedbackData from a dict
feedback_data_from_dict = FeedbackData.from_dict(feedback_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


