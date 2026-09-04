# CategoryListData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**List[CategoryData]**](CategoryData.md) | Every category available in this knowledge base — the ones created here plus the tenant-global presets. | [optional] 

## Example

```python
from everos_cloud.models.category_list_data import CategoryListData

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryListData from a JSON string
category_list_data_instance = CategoryListData.from_json(json)
# print the JSON string representation of the object
print(CategoryListData.to_json())

# convert the object into a dict
category_list_data_dict = category_list_data_instance.to_dict()
# create an instance of CategoryListData from a dict
category_list_data_from_dict = CategoryListData.from_dict(category_list_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


