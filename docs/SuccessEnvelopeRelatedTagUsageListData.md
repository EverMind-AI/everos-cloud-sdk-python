# SuccessEnvelopeRelatedTagUsageListData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Request trace id (peer to data) | 
**data** | [**RelatedTagUsageListData**](RelatedTagUsageListData.md) | Endpoint-defined business result | 

## Example

```python
from everos_cloud.models.success_envelope_related_tag_usage_list_data import SuccessEnvelopeRelatedTagUsageListData

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessEnvelopeRelatedTagUsageListData from a JSON string
success_envelope_related_tag_usage_list_data_instance = SuccessEnvelopeRelatedTagUsageListData.from_json(json)
# print the JSON string representation of the object
print(SuccessEnvelopeRelatedTagUsageListData.to_json())

# convert the object into a dict
success_envelope_related_tag_usage_list_data_dict = success_envelope_related_tag_usage_list_data_instance.to_dict()
# create an instance of SuccessEnvelopeRelatedTagUsageListData from a dict
success_envelope_related_tag_usage_list_data_from_dict = SuccessEnvelopeRelatedTagUsageListData.from_dict(success_envelope_related_tag_usage_list_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


