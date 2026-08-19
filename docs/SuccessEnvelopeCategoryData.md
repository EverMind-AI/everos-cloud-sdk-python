# SuccessEnvelopeCategoryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Request trace id (peer to data) | 
**data** | [**CategoryData**](CategoryData.md) | Endpoint-defined business result | 

## Example

```python
from everos_cloud.models.success_envelope_category_data import SuccessEnvelopeCategoryData

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessEnvelopeCategoryData from a JSON string
success_envelope_category_data_instance = SuccessEnvelopeCategoryData.from_json(json)
# print the JSON string representation of the object
print(SuccessEnvelopeCategoryData.to_json())

# convert the object into a dict
success_envelope_category_data_dict = success_envelope_category_data_instance.to_dict()
# create an instance of SuccessEnvelopeCategoryData from a dict
success_envelope_category_data_from_dict = SuccessEnvelopeCategoryData.from_dict(success_envelope_category_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


