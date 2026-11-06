# PurgeSummary

What the purge would delete right now, counted per store.  A snapshot at request time: data written before the purge runs is deleted too. Counts include soft-deleted rows (the purge removes those as well), so they can be higher than what ``get`` shows. Feedback is not memory data and is not counted. A count that did not finish in time is ``null`` and ``complete`` is ``false``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mongo** | [**Dict[str, MongoValue]**](MongoValue.md) | MongoDB documents per memory type (collection without the &#x60;v2_&#x60; prefix), the source of truth. | 
**mongo_total** | **int** |  | 
**elasticsearch_total** | **int** |  | 
**milvus_total** | **int** |  | 
**complete** | **bool** | False when any count timed out or failed. | 
**counted_at** | **datetime** |  | 
**comment** | **str** | What the counts include and exclude (soft-deleted rows, feedback). | 
**error** | **str** |  | [optional] 

## Example

```python
from everos_cloud.models.purge_summary import PurgeSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PurgeSummary from a JSON string
purge_summary_instance = PurgeSummary.from_json(json)
# print the JSON string representation of the object
print(PurgeSummary.to_json())

# convert the object into a dict
purge_summary_dict = purge_summary_instance.to_dict()
# create an instance of PurgeSummary from a dict
purge_summary_from_dict = PurgeSummary.from_dict(purge_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


