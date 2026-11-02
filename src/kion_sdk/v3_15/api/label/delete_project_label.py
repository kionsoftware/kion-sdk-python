from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_project_label_response_200 import DeleteProjectLabelResponse200
from ...models.delete_project_label_response_400 import DeleteProjectLabelResponse400
from ...models.delete_project_label_response_401 import DeleteProjectLabelResponse401
from ...models.delete_project_label_response_404 import DeleteProjectLabelResponse404
from ...models.delete_project_label_response_422 import DeleteProjectLabelResponse422
from ...models.delete_project_label_response_500 import DeleteProjectLabelResponse500
from typing import cast



def _get_kwargs(
    project_id: int,
    label_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/project/{project_id}/labels/{label_id}".format(project_id=quote(str(project_id), safe=""),label_id=quote(str(label_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteProjectLabelResponse200 | DeleteProjectLabelResponse400 | DeleteProjectLabelResponse401 | DeleteProjectLabelResponse404 | DeleteProjectLabelResponse422 | DeleteProjectLabelResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteProjectLabelResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteProjectLabelResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteProjectLabelResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = DeleteProjectLabelResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = DeleteProjectLabelResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = DeleteProjectLabelResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteProjectLabelResponse200 | DeleteProjectLabelResponse400 | DeleteProjectLabelResponse401 | DeleteProjectLabelResponse404 | DeleteProjectLabelResponse422 | DeleteProjectLabelResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: int,
    label_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteProjectLabelResponse200 | DeleteProjectLabelResponse400 | DeleteProjectLabelResponse401 | DeleteProjectLabelResponse404 | DeleteProjectLabelResponse422 | DeleteProjectLabelResponse500]:
    """ Removes a label from the given project by label ID.

    Args:
        project_id (int):
        label_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteProjectLabelResponse200 | DeleteProjectLabelResponse400 | DeleteProjectLabelResponse401 | DeleteProjectLabelResponse404 | DeleteProjectLabelResponse422 | DeleteProjectLabelResponse500]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
label_id=label_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    project_id: int,
    label_id: int,
    *,
    client: AuthenticatedClient,

) -> DeleteProjectLabelResponse200 | DeleteProjectLabelResponse400 | DeleteProjectLabelResponse401 | DeleteProjectLabelResponse404 | DeleteProjectLabelResponse422 | DeleteProjectLabelResponse500 | None:
    """ Removes a label from the given project by label ID.

    Args:
        project_id (int):
        label_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteProjectLabelResponse200 | DeleteProjectLabelResponse400 | DeleteProjectLabelResponse401 | DeleteProjectLabelResponse404 | DeleteProjectLabelResponse422 | DeleteProjectLabelResponse500
     """


    return sync_detailed(
        project_id=project_id,
label_id=label_id,
client=client,

    ).parsed

async def asyncio_detailed(
    project_id: int,
    label_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteProjectLabelResponse200 | DeleteProjectLabelResponse400 | DeleteProjectLabelResponse401 | DeleteProjectLabelResponse404 | DeleteProjectLabelResponse422 | DeleteProjectLabelResponse500]:
    """ Removes a label from the given project by label ID.

    Args:
        project_id (int):
        label_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteProjectLabelResponse200 | DeleteProjectLabelResponse400 | DeleteProjectLabelResponse401 | DeleteProjectLabelResponse404 | DeleteProjectLabelResponse422 | DeleteProjectLabelResponse500]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
label_id=label_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    project_id: int,
    label_id: int,
    *,
    client: AuthenticatedClient,

) -> DeleteProjectLabelResponse200 | DeleteProjectLabelResponse400 | DeleteProjectLabelResponse401 | DeleteProjectLabelResponse404 | DeleteProjectLabelResponse422 | DeleteProjectLabelResponse500 | None:
    """ Removes a label from the given project by label ID.

    Args:
        project_id (int):
        label_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteProjectLabelResponse200 | DeleteProjectLabelResponse400 | DeleteProjectLabelResponse401 | DeleteProjectLabelResponse404 | DeleteProjectLabelResponse422 | DeleteProjectLabelResponse500
     """


    return (await asyncio_detailed(
        project_id=project_id,
label_id=label_id,
client=client,

    )).parsed
