# SearchAtomicFactItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Atomic-fact id. | 
**content** | **str** | The fact itself, as a single statement. | 
**score** | **float** | Relevance of this fact to the query. | 

## Example

```python
from everos_cloud.models.search_atomic_fact_item import SearchAtomicFactItem

# TODO update the JSON string below
json = "{}"
# create an instance of SearchAtomicFactItem from a JSON string
search_atomic_fact_item_instance = SearchAtomicFactItem.from_json(json)
# print the JSON string representation of the object
print(SearchAtomicFactItem.to_json())

# convert the object into a dict
search_atomic_fact_item_dict = search_atomic_fact_item_instance.to_dict()
# create an instance of SearchAtomicFactItem from a dict
search_atomic_fact_item_from_dict = SearchAtomicFactItem.from_dict(search_atomic_fact_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


