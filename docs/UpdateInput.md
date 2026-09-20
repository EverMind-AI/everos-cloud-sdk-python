# UpdateInput

Edit ONE memory record's editable fields [Cloud-only].  No ``expected_*`` / version: the API does no conflict detection (last write wins). Resend idempotency comes from the no-change short circuit, and Reflection guards itself with a content CAS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory_type** | **str** | Kind of the memory being edited. Only \&quot;episode\&quot; is accepted today. | 
**memory_id** | **str** | The memory&#39;s &#x60;id&#x60; as returned by /api/v2/memory/get or /search. | 
**patch** | [**EpisodePatch**](EpisodePatch.md) | The fields to rewrite — at least one. Fields left out keep their current value. | 
**reason** | [**Reason**](Reason.md) |  | [optional] 

## Example

```python
from everos_cloud.models.update_input import UpdateInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInput from a JSON string
update_input_instance = UpdateInput.from_json(json)
# print the JSON string representation of the object
print(UpdateInput.to_json())

# convert the object into a dict
update_input_dict = update_input_instance.to_dict()
# create an instance of UpdateInput from a dict
update_input_from_dict = UpdateInput.from_dict(update_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


