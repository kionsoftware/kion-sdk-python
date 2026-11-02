from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_project_datasets_deprecated_response_200 import GetProjectDatasetsDeprecatedResponse200
from ...models.get_project_datasets_deprecated_response_401 import GetProjectDatasetsDeprecatedResponse401
from ...models.get_project_datasets_deprecated_response_403 import GetProjectDatasetsDeprecatedResponse403
from ...models.get_project_datasets_deprecated_response_404 import GetProjectDatasetsDeprecatedResponse404
from ...models.get_project_datasets_deprecated_response_500 import GetProjectDatasetsDeprecatedResponse500
from typing import cast



def _get_kwargs(
    id: int,
    ba_id: int,
    project_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/gcp/service-account/{id}/billing-accounts/{ba_id}/projects/{project_id}/datasets".format(id=quote(str(id), safe=""),ba_id=quote(str(ba_id), safe=""),project_id=quote(str(project_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetProjectDatasetsDeprecatedResponse200 | GetProjectDatasetsDeprecatedResponse401 | GetProjectDatasetsDeprecatedResponse403 | GetProjectDatasetsDeprecatedResponse404 | GetProjectDatasetsDeprecatedResponse500 | None:
    if response.status_code == 200:
        response_200 = GetProjectDatasetsDeprecatedResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetProjectDatasetsDeprecatedResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetProjectDatasetsDeprecatedResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetProjectDatasetsDeprecatedResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetProjectDatasetsDeprecatedResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetProjectDatasetsDeprecatedResponse200 | GetProjectDatasetsDeprecatedResponse401 | GetProjectDatasetsDeprecatedResponse403 | GetProjectDatasetsDeprecatedResponse404 | GetProjectDatasetsDeprecatedResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    ba_id: int,
    project_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetProjectDatasetsDeprecatedResponse200 | GetProjectDatasetsDeprecatedResponse401 | GetProjectDatasetsDeprecatedResponse403 | GetProjectDatasetsDeprecatedResponse404 | GetProjectDatasetsDeprecatedResponse500]:
    """ Returns the bigquery datasets in the google cloud project.

    Args:
        id (int):
        ba_id (int):
        project_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProjectDatasetsDeprecatedResponse200 | GetProjectDatasetsDeprecatedResponse401 | GetProjectDatasetsDeprecatedResponse403 | GetProjectDatasetsDeprecatedResponse404 | GetProjectDatasetsDeprecatedResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
ba_id=ba_id,
project_id=project_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    ba_id: int,
    project_id: int,
    *,
    client: AuthenticatedClient,

) -> GetProjectDatasetsDeprecatedResponse200 | GetProjectDatasetsDeprecatedResponse401 | GetProjectDatasetsDeprecatedResponse403 | GetProjectDatasetsDeprecatedResponse404 | GetProjectDatasetsDeprecatedResponse500 | None:
    """ Returns the bigquery datasets in the google cloud project.

    Args:
        id (int):
        ba_id (int):
        project_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProjectDatasetsDeprecatedResponse200 | GetProjectDatasetsDeprecatedResponse401 | GetProjectDatasetsDeprecatedResponse403 | GetProjectDatasetsDeprecatedResponse404 | GetProjectDatasetsDeprecatedResponse500
     """


    return sync_detailed(
        id=id,
ba_id=ba_id,
project_id=project_id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    ba_id: int,
    project_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetProjectDatasetsDeprecatedResponse200 | GetProjectDatasetsDeprecatedResponse401 | GetProjectDatasetsDeprecatedResponse403 | GetProjectDatasetsDeprecatedResponse404 | GetProjectDatasetsDeprecatedResponse500]:
    """ Returns the bigquery datasets in the google cloud project.

    Args:
        id (int):
        ba_id (int):
        project_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProjectDatasetsDeprecatedResponse200 | GetProjectDatasetsDeprecatedResponse401 | GetProjectDatasetsDeprecatedResponse403 | GetProjectDatasetsDeprecatedResponse404 | GetProjectDatasetsDeprecatedResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
ba_id=ba_id,
project_id=project_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    ba_id: int,
    project_id: int,
    *,
    client: AuthenticatedClient,

) -> GetProjectDatasetsDeprecatedResponse200 | GetProjectDatasetsDeprecatedResponse401 | GetProjectDatasetsDeprecatedResponse403 | GetProjectDatasetsDeprecatedResponse404 | GetProjectDatasetsDeprecatedResponse500 | None:
    """ Returns the bigquery datasets in the google cloud project.

    Args:
        id (int):
        ba_id (int):
        project_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProjectDatasetsDeprecatedResponse200 | GetProjectDatasetsDeprecatedResponse401 | GetProjectDatasetsDeprecatedResponse403 | GetProjectDatasetsDeprecatedResponse404 | GetProjectDatasetsDeprecatedResponse500
     """


    return (await asyncio_detailed(
        id=id,
ba_id=ba_id,
project_id=project_id,
client=client,

    )).parsed
