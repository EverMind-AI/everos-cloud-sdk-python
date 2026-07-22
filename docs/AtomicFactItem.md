# AtomicFactItem

Atomic fact nested in an episode. Spec appendix E references it but does not enumerate its fields — minimal shape until the contract is detailed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**content** | **str** |  | 

## Example

```python
from everos_cloud_sdk.models.atomic_fact_item import AtomicFactItem

# TODO update the JSON string below
json = "{}"
# create an instance of AtomicFactItem from a JSON string
atomic_fact_item_instance = AtomicFactItem.from_json(json)
# print the JSON string representation of the object
print(AtomicFactItem.to_json())

# convert the object into a dict
atomic_fact_item_dict = atomic_fact_item_instance.to_dict()
# create an instance of AtomicFactItem from a dict
atomic_fact_item_from_dict = AtomicFactItem.from_dict(atomic_fact_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


