from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_project_ca_rs_by_project_id_response_200 import GetProjectCARsByProjectIDResponse200
from ...models.get_project_ca_rs_by_project_id_response_401 import GetProjectCARsByProjectIDResponse401
from ...models.get_project_ca_rs_by_project_id_response_403 import GetProjectCARsByProjectIDResponse403
from ...models.get_project_ca_rs_by_project_id_response_404 import GetProjectCARsByProjectIDResponse404
from ...models.get_project_ca_rs_by_project_id_response_500 import GetProjectCARsByProjectIDResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    detailed: bool | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["detailed"] = detailed


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/project/{id}/project-cloud-access-role".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetProjectCARsByProjectIDResponse200 | GetProjectCARsByProjectIDResponse401 | GetProjectCARsByProjectIDResponse403 | GetProjectCARsByProjectIDResponse404 | GetProjectCARsByProjectIDResponse500 | None:
    if response.status_code == 200:
        response_200 = GetProjectCARsByProjectIDResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetProjectCARsByProjectIDResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetProjectCARsByProjectIDResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetProjectCARsByProjectIDResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetProjectCARsByProjectIDResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetProjectCARsByProjectIDResponse200 | GetProjectCARsByProjectIDResponse401 | GetProjectCARsByProjectIDResponse403 | GetProjectCARsByProjectIDResponse404 | GetProjectCARsByProjectIDResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    detailed: bool | Unset = UNSET,

) -> Response[GetProjectCARsByProjectIDResponse200 | GetProjectCARsByProjectIDResponse401 | GetProjectCARsByProjectIDResponse403 | GetProjectCARsByProjectIDResponse404 | GetProjectCARsByProjectIDResponse500]:
    """ Returns a list of project cloud access roles that are associated with a project.

    Args:
        id (int):
        detailed (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProjectCARsByProjectIDResponse200 | GetProjectCARsByProjectIDResponse401 | GetProjectCARsByProjectIDResponse403 | GetProjectCARsByProjectIDResponse404 | GetProjectCARsByProjectIDResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
detailed=detailed,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    detailed: bool | Unset = UNSET,

) -> GetProjectCARsByProjectIDResponse200 | GetProjectCARsByProjectIDResponse401 | GetProjectCARsByProjectIDResponse403 | GetProjectCARsByProjectIDResponse404 | GetProjectCARsByProjectIDResponse500 | None:
    """ Returns a list of project cloud access roles that are associated with a project.

    Args:
        id (int):
        detailed (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProjectCARsByProjectIDResponse200 | GetProjectCARsByProjectIDResponse401 | GetProjectCARsByProjectIDResponse403 | GetProjectCARsByProjectIDResponse404 | GetProjectCARsByProjectIDResponse500
     """


    return sync_detailed(
        id=id,
client=client,
detailed=detailed,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    detailed: bool | Unset = UNSET,

) -> Response[GetProjectCARsByProjectIDResponse200 | GetProjectCARsByProjectIDResponse401 | GetProjectCARsByProjectIDResponse403 | GetProjectCARsByProjectIDResponse404 | GetProjectCARsByProjectIDResponse500]:
    """ Returns a list of project cloud access roles that are associated with a project.

    Args:
        id (int):
        detailed (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProjectCARsByProjectIDResponse200 | GetProjectCARsByProjectIDResponse401 | GetProjectCARsByProjectIDResponse403 | GetProjectCARsByProjectIDResponse404 | GetProjectCARsByProjectIDResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
detailed=detailed,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    detailed: bool | Unset = UNSET,

) -> GetProjectCARsByProjectIDResponse200 | GetProjectCARsByProjectIDResponse401 | GetProjectCARsByProjectIDResponse403 | GetProjectCARsByProjectIDResponse404 | GetProjectCARsByProjectIDResponse500 | None:
    """ Returns a list of project cloud access roles that are associated with a project.

    Args:
        id (int):
        detailed (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProjectCARsByProjectIDResponse200 | GetProjectCARsByProjectIDResponse401 | GetProjectCARsByProjectIDResponse403 | GetProjectCARsByProjectIDResponse404 | GetProjectCARsByProjectIDResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
detailed=detailed,

    )).parsed
