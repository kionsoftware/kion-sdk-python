from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_ou_index_response_200 import GetOUIndexResponse200
from ...models.get_ou_index_response_400 import GetOUIndexResponse400
from ...models.get_ou_index_response_401 import GetOUIndexResponse401
from ...models.get_ou_index_response_500 import GetOUIndexResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    name: str | Unset = UNSET,
    label: str | Unset = UNSET,
    label_key: str | Unset = UNSET,
    label_value: str | Unset = UNSET,
    label_id: str | Unset = UNSET,
    include_archived: str | Unset = 'false',
    parent_ou_id: str | Unset = UNSET,
    ancestor_ou_id: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["name"] = name

    params["label"] = label

    params["label_key"] = label_key

    params["label_value"] = label_value

    params["label_id"] = label_id

    params["includeArchived"] = include_archived

    params["parent_ou_id"] = parent_ou_id

    params["ancestor_ou_id"] = ancestor_ou_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/ou",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetOUIndexResponse200 | GetOUIndexResponse400 | GetOUIndexResponse401 | GetOUIndexResponse500 | None:
    if response.status_code == 200:
        response_200 = GetOUIndexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetOUIndexResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetOUIndexResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = GetOUIndexResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetOUIndexResponse200 | GetOUIndexResponse400 | GetOUIndexResponse401 | GetOUIndexResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    name: str | Unset = UNSET,
    label: str | Unset = UNSET,
    label_key: str | Unset = UNSET,
    label_value: str | Unset = UNSET,
    label_id: str | Unset = UNSET,
    include_archived: str | Unset = 'false',
    parent_ou_id: str | Unset = UNSET,
    ancestor_ou_id: str | Unset = UNSET,

) -> Response[GetOUIndexResponse200 | GetOUIndexResponse400 | GetOUIndexResponse401 | GetOUIndexResponse500]:
    """ Returns a list of OUs from the application.

    Args:
        name (str | Unset):
        label (str | Unset):
        label_key (str | Unset):
        label_value (str | Unset):
        label_id (str | Unset):
        include_archived (str | Unset):  Default: 'false'.
        parent_ou_id (str | Unset):
        ancestor_ou_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOUIndexResponse200 | GetOUIndexResponse400 | GetOUIndexResponse401 | GetOUIndexResponse500]
     """


    kwargs = _get_kwargs(
        name=name,
label=label,
label_key=label_key,
label_value=label_value,
label_id=label_id,
include_archived=include_archived,
parent_ou_id=parent_ou_id,
ancestor_ou_id=ancestor_ou_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    name: str | Unset = UNSET,
    label: str | Unset = UNSET,
    label_key: str | Unset = UNSET,
    label_value: str | Unset = UNSET,
    label_id: str | Unset = UNSET,
    include_archived: str | Unset = 'false',
    parent_ou_id: str | Unset = UNSET,
    ancestor_ou_id: str | Unset = UNSET,

) -> GetOUIndexResponse200 | GetOUIndexResponse400 | GetOUIndexResponse401 | GetOUIndexResponse500 | None:
    """ Returns a list of OUs from the application.

    Args:
        name (str | Unset):
        label (str | Unset):
        label_key (str | Unset):
        label_value (str | Unset):
        label_id (str | Unset):
        include_archived (str | Unset):  Default: 'false'.
        parent_ou_id (str | Unset):
        ancestor_ou_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOUIndexResponse200 | GetOUIndexResponse400 | GetOUIndexResponse401 | GetOUIndexResponse500
     """


    return sync_detailed(
        client=client,
name=name,
label=label,
label_key=label_key,
label_value=label_value,
label_id=label_id,
include_archived=include_archived,
parent_ou_id=parent_ou_id,
ancestor_ou_id=ancestor_ou_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    name: str | Unset = UNSET,
    label: str | Unset = UNSET,
    label_key: str | Unset = UNSET,
    label_value: str | Unset = UNSET,
    label_id: str | Unset = UNSET,
    include_archived: str | Unset = 'false',
    parent_ou_id: str | Unset = UNSET,
    ancestor_ou_id: str | Unset = UNSET,

) -> Response[GetOUIndexResponse200 | GetOUIndexResponse400 | GetOUIndexResponse401 | GetOUIndexResponse500]:
    """ Returns a list of OUs from the application.

    Args:
        name (str | Unset):
        label (str | Unset):
        label_key (str | Unset):
        label_value (str | Unset):
        label_id (str | Unset):
        include_archived (str | Unset):  Default: 'false'.
        parent_ou_id (str | Unset):
        ancestor_ou_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOUIndexResponse200 | GetOUIndexResponse400 | GetOUIndexResponse401 | GetOUIndexResponse500]
     """


    kwargs = _get_kwargs(
        name=name,
label=label,
label_key=label_key,
label_value=label_value,
label_id=label_id,
include_archived=include_archived,
parent_ou_id=parent_ou_id,
ancestor_ou_id=ancestor_ou_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    name: str | Unset = UNSET,
    label: str | Unset = UNSET,
    label_key: str | Unset = UNSET,
    label_value: str | Unset = UNSET,
    label_id: str | Unset = UNSET,
    include_archived: str | Unset = 'false',
    parent_ou_id: str | Unset = UNSET,
    ancestor_ou_id: str | Unset = UNSET,

) -> GetOUIndexResponse200 | GetOUIndexResponse400 | GetOUIndexResponse401 | GetOUIndexResponse500 | None:
    """ Returns a list of OUs from the application.

    Args:
        name (str | Unset):
        label (str | Unset):
        label_key (str | Unset):
        label_value (str | Unset):
        label_id (str | Unset):
        include_archived (str | Unset):  Default: 'false'.
        parent_ou_id (str | Unset):
        ancestor_ou_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOUIndexResponse200 | GetOUIndexResponse400 | GetOUIndexResponse401 | GetOUIndexResponse500
     """


    return (await asyncio_detailed(
        client=client,
name=name,
label=label,
label_key=label_key,
label_value=label_value,
label_id=label_id,
include_archived=include_archived,
parent_ou_id=parent_ou_id,
ancestor_ou_id=ancestor_ou_id,

    )).parsed
