# EpisodePatch

The editable surface of an episode.  NATIVE field names, not generic ones: a generic mapping is a stretch for other types (agent_case has three parallel content fields), and it would make the audit event's before/after unreadable. Generality lives in the envelope + the ``EDITABLE_FIELDS`` registry.  Partial, and ``None`` means \"leave it alone\" rather than \"clear it\". A body-only patch is accepted: the server regenerates ``summary`` from the new text (the same way a freshly extracted episode gets one) so the preview never describes text that no longer exists; ``subject`` has no generator and is kept unless supplied.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**episode** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 

## Example

```python
from everos_cloud.models.episode_patch import EpisodePatch

# TODO update the JSON string below
json = "{}"
# create an instance of EpisodePatch from a JSON string
episode_patch_instance = EpisodePatch.from_json(json)
# print the JSON string representation of the object
print(EpisodePatch.to_json())

# convert the object into a dict
episode_patch_dict = episode_patch_instance.to_dict()
# create an instance of EpisodePatch from a dict
episode_patch_from_dict = EpisodePatch.from_dict(episode_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


