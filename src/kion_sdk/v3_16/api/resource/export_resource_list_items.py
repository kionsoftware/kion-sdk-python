from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.export_resource_list_items_response_400 import ExportResourceListItemsResponse400
from ...models.export_resource_list_items_response_401 import ExportResourceListItemsResponse401
from ...models.export_resource_list_items_response_403 import ExportResourceListItemsResponse403
from ...models.export_resource_list_items_response_422 import ExportResourceListItemsResponse422
from ...models.export_resource_list_items_response_500 import ExportResourceListItemsResponse500
from ...types import File, FileTypes
from ...types import UNSET, Unset
from io import BytesIO
from typing import cast
import datetime



def _get_kwargs(
    *,
    cloud_provider_i_ds: list[int] | Unset = UNSET,
    include_deleted: bool | Unset = UNSET,
    created_at_start: datetime.datetime | Unset = UNSET,
    created_at_end: datetime.datetime | Unset = UNSET,
    active_at_start: datetime.datetime | Unset = UNSET,
    active_at_end: datetime.datetime | Unset = UNSET,
    deleted_at_start: datetime.datetime | Unset = UNSET,
    deleted_at_end: datetime.datetime | Unset = UNSET,
    type_i_ds: list[int] | Unset = UNSET,
    size: list[str] | Unset = UNSET,
    regions: list[str] | Unset = UNSET,
    ou_i_ds: list[int] | Unset = UNSET,
    project_i_ds: list[int] | Unset = UNSET,
    account_i_ds: list[int] | Unset = UNSET,
    keyword: str | Unset = UNSET,
    include_resource_details: bool | Unset = UNSET,
    include_resource_access: bool | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_cloud_provider_i_ds: list[int] | Unset = UNSET
    if not isinstance(cloud_provider_i_ds, Unset):
        json_cloud_provider_i_ds = cloud_provider_i_ds


    params["cloudProviderIDs"] = json_cloud_provider_i_ds

    params["includeDeleted"] = include_deleted

    json_created_at_start: str | Unset = UNSET
    if not isinstance(created_at_start, Unset):
        json_created_at_start = created_at_start.isoformat()
    params["createdAtStart"] = json_created_at_start

    json_created_at_end: str | Unset = UNSET
    if not isinstance(created_at_end, Unset):
        json_created_at_end = created_at_end.isoformat()
    params["createdAtEnd"] = json_created_at_end

    json_active_at_start: str | Unset = UNSET
    if not isinstance(active_at_start, Unset):
        json_active_at_start = active_at_start.isoformat()
    params["activeAtStart"] = json_active_at_start

    json_active_at_end: str | Unset = UNSET
    if not isinstance(active_at_end, Unset):
        json_active_at_end = active_at_end.isoformat()
    params["activeAtEnd"] = json_active_at_end

    json_deleted_at_start: str | Unset = UNSET
    if not isinstance(deleted_at_start, Unset):
        json_deleted_at_start = deleted_at_start.isoformat()
    params["deletedAtStart"] = json_deleted_at_start

    json_deleted_at_end: str | Unset = UNSET
    if not isinstance(deleted_at_end, Unset):
        json_deleted_at_end = deleted_at_end.isoformat()
    params["deletedAtEnd"] = json_deleted_at_end

    json_type_i_ds: list[int] | Unset = UNSET
    if not isinstance(type_i_ds, Unset):
        json_type_i_ds = type_i_ds


    params["typeIDs"] = json_type_i_ds

    json_size: list[str] | Unset = UNSET
    if not isinstance(size, Unset):
        json_size = size


    params["size"] = json_size

    json_regions: list[str] | Unset = UNSET
    if not isinstance(regions, Unset):
        json_regions = regions


    params["regions"] = json_regions

    json_ou_i_ds: list[int] | Unset = UNSET
    if not isinstance(ou_i_ds, Unset):
        json_ou_i_ds = ou_i_ds


    params["ouIDs"] = json_ou_i_ds

    json_project_i_ds: list[int] | Unset = UNSET
    if not isinstance(project_i_ds, Unset):
        json_project_i_ds = project_i_ds


    params["projectIDs"] = json_project_i_ds

    json_account_i_ds: list[int] | Unset = UNSET
    if not isinstance(account_i_ds, Unset):
        json_account_i_ds = account_i_ds


    params["accountIDs"] = json_account_i_ds

    params["keyword"] = keyword

    params["includeResourceDetails"] = include_resource_details

    params["includeResourceAccess"] = include_resource_access


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/resource-inventory/export",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ExportResourceListItemsResponse400 | ExportResourceListItemsResponse401 | ExportResourceListItemsResponse403 | ExportResourceListItemsResponse422 | ExportResourceListItemsResponse500 | File | None:
    if response.status_code == 200:
        response_200 = File(
             payload = BytesIO(response.json())
        )



        return response_200

    if response.status_code == 400:
        response_400 = ExportResourceListItemsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ExportResourceListItemsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ExportResourceListItemsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = ExportResourceListItemsResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = ExportResourceListItemsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ExportResourceListItemsResponse400 | ExportResourceListItemsResponse401 | ExportResourceListItemsResponse403 | ExportResourceListItemsResponse422 | ExportResourceListItemsResponse500 | File]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    cloud_provider_i_ds: list[int] | Unset = UNSET,
    include_deleted: bool | Unset = UNSET,
    created_at_start: datetime.datetime | Unset = UNSET,
    created_at_end: datetime.datetime | Unset = UNSET,
    active_at_start: datetime.datetime | Unset = UNSET,
    active_at_end: datetime.datetime | Unset = UNSET,
    deleted_at_start: datetime.datetime | Unset = UNSET,
    deleted_at_end: datetime.datetime | Unset = UNSET,
    type_i_ds: list[int] | Unset = UNSET,
    size: list[str] | Unset = UNSET,
    regions: list[str] | Unset = UNSET,
    ou_i_ds: list[int] | Unset = UNSET,
    project_i_ds: list[int] | Unset = UNSET,
    account_i_ds: list[int] | Unset = UNSET,
    keyword: str | Unset = UNSET,
    include_resource_details: bool | Unset = UNSET,
    include_resource_access: bool | Unset = UNSET,

) -> Response[ExportResourceListItemsResponse400 | ExportResourceListItemsResponse401 | ExportResourceListItemsResponse403 | ExportResourceListItemsResponse422 | ExportResourceListItemsResponse500 | File]:
    """ Exports resource inventory search results.

    Args:
        cloud_provider_i_ds (list[int] | Unset):
        include_deleted (bool | Unset):
        created_at_start (datetime.datetime | Unset):
        created_at_end (datetime.datetime | Unset):
        active_at_start (datetime.datetime | Unset):
        active_at_end (datetime.datetime | Unset):
        deleted_at_start (datetime.datetime | Unset):
        deleted_at_end (datetime.datetime | Unset):
        type_i_ds (list[int] | Unset):
        size (list[str] | Unset):
        regions (list[str] | Unset):
        ou_i_ds (list[int] | Unset):
        project_i_ds (list[int] | Unset):
        account_i_ds (list[int] | Unset):
        keyword (str | Unset):
        include_resource_details (bool | Unset):
        include_resource_access (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExportResourceListItemsResponse400 | ExportResourceListItemsResponse401 | ExportResourceListItemsResponse403 | ExportResourceListItemsResponse422 | ExportResourceListItemsResponse500 | File]
     """


    kwargs = _get_kwargs(
        cloud_provider_i_ds=cloud_provider_i_ds,
include_deleted=include_deleted,
created_at_start=created_at_start,
created_at_end=created_at_end,
active_at_start=active_at_start,
active_at_end=active_at_end,
deleted_at_start=deleted_at_start,
deleted_at_end=deleted_at_end,
type_i_ds=type_i_ds,
size=size,
regions=regions,
ou_i_ds=ou_i_ds,
project_i_ds=project_i_ds,
account_i_ds=account_i_ds,
keyword=keyword,
include_resource_details=include_resource_details,
include_resource_access=include_resource_access,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    cloud_provider_i_ds: list[int] | Unset = UNSET,
    include_deleted: bool | Unset = UNSET,
    created_at_start: datetime.datetime | Unset = UNSET,
    created_at_end: datetime.datetime | Unset = UNSET,
    active_at_start: datetime.datetime | Unset = UNSET,
    active_at_end: datetime.datetime | Unset = UNSET,
    deleted_at_start: datetime.datetime | Unset = UNSET,
    deleted_at_end: datetime.datetime | Unset = UNSET,
    type_i_ds: list[int] | Unset = UNSET,
    size: list[str] | Unset = UNSET,
    regions: list[str] | Unset = UNSET,
    ou_i_ds: list[int] | Unset = UNSET,
    project_i_ds: list[int] | Unset = UNSET,
    account_i_ds: list[int] | Unset = UNSET,
    keyword: str | Unset = UNSET,
    include_resource_details: bool | Unset = UNSET,
    include_resource_access: bool | Unset = UNSET,

) -> ExportResourceListItemsResponse400 | ExportResourceListItemsResponse401 | ExportResourceListItemsResponse403 | ExportResourceListItemsResponse422 | ExportResourceListItemsResponse500 | File | None:
    """ Exports resource inventory search results.

    Args:
        cloud_provider_i_ds (list[int] | Unset):
        include_deleted (bool | Unset):
        created_at_start (datetime.datetime | Unset):
        created_at_end (datetime.datetime | Unset):
        active_at_start (datetime.datetime | Unset):
        active_at_end (datetime.datetime | Unset):
        deleted_at_start (datetime.datetime | Unset):
        deleted_at_end (datetime.datetime | Unset):
        type_i_ds (list[int] | Unset):
        size (list[str] | Unset):
        regions (list[str] | Unset):
        ou_i_ds (list[int] | Unset):
        project_i_ds (list[int] | Unset):
        account_i_ds (list[int] | Unset):
        keyword (str | Unset):
        include_resource_details (bool | Unset):
        include_resource_access (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExportResourceListItemsResponse400 | ExportResourceListItemsResponse401 | ExportResourceListItemsResponse403 | ExportResourceListItemsResponse422 | ExportResourceListItemsResponse500 | File
     """


    return sync_detailed(
        client=client,
cloud_provider_i_ds=cloud_provider_i_ds,
include_deleted=include_deleted,
created_at_start=created_at_start,
created_at_end=created_at_end,
active_at_start=active_at_start,
active_at_end=active_at_end,
deleted_at_start=deleted_at_start,
deleted_at_end=deleted_at_end,
type_i_ds=type_i_ds,
size=size,
regions=regions,
ou_i_ds=ou_i_ds,
project_i_ds=project_i_ds,
account_i_ds=account_i_ds,
keyword=keyword,
include_resource_details=include_resource_details,
include_resource_access=include_resource_access,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cloud_provider_i_ds: list[int] | Unset = UNSET,
    include_deleted: bool | Unset = UNSET,
    created_at_start: datetime.datetime | Unset = UNSET,
    created_at_end: datetime.datetime | Unset = UNSET,
    active_at_start: datetime.datetime | Unset = UNSET,
    active_at_end: datetime.datetime | Unset = UNSET,
    deleted_at_start: datetime.datetime | Unset = UNSET,
    deleted_at_end: datetime.datetime | Unset = UNSET,
    type_i_ds: list[int] | Unset = UNSET,
    size: list[str] | Unset = UNSET,
    regions: list[str] | Unset = UNSET,
    ou_i_ds: list[int] | Unset = UNSET,
    project_i_ds: list[int] | Unset = UNSET,
    account_i_ds: list[int] | Unset = UNSET,
    keyword: str | Unset = UNSET,
    include_resource_details: bool | Unset = UNSET,
    include_resource_access: bool | Unset = UNSET,

) -> Response[ExportResourceListItemsResponse400 | ExportResourceListItemsResponse401 | ExportResourceListItemsResponse403 | ExportResourceListItemsResponse422 | ExportResourceListItemsResponse500 | File]:
    """ Exports resource inventory search results.

    Args:
        cloud_provider_i_ds (list[int] | Unset):
        include_deleted (bool | Unset):
        created_at_start (datetime.datetime | Unset):
        created_at_end (datetime.datetime | Unset):
        active_at_start (datetime.datetime | Unset):
        active_at_end (datetime.datetime | Unset):
        deleted_at_start (datetime.datetime | Unset):
        deleted_at_end (datetime.datetime | Unset):
        type_i_ds (list[int] | Unset):
        size (list[str] | Unset):
        regions (list[str] | Unset):
        ou_i_ds (list[int] | Unset):
        project_i_ds (list[int] | Unset):
        account_i_ds (list[int] | Unset):
        keyword (str | Unset):
        include_resource_details (bool | Unset):
        include_resource_access (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExportResourceListItemsResponse400 | ExportResourceListItemsResponse401 | ExportResourceListItemsResponse403 | ExportResourceListItemsResponse422 | ExportResourceListItemsResponse500 | File]
     """


    kwargs = _get_kwargs(
        cloud_provider_i_ds=cloud_provider_i_ds,
include_deleted=include_deleted,
created_at_start=created_at_start,
created_at_end=created_at_end,
active_at_start=active_at_start,
active_at_end=active_at_end,
deleted_at_start=deleted_at_start,
deleted_at_end=deleted_at_end,
type_i_ds=type_i_ds,
size=size,
regions=regions,
ou_i_ds=ou_i_ds,
project_i_ds=project_i_ds,
account_i_ds=account_i_ds,
keyword=keyword,
include_resource_details=include_resource_details,
include_resource_access=include_resource_access,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    cloud_provider_i_ds: list[int] | Unset = UNSET,
    include_deleted: bool | Unset = UNSET,
    created_at_start: datetime.datetime | Unset = UNSET,
    created_at_end: datetime.datetime | Unset = UNSET,
    active_at_start: datetime.datetime | Unset = UNSET,
    active_at_end: datetime.datetime | Unset = UNSET,
    deleted_at_start: datetime.datetime | Unset = UNSET,
    deleted_at_end: datetime.datetime | Unset = UNSET,
    type_i_ds: list[int] | Unset = UNSET,
    size: list[str] | Unset = UNSET,
    regions: list[str] | Unset = UNSET,
    ou_i_ds: list[int] | Unset = UNSET,
    project_i_ds: list[int] | Unset = UNSET,
    account_i_ds: list[int] | Unset = UNSET,
    keyword: str | Unset = UNSET,
    include_resource_details: bool | Unset = UNSET,
    include_resource_access: bool | Unset = UNSET,

) -> ExportResourceListItemsResponse400 | ExportResourceListItemsResponse401 | ExportResourceListItemsResponse403 | ExportResourceListItemsResponse422 | ExportResourceListItemsResponse500 | File | None:
    """ Exports resource inventory search results.

    Args:
        cloud_provider_i_ds (list[int] | Unset):
        include_deleted (bool | Unset):
        created_at_start (datetime.datetime | Unset):
        created_at_end (datetime.datetime | Unset):
        active_at_start (datetime.datetime | Unset):
        active_at_end (datetime.datetime | Unset):
        deleted_at_start (datetime.datetime | Unset):
        deleted_at_end (datetime.datetime | Unset):
        type_i_ds (list[int] | Unset):
        size (list[str] | Unset):
        regions (list[str] | Unset):
        ou_i_ds (list[int] | Unset):
        project_i_ds (list[int] | Unset):
        account_i_ds (list[int] | Unset):
        keyword (str | Unset):
        include_resource_details (bool | Unset):
        include_resource_access (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExportResourceListItemsResponse400 | ExportResourceListItemsResponse401 | ExportResourceListItemsResponse403 | ExportResourceListItemsResponse422 | ExportResourceListItemsResponse500 | File
     """


    return (await asyncio_detailed(
        client=client,
cloud_provider_i_ds=cloud_provider_i_ds,
include_deleted=include_deleted,
created_at_start=created_at_start,
created_at_end=created_at_end,
active_at_start=active_at_start,
active_at_end=active_at_end,
deleted_at_start=deleted_at_start,
deleted_at_end=deleted_at_end,
type_i_ds=type_i_ds,
size=size,
regions=regions,
ou_i_ds=ou_i_ds,
project_i_ds=project_i_ds,
account_i_ds=account_i_ds,
keyword=keyword,
include_resource_details=include_resource_details,
include_resource_access=include_resource_access,

    )).parsed
