# everos_cloud.MemoryApi

All URIs are relative to *https://api.evermind.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_memory**](MemoryApi.md#add_memory) | **POST** /api/v2/memory/add | Add messages [OSS + Cloud]
[**bind_tags**](MemoryApi.md#bind_tags) | **POST** /api/v2/memory/tag/bind | Bind tags to memory items [Cloud]
[**delete_memory**](MemoryApi.md#delete_memory) | **POST** /api/v2/memory/delete | Delete memories [Cloud-only]
[**edit_profile**](MemoryApi.md#edit_profile) | **POST** /api/v2/memory/edit | Edit profile items [Cloud-only]
[**flush_memory**](MemoryApi.md#flush_memory) | **POST** /api/v2/memory/flush | Force memory extraction [OSS + Cloud]
[**get_memory**](MemoryApi.md#get_memory) | **POST** /api/v2/memory/get | Get memories (paginated) [OSS + Cloud]
[**replace_tags**](MemoryApi.md#replace_tags) | **POST** /api/v2/memory/tag/replace | Replace (overwrite) tags on memory items [Cloud]
[**search_memory**](MemoryApi.md#search_memory) | **POST** /api/v2/memory/search | Search memories [OSS + Cloud]
[**unbind_tags**](MemoryApi.md#unbind_tags) | **POST** /api/v2/memory/tag/unbind | Unbind tags from memory items [Cloud]


# **add_memory**
> SuccessEnvelopeAddData add_memory(add_input)

Add messages [OSS + Cloud]

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

Bind tags to memory items [Cloud]

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
        # Bind tags to memory items [Cloud]
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_memory**
> SuccessEnvelopeDeleteData delete_memory(delete_input)

Delete memories [Cloud-only]

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

Get memories (paginated) [OSS + Cloud]

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
        # Get memories (paginated) [OSS + Cloud]
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

Replace (overwrite) tags on memory items [Cloud]

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
        # Replace (overwrite) tags on memory items [Cloud]
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_memory**
> SuccessEnvelopeSearchData search_memory(search_input)

Search memories [OSS + Cloud]

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

# **unbind_tags**
> SuccessEnvelopeTagUnbindData unbind_tags(tag_unbind_input)

Unbind tags from memory items [Cloud]

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
        # Unbind tags from memory items [Cloud]
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

