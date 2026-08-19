# TopicListData

A document's topic tree, DFS-ordered (flat list; build the tree from `parent_id`).  The list INCLUDES the synthetic document-root item (`type=root`), so ``len(topics) == document.topic_count + 1`` — the document's ``topic_count`` counts real topics only. Two consumer recipes:  * **Full tree** — root at the item whose ``parent_id`` is null, link the rest by   ``parent_id``. Returned order is already DFS, so children keep document order. * **Real topics only** (to match ``topic_count``) — drop the ``type=root`` item AND   null out the ``parent_id`` of its direct children, otherwise those now point at an id   that is no longer in the set.  Robust root test for either recipe: ``parent_id is null OR parent_id not in the returned ids`` — that also survives an orphan row left behind by a partial cascade delete.  ``include=content`` hydrates every item's body, which can grow the response by orders of magnitude. Ask for it to render a whole document, not to draw the tree.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topics** | [**List[TopicListItem]**](TopicListItem.md) |  | [optional] 

## Example

```python
from everos_cloud.models.topic_list_data import TopicListData

# TODO update the JSON string below
json = "{}"
# create an instance of TopicListData from a JSON string
topic_list_data_instance = TopicListData.from_json(json)
# print the JSON string representation of the object
print(TopicListData.to_json())

# convert the object into a dict
topic_list_data_dict = topic_list_data_instance.to_dict()
# create an instance of TopicListData from a dict
topic_list_data_from_dict = TopicListData.from_dict(topic_list_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


