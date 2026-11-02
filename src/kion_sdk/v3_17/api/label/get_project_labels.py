from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_project_labels_response_200 import GetProjectLabelsResponse200
from ...models.get_project_labels_response_400 import GetProjectLabelsResponse400
from ...models.get_project_labels_response_401 import GetProjectLabelsResponse401
from ...models.get_project_labels_response_403 import GetProjectLabelsResponse403
from ...models.get_project_labels_response_500 import GetProjectLabelsResponse500
from typing import cast



def _get_kwargs(
    project_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/project/{project_id}/labels".format(project_id=quote(str(project_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetProjectLabelsResponse200 | GetProjectLabelsResponse400 | GetProjectLabelsResponse401 | GetProjectLabelsResponse403 | GetProjectLabelsResponse500 | None:
    if response.status_code == 200:
        response_200 = GetProjectLabelsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetProjectLabelsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetProjectLabelsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetProjectLabelsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetProjectLabelsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetProjectLabelsResponse200 | GetProjectLabelsResponse400 | GetProjectLabelsResponse401 | GetProjectLabelsResponse403 | GetProjectLabelsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetProjectLabelsResponse200 | GetProjectLabelsResponse400 | GetProjectLabelsResponse401 | GetProjectLabelsResponse403 | GetProjectLabelsResponse500]:
    """ Gets all labels associated with a given project ID.

    Args:
        project_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProjectLabelsResponse200 | GetProjectLabelsResponse400 | GetProjectLabelsResponse401 | GetProjectLabelsResponse403 | GetProjectLabelsResponse500]
     """


    kwargs = _get_kwargs(
        project_id=project_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    project_id: int,
    *,
    client: AuthenticatedClient,

) -> GetProjectLabelsResponse200 | GetProjectLabelsResponse400 | GetProjectLabelsResponse401 | GetProjectLabelsResponse403 | GetProjectLabelsResponse500 | None:
    """ Gets all labels associated with a given project ID.

    Args:
        project_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProjectLabelsResponse200 | GetProjectLabelsResponse400 | GetProjectLabelsResponse401 | GetProjectLabelsResponse403 | GetProjectLabelsResponse500
     """


    return sync_detailed(
        project_id=project_id,
client=client,

    ).parsed

async def asyncio_detailed(
    project_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetProjectLabelsResponse200 | GetProjectLabelsResponse400 | GetProjectLabelsResponse401 | GetProjectLabelsResponse403 | GetProjectLabelsResponse500]:
    """ Gets all labels associated with a given project ID.

    Args:
        project_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProjectLabelsResponse200 | GetProjectLabelsResponse400 | GetProjectLabelsResponse401 | GetProjectLabelsResponse403 | GetProjectLabelsResponse500]
     """


    kwargs = _get_kwargs(
        project_id=project_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    project_id: int,
    *,
    client: AuthenticatedClient,

) -> GetProjectLabelsResponse200 | GetProjectLabelsResponse400 | GetProjectLabelsResponse401 | GetProjectLabelsResponse403 | GetProjectLabelsResponse500 | None:
    """ Gets all labels associated with a given project ID.

    Args:
        project_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProjectLabelsResponse200 | GetProjectLabelsResponse400 | GetProjectLabelsResponse401 | GetProjectLabelsResponse403 | GetProjectLabelsResponse500
     """


    return (await asyncio_detailed(
        project_id=project_id,
client=client,

    )).parsed
