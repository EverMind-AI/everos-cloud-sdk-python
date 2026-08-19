# SuccessEnvelopeCategoryDeleteData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Request trace id (peer to data) | 
**data** | [**CategoryDeleteData**](CategoryDeleteData.md) | Endpoint-defined business result | 

## Example

```python
from everos_cloud.models.success_envelope_category_delete_data import SuccessEnvelopeCategoryDeleteData

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessEnvelopeCategoryDeleteData from a JSON string
success_envelope_category_delete_data_instance = SuccessEnvelopeCategoryDeleteData.from_json(json)
# print the JSON string representation of the object
print(SuccessEnvelopeCategoryDeleteData.to_json())

# convert the object into a dict
success_envelope_category_delete_data_dict = success_envelope_category_delete_data_instance.to_dict()
# create an instance of SuccessEnvelopeCategoryDeleteData from a dict
success_envelope_category_delete_data_from_dict = SuccessEnvelopeCategoryDeleteData.from_dict(success_envelope_category_delete_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


