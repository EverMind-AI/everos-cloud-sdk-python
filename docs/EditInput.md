# EditInput

Bulk profile edit request [Cloud-only].  Carries 1–50 ``EditOperation`` items targeting a single user's profile. ``memory_type`` is pinned to ``\"profile\"``; ``source`` is server-set and not accepted from the client.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | Scope the profile lives in, defaulting to \&quot;default\&quot;. | [optional] [default to 'default']
**project_id** | **str** | Second half of the scope, defaulting to \&quot;default\&quot;. | [optional] [default to 'default']
**user_id** | **str** | The user whose profile is being edited. | 
**memory_type** | **str** | Pinned to \&quot;profile\&quot; — this endpoint edits nothing else. | [optional] [default to 'profile']
**operations** | [**List[EditInputOperationsInner]**](EditInputOperationsInner.md) | 1 to 50 edits applied in one call. \&quot;add\&quot; mints the item id and must not carry one; \&quot;update\&quot; and \&quot;delete\&quot; require an &#x60;item_id&#x60; whose prefix matches the item type (\&quot;ei_\&quot; for explicit_info, \&quot;it_\&quot; for implicit_traits). Each operation&#39;s outcome is reported separately, so one can be rejected while the rest apply. | 

## Example

```python
from everos_cloud.models.edit_input import EditInput

# TODO update the JSON string below
json = "{}"
# create an instance of EditInput from a JSON string
edit_input_instance = EditInput.from_json(json)
# print the JSON string representation of the object
print(EditInput.to_json())

# convert the object into a dict
edit_input_dict = edit_input_instance.to_dict()
# create an instance of EditInput from a dict
edit_input_from_dict = EditInput.from_dict(edit_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


