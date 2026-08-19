# everos_cloud.TasksApi

All URIs are relative to *https://api.evermind.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_task_stats**](TasksApi.md#get_task_stats) | **GET** /api/v2/tasks/stats | Aggregate task counts by status
[**get_task_status**](TasksApi.md#get_task_status) | **GET** /api/v2/tasks/{task_id} | Get async task status
[**list_tasks**](TasksApi.md#list_tasks) | **GET** /api/v2/tasks | List async tasks


# **get_task_stats**
> TaskStatsResponse get_task_stats(start=start, end=end)

Aggregate task counts by status

Counts tasks per status over a time window. All four statuses are always present (0 when absent) so dashboards get a stable shape, and the response echoes the window actually used after server-side clamping. Results are scoped to the caller's tenant, resolved from the request context; a caller can only ever see its own tasks.

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.task_stats_response import TaskStatsResponse
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
    api_instance = everos_cloud.TasksApi(api_client)
    start = 'start_example' # str |  (optional)
    end = 'end_example' # str |  (optional)

    try:
        # Aggregate task counts by status
        api_response = api_instance.get_task_stats(start=start, end=end)
        print("The response of TasksApi->get_task_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_task_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **str**|  | [optional] 
 **end** | **str**|  | [optional] 

### Return type

[**TaskStatsResponse**](TaskStatsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Aggregated counts |  -  |
**400** | Invalid query parameter, or missing tenant scope |  -  |
**503** | Stats require the database-backed store, which is not configured |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_status**
> TaskStatusResponse get_task_status(task_id)

Get async task status

Returns the progress of one async task. Task ids are unique system-wide, so the task type does not need to be known. Unknown or expired ids return 404. Results are scoped to the caller's tenant, resolved from the request context; a caller can only ever see its own tasks.

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.task_status_response import TaskStatusResponse
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
    api_instance = everos_cloud.TasksApi(api_client)
    task_id = 'task_id_example' # str | Task id, as returned in the 202 acknowledgement of the write that created it

    try:
        # Get async task status
        api_response = api_instance.get_task_status(task_id)
        print("The response of TasksApi->get_task_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_task_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Task id, as returned in the 202 acknowledgement of the write that created it | 

### Return type

[**TaskStatusResponse**](TaskStatusResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task status |  -  |
**400** | Missing tenant scope |  -  |
**404** | Task id is unknown or has expired |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tasks**
> TaskListResponse list_tasks(page=page, page_size=page_size, status=status, session_id=session_id, start=start, end=end)

List async tasks

Paginated task list, filterable by status, session and time window. Results are scoped to the caller's tenant, resolved from the request context; a caller can only ever see its own tasks.

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.task_list_response import TaskListResponse
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
    api_instance = everos_cloud.TasksApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    status = 'status_example' # str |  (optional)
    session_id = 'session_id_example' # str |  (optional)
    start = 'start_example' # str |  (optional)
    end = 'end_example' # str |  (optional)

    try:
        # List async tasks
        api_response = api_instance.list_tasks(page=page, page_size=page_size, status=status, session_id=session_id, start=start, end=end)
        print("The response of TasksApi->list_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->list_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **status** | **str**|  | [optional] 
 **session_id** | **str**|  | [optional] 
 **start** | **str**|  | [optional] 
 **end** | **str**|  | [optional] 

### Return type

[**TaskListResponse**](TaskListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task list |  -  |
**400** | Invalid query parameter, or missing tenant scope |  -  |
**503** | Listing requires the database-backed store, which is not configured |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

