from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_project_datasets_response_200 import GetProjectDatasetsResponse200
from ...models.get_project_datasets_response_401 import GetProjectDatasetsResponse401
from ...models.get_project_datasets_response_403 import GetProjectDatasetsResponse403
from ...models.get_project_datasets_response_404 import GetProjectDatasetsResponse404
from ...models.get_project_datasets_response_500 import GetProjectDatasetsResponse500
from typing import cast



def _get_kwargs(
    id: int,
    project_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/gcp/service-account/{id}/projects/{project_id}/datasets".format(id=quote(str(id), safe=""),project_id=quote(str(project_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetProjectDatasetsResponse200 | GetProjectDatasetsResponse401 | GetProjectDatasetsResponse403 | GetProjectDatasetsResponse404 | GetProjectDatasetsResponse500 | None:
    if response.status_code == 200:
        response_200 = GetProjectDatasetsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetProjectDatasetsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetProjectDatasetsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetProjectDatasetsResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetProjectDatasetsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetProjectDatasetsResponse200 | GetProjectDatasetsResponse401 | GetProjectDatasetsResponse403 | GetProjectDatasetsResponse404 | GetProjectDatasetsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    project_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetProjectDatasetsResponse200 | GetProjectDatasetsResponse401 | GetProjectDatasetsResponse403 | GetProjectDatasetsResponse404 | GetProjectDatasetsResponse500]:
    """ Returns the bigquery datasets in the google cloud project.

    Args:
        id (int):
        project_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProjectDatasetsResponse200 | GetProjectDatasetsResponse401 | GetProjectDatasetsResponse403 | GetProjectDatasetsResponse404 | GetProjectDatasetsResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
project_id=project_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    project_id: int,
    *,
    client: AuthenticatedClient,

) -> GetProjectDatasetsResponse200 | GetProjectDatasetsResponse401 | GetProjectDatasetsResponse403 | GetProjectDatasetsResponse404 | GetProjectDatasetsResponse500 | None:
    """ Returns the bigquery datasets in the google cloud project.

    Args:
        id (int):
        project_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProjectDatasetsResponse200 | GetProjectDatasetsResponse401 | GetProjectDatasetsResponse403 | GetProjectDatasetsResponse404 | GetProjectDatasetsResponse500
     """


    return sync_detailed(
        id=id,
project_id=project_id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    project_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetProjectDatasetsResponse200 | GetProjectDatasetsResponse401 | GetProjectDatasetsResponse403 | GetProjectDatasetsResponse404 | GetProjectDatasetsResponse500]:
    """ Returns the bigquery datasets in the google cloud project.

    Args:
        id (int):
        project_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProjectDatasetsResponse200 | GetProjectDatasetsResponse401 | GetProjectDatasetsResponse403 | GetProjectDatasetsResponse404 | GetProjectDatasetsResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
project_id=project_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    project_id: int,
    *,
    client: AuthenticatedClient,

) -> GetProjectDatasetsResponse200 | GetProjectDatasetsResponse401 | GetProjectDatasetsResponse403 | GetProjectDatasetsResponse404 | GetProjectDatasetsResponse500 | None:
    """ Returns the bigquery datasets in the google cloud project.

    Args:
        id (int):
        project_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProjectDatasetsResponse200 | GetProjectDatasetsResponse401 | GetProjectDatasetsResponse403 | GetProjectDatasetsResponse404 | GetProjectDatasetsResponse500
     """


    return (await asyncio_detailed(
        id=id,
project_id=project_id,
client=client,

    )).parsed
