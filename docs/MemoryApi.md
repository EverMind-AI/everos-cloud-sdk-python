# everos_cloud.MemoryApi

All URIs are relative to *https://api.evermind.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_memory**](MemoryApi.md#add_memory) | **POST** /api/v2/memory/add | Add messages [OSS + Cloud]
[**bind_tags**](MemoryApi.md#bind_tags) | **POST** /api/v2/memory/tag/bind | Bind tags to memories [Cloud]
[**delete_memories_by_ids**](MemoryApi.md#delete_memories_by_ids) | **POST** /api/v2/memory/delete_by_ids | Soft-delete memory records by id [Cloud-only]
[**delete_memory**](MemoryApi.md#delete_memory) | **POST** /api/v2/memory/delete | Delete memories [Cloud-only]
[**edit_profile**](MemoryApi.md#edit_profile) | **POST** /api/v2/memory/edit | Edit profile items [Cloud-only]
[**flush_memory**](MemoryApi.md#flush_memory) | **POST** /api/v2/memory/flush | Force memory extraction [OSS + Cloud]
[**get_memory**](MemoryApi.md#get_memory) | **POST** /api/v2/memory/get | Get memories [OSS + Cloud]
[**replace_tags**](MemoryApi.md#replace_tags) | **POST** /api/v2/memory/tag/replace | Replace tags on memories [Cloud]
[**search_memory**](MemoryApi.md#search_memory) | **POST** /api/v2/memory/search | Search memories [OSS + Cloud]
[**submit_feedback**](MemoryApi.md#submit_feedback) | **POST** /api/v2/memory/feedback | Submit feedback about one memory [Cloud-only]
[**unbind_tags**](MemoryApi.md#unbind_tags) | **POST** /api/v2/memory/tag/unbind | Unbind tags from memories [Cloud]
[**update_memory**](MemoryApi.md#update_memory) | **POST** /api/v2/memory/update | Edit one memory record [Cloud-only]


# **add_memory**
> SuccessEnvelopeAddData add_memory(add_input)

Add messages [OSS + Cloud]

Append conversation messages to a session's working memory. One call carries 1–500 messages.  The write is asynchronous by default (`async_mode` true): the gateway validates and enqueues it, answering 202 with status \"queued\". Pass `async_mode: false` to forward synchronously and receive the engine's 200 result instead.  Distillation into long-term memory is always asynchronous — it runs on a session boundary, or when you call /api/v2/memory/flush.

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.add_input import AddInput
from everos_cloud.models.success_envelope_add_data import SuccessEnvelopeAddData
from everos_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.evermind.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = everos_cloud.Configuration(
    host = "https://api.evermind.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = everos_cloud.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with everos_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = everos_cloud.MemoryApi(api_client)
    add_input = everos_cloud.AddInput() # AddInput | 

    try:
        # Add messages [OSS + Cloud]
        api_response = api_instance.add_memory(add_input)
        print("The response of MemoryApi->add_memory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->add_memory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_input** | [**AddInput**](AddInput.md)|  | 

### Return type

[**SuccessEnvelopeAddData**](SuccessEnvelopeAddData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Synchronous write result (async_mode&#x3D;false). |  -  |
**422** | Validation Error |  -  |
**202** | Accepted for asynchronous processing (async_mode&#x3D;true, default). |  -  |
**401** | Missing or invalid bearer token. |  -  |
**403** | Authenticated but not permitted — either rejected by the auth service, or the account&#39;s memory API version does not match the interface version implied by the path (a v1 account calling an /api/v2 route). |  -  |
**429** | Rate limit or quota exceeded. |  -  |
**503** | The gateway could not reach the authentication service. Transient — retry with backoff. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bind_tags**
> SuccessEnvelopeTagBindData bind_tags(tag_bind_input)

Bind tags to memories [Cloud]

Add tags to existing memories, keeping the tags they already carry.  Tags are scoped by the memory ids themselves — pass `memory_type` plus the ids, not an app or project scope. Tags are created by use: binding a name that does not exist yet is how it comes into existence.  Idempotent, and batched over memory_ids × tags.

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.success_envelope_tag_bind_data import SuccessEnvelopeTagBindData
from everos_cloud.models.tag_bind_input import TagBindInput
from everos_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.evermind.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = everos_cloud.Configuration(
    host = "https://api.evermind.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = everos_cloud.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with everos_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = everos_cloud.MemoryApi(api_client)
    tag_bind_input = everos_cloud.TagBindInput() # TagBindInput | 

    try:
        # Bind tags to memories [Cloud]
        api_response = api_instance.bind_tags(tag_bind_input)
        print("The response of MemoryApi->bind_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->bind_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_bind_input** | [**TagBindInput**](TagBindInput.md)|  | 

### Return type

[**SuccessEnvelopeTagBindData**](SuccessEnvelopeTagBindData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**401** | Missing or invalid bearer token. |  -  |
**403** | Authenticated but not permitted — either rejected by the auth service, or the account&#39;s memory API version does not match the interface version implied by the path (a v1 account calling an /api/v2 route). |  -  |
**429** | Rate limit or quota exceeded. |  -  |
**503** | The gateway could not reach the authentication service. Transient — retry with backoff. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_memories_by_ids**
> SuccessEnvelopeDeleteByIdsData delete_memories_by_ids(delete_by_ids_input)

Soft-delete memory records by id [Cloud-only]

Soft-delete up to 50 memories chosen by id, together with what was derived from them (extracted facts, cluster membership and search-index copies). Only \"episode\" is supported today.  - Every id must be well-formed; one malformed id rejects the whole request with 422 and nothing is deleted. - Ids that do not exist, are already deleted, or belong to another tenant are skipped rather than reported — the rest of the batch is still deleted, so re-sending a batch is safe. Duplicates are collapsed.  To remove memories by owner or session rather than by id, use /api/v2/memory/delete.

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.delete_by_ids_input import DeleteByIdsInput
from everos_cloud.models.success_envelope_delete_by_ids_data import SuccessEnvelopeDeleteByIdsData
from everos_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.evermind.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = everos_cloud.Configuration(
    host = "https://api.evermind.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = everos_cloud.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with everos_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = everos_cloud.MemoryApi(api_client)
    delete_by_ids_input = everos_cloud.DeleteByIdsInput() # DeleteByIdsInput | 

    try:
        # Soft-delete memory records by id [Cloud-only]
        api_response = api_instance.delete_memories_by_ids(delete_by_ids_input)
        print("The response of MemoryApi->delete_memories_by_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->delete_memories_by_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_by_ids_input** | [**DeleteByIdsInput**](DeleteByIdsInput.md)|  | 

### Return type

[**SuccessEnvelopeDeleteByIdsData**](SuccessEnvelopeDeleteByIdsData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**401** | Missing or invalid bearer token. |  -  |
**403** | Authenticated but not permitted — either rejected by the auth service, or the account&#39;s memory API version does not match the interface version implied by the path (a v1 account calling an /api/v2 route). |  -  |
**429** | Rate limit or quota exceeded. |  -  |
**503** | The gateway could not reach the authentication service. Transient — retry with backoff. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_memory**
> SuccessEnvelopeDeleteData delete_memory(delete_input)

Delete memories [Cloud-only]

Soft-delete memories within a scope.  - At least one of `user_id`, `agent_id` or `session_id` is required — an empty body is rejected with 422. - `user_id` and `agent_id` are mutually exclusive.  The response echoes which scope filters were applied and how many records were removed across all memory types.

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.delete_input import DeleteInput
from everos_cloud.models.success_envelope_delete_data import SuccessEnvelopeDeleteData
from everos_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.evermind.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = everos_cloud.Configuration(
    host = "https://api.evermind.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = everos_cloud.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with everos_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = everos_cloud.MemoryApi(api_client)
    delete_input = everos_cloud.DeleteInput() # DeleteInput | 

    try:
        # Delete memories [Cloud-only]
        api_response = api_instance.delete_memory(delete_input)
        print("The response of MemoryApi->delete_memory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->delete_memory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_input** | [**DeleteInput**](DeleteInput.md)|  | 

### Return type

[**SuccessEnvelopeDeleteData**](SuccessEnvelopeDeleteData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**401** | Missing or invalid bearer token. |  -  |
**403** | Authenticated but not permitted — either rejected by the auth service, or the account&#39;s memory API version does not match the interface version implied by the path (a v1 account calling an /api/v2 route). |  -  |
**429** | Rate limit or quota exceeded. |  -  |
**503** | The gateway could not reach the authentication service. Transient — retry with backoff. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_profile**
> SuccessEnvelopeEditData edit_profile(edit_input)

Edit profile items [Cloud-only]

Apply 1–50 edits to one user's profile in a single call.  Each operation carries an `action` (add, update or delete), a `type` (explicit_info or implicit_traits), the item `data`, and an optional `reason`.  Profile is the only memory type this endpoint edits — `memory_type` is pinned to \"profile\"; every other type is produced by extraction. Operations are reported individually in the response, so some can be rejected while others apply.  To change an episode's narrative, summary or subject, use /api/v2/memory/update instead.

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.edit_input import EditInput
from everos_cloud.models.success_envelope_edit_data import SuccessEnvelopeEditData
from everos_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.evermind.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = everos_cloud.Configuration(
    host = "https://api.evermind.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = everos_cloud.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with everos_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = everos_cloud.MemoryApi(api_client)
    edit_input = everos_cloud.EditInput() # EditInput | 

    try:
        # Edit profile items [Cloud-only]
        api_response = api_instance.edit_profile(edit_input)
        print("The response of MemoryApi->edit_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->edit_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_input** | [**EditInput**](EditInput.md)|  | 

### Return type

[**SuccessEnvelopeEditData**](SuccessEnvelopeEditData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**401** | Missing or invalid bearer token. |  -  |
**403** | Authenticated but not permitted — either rejected by the auth service, or the account&#39;s memory API version does not match the interface version implied by the path (a v1 account calling an /api/v2 route). |  -  |
**429** | Rate limit or quota exceeded. |  -  |
**503** | The gateway could not reach the authentication service. Transient — retry with backoff. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flush_memory**
> SuccessEnvelopeFlushData flush_memory(flush_input)

Force memory extraction [OSS + Cloud]

Force extraction for a session instead of waiting for a boundary.  - `\"extracted\"` — memories were distilled. - `\"no_extraction\"` — there was nothing to extract.  A default (async) add that is still queued yields `\"no_extraction\"`, so either write with `async_mode: false` or poll the add's task before flushing.

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.flush_input import FlushInput
from everos_cloud.models.success_envelope_flush_data import SuccessEnvelopeFlushData
from everos_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.evermind.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = everos_cloud.Configuration(
    host = "https://api.evermind.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = everos_cloud.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with everos_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = everos_cloud.MemoryApi(api_client)
    flush_input = everos_cloud.FlushInput() # FlushInput | 

    try:
        # Force memory extraction [OSS + Cloud]
        api_response = api_instance.flush_memory(flush_input)
        print("The response of MemoryApi->flush_memory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->flush_memory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flush_input** | [**FlushInput**](FlushInput.md)|  | 

### Return type

[**SuccessEnvelopeFlushData**](SuccessEnvelopeFlushData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**401** | Missing or invalid bearer token. |  -  |
**403** | Authenticated but not permitted — either rejected by the auth service, or the account&#39;s memory API version does not match the interface version implied by the path (a v1 account calling an /api/v2 route). |  -  |
**429** | Rate limit or quota exceeded. |  -  |
**503** | The gateway could not reach the authentication service. Transient — retry with backoff. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_memory**
> SuccessEnvelopeGetData get_memory(get_input)

Get memories [OSS + Cloud]

List stored memories of one type, paginated.  - Exactly one of `user_id` / `agent_id` is required. - `memory_type` must match that owner: a user owns \"episode\" and \"profile\", an agent owns \"agent_case\" and \"agent_skill\". The other pairings are rejected with 422.  This is a structured read, not a query: it does not embed the request, so a memory is readable as soon as it is extracted — whereas the vector index /api/v2/memory/search relies on lags behind extraction by seconds.

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.get_input import GetInput
from everos_cloud.models.success_envelope_get_data import SuccessEnvelopeGetData
from everos_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.evermind.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = everos_cloud.Configuration(
    host = "https://api.evermind.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = everos_cloud.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with everos_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = everos_cloud.MemoryApi(api_client)
    get_input = everos_cloud.GetInput() # GetInput | 

    try:
        # Get memories [OSS + Cloud]
        api_response = api_instance.get_memory(get_input)
        print("The response of MemoryApi->get_memory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->get_memory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_input** | [**GetInput**](GetInput.md)|  | 

### Return type

[**SuccessEnvelopeGetData**](SuccessEnvelopeGetData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**401** | Missing or invalid bearer token. |  -  |
**403** | Authenticated but not permitted — either rejected by the auth service, or the account&#39;s memory API version does not match the interface version implied by the path (a v1 account calling an /api/v2 route). |  -  |
**429** | Rate limit or quota exceeded. |  -  |
**503** | The gateway could not reach the authentication service. Transient — retry with backoff. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_tags**
> SuccessEnvelopeTagReplaceData replace_tags(tag_replace_input)

Replace tags on memories [Cloud]

Overwrite the tag set on the given memories: tags absent from the request are dropped, and an empty `tags` list clears them all. Use /api/v2/memory/tag/bind to add without removing.

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.success_envelope_tag_replace_data import SuccessEnvelopeTagReplaceData
from everos_cloud.models.tag_replace_input import TagReplaceInput
from everos_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.evermind.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = everos_cloud.Configuration(
    host = "https://api.evermind.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = everos_cloud.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with everos_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = everos_cloud.MemoryApi(api_client)
    tag_replace_input = everos_cloud.TagReplaceInput() # TagReplaceInput | 

    try:
        # Replace tags on memories [Cloud]
        api_response = api_instance.replace_tags(tag_replace_input)
        print("The response of MemoryApi->replace_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->replace_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_replace_input** | [**TagReplaceInput**](TagReplaceInput.md)|  | 

### Return type

[**SuccessEnvelopeTagReplaceData**](SuccessEnvelopeTagReplaceData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**401** | Missing or invalid bearer token. |  -  |
**403** | Authenticated but not permitted — either rejected by the auth service, or the account&#39;s memory API version does not match the interface version implied by the path (a v1 account calling an /api/v2 route). |  -  |
**429** | Rate limit or quota exceeded. |  -  |
**503** | The gateway could not reach the authentication service. Transient — retry with backoff. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_memory**
> SuccessEnvelopeSearchData search_memory(search_input)

Search memories [OSS + Cloud]

Retrieve the memories relevant to a query.  Exactly one of `user_id` / `agent_id` is required, and it decides what comes back: a user owner returns episodes (plus profiles with `include_profile`), an agent owner returns agent cases and skills. All result collections are always present in the response, empty when they do not apply.  The vector-backed methods read an index that lags extraction by seconds — to read back something just extracted, use /api/v2/memory/get.

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.search_input import SearchInput
from everos_cloud.models.success_envelope_search_data import SuccessEnvelopeSearchData
from everos_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.evermind.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = everos_cloud.Configuration(
    host = "https://api.evermind.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = everos_cloud.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with everos_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = everos_cloud.MemoryApi(api_client)
    search_input = everos_cloud.SearchInput() # SearchInput | 

    try:
        # Search memories [OSS + Cloud]
        api_response = api_instance.search_memory(search_input)
        print("The response of MemoryApi->search_memory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->search_memory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_input** | [**SearchInput**](SearchInput.md)|  | 

### Return type

[**SuccessEnvelopeSearchData**](SuccessEnvelopeSearchData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**401** | Missing or invalid bearer token. |  -  |
**403** | Authenticated but not permitted — either rejected by the auth service, or the account&#39;s memory API version does not match the interface version implied by the path (a v1 account calling an /api/v2 route). |  -  |
**429** | Rate limit or quota exceeded. |  -  |
**503** | The gateway could not reach the authentication service. Transient — retry with backoff. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_feedback**
> SuccessEnvelopeFeedbackData submit_feedback(feedback_input)

Submit feedback about one memory [Cloud-only]

Rate one memory — an episode, a profile item, an agent case or an agent skill — as `positive` or `negative`, optionally saying why.  - Address the target the way /api/v2/memory/get or /search returned it: `memory_type` + `memory_id`, plus `item_id` for a profile (required there, rejected for the other kinds). - `reason` and `suggestion` go with negative ratings only; `note` is free text on either. - A target that does not exist, is deleted, or belongs to another tenant is rejected with 404.  Recording is not applying: nothing about the memory is updated, deleted, suppressed or re-indexed. The response is the id of the stored signal.

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.feedback_input import FeedbackInput
from everos_cloud.models.success_envelope_feedback_data import SuccessEnvelopeFeedbackData
from everos_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.evermind.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = everos_cloud.Configuration(
    host = "https://api.evermind.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = everos_cloud.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with everos_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = everos_cloud.MemoryApi(api_client)
    feedback_input = everos_cloud.FeedbackInput() # FeedbackInput | 

    try:
        # Submit feedback about one memory [Cloud-only]
        api_response = api_instance.submit_feedback(feedback_input)
        print("The response of MemoryApi->submit_feedback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->submit_feedback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedback_input** | [**FeedbackInput**](FeedbackInput.md)|  | 

### Return type

[**SuccessEnvelopeFeedbackData**](SuccessEnvelopeFeedbackData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**401** | Missing or invalid bearer token. |  -  |
**403** | Authenticated but not permitted — either rejected by the auth service, or the account&#39;s memory API version does not match the interface version implied by the path (a v1 account calling an /api/v2 route). |  -  |
**429** | Rate limit or quota exceeded. |  -  |
**503** | The gateway could not reach the authentication service. Transient — retry with backoff. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unbind_tags**
> SuccessEnvelopeTagUnbindData unbind_tags(tag_unbind_input)

Unbind tags from memories [Cloud]

Remove the given tags from the given memories, leaving their other tags in place. Idempotent: unbinding a tag an item does not carry still counts as matched.

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.success_envelope_tag_unbind_data import SuccessEnvelopeTagUnbindData
from everos_cloud.models.tag_unbind_input import TagUnbindInput
from everos_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.evermind.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = everos_cloud.Configuration(
    host = "https://api.evermind.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = everos_cloud.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with everos_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = everos_cloud.MemoryApi(api_client)
    tag_unbind_input = everos_cloud.TagUnbindInput() # TagUnbindInput | 

    try:
        # Unbind tags from memories [Cloud]
        api_response = api_instance.unbind_tags(tag_unbind_input)
        print("The response of MemoryApi->unbind_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->unbind_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_unbind_input** | [**TagUnbindInput**](TagUnbindInput.md)|  | 

### Return type

[**SuccessEnvelopeTagUnbindData**](SuccessEnvelopeTagUnbindData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**401** | Missing or invalid bearer token. |  -  |
**403** | Authenticated but not permitted — either rejected by the auth service, or the account&#39;s memory API version does not match the interface version implied by the path (a v1 account calling an /api/v2 route). |  -  |
**429** | Rate limit or quota exceeded. |  -  |
**503** | The gateway could not reach the authentication service. Transient — retry with backoff. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_memory**
> SuccessEnvelopeUpdateData update_memory(update_input)

Edit one memory record [Cloud-only]

Rewrite the editable fields of one memory. Only \"episode\" can be edited today.  - `patch` uses the episode's own field names — `episode`, `summary`, `subject` — and needs at least one of them. Fields left out keep their current value. - A patch that changes only `episode` makes the server regenerate `summary` from the new text; `subject` is never regenerated. - No `app_id` / `project_id`: the record already knows its scope.  There is no version check — the last write wins. Re-sending content equal to what is stored answers 200 with `unchanged: true` and writes nothing. Changing the narrative re-indexes the memory and re-extracts its facts in the background; the response is the edited record itself, with `edited_at` and `reflect_state` set.  A record that does not exist, is already deleted, or belongs to another tenant is rejected with 404.  Profile items are edited through /api/v2/memory/edit, not here.

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.success_envelope_update_data import SuccessEnvelopeUpdateData
from everos_cloud.models.update_input import UpdateInput
from everos_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.evermind.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = everos_cloud.Configuration(
    host = "https://api.evermind.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = everos_cloud.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with everos_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = everos_cloud.MemoryApi(api_client)
    update_input = everos_cloud.UpdateInput() # UpdateInput | 

    try:
        # Edit one memory record [Cloud-only]
        api_response = api_instance.update_memory(update_input)
        print("The response of MemoryApi->update_memory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->update_memory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_input** | [**UpdateInput**](UpdateInput.md)|  | 

### Return type

[**SuccessEnvelopeUpdateData**](SuccessEnvelopeUpdateData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**401** | Missing or invalid bearer token. |  -  |
**403** | Authenticated but not permitted — either rejected by the auth service, or the account&#39;s memory API version does not match the interface version implied by the path (a v1 account calling an /api/v2 route). |  -  |
**429** | Rate limit or quota exceeded. |  -  |
**503** | The gateway could not reach the authentication service. Transient — retry with backoff. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

