from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_ami_response_200 import DeleteAMIResponse200
from ...models.delete_ami_response_401 import DeleteAMIResponse401
from ...models.delete_ami_response_403 import DeleteAMIResponse403
from ...models.delete_ami_response_404 import DeleteAMIResponse404
from ...models.delete_ami_response_500 import DeleteAMIResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/ami/{id}".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteAMIResponse200 | DeleteAMIResponse401 | DeleteAMIResponse403 | DeleteAMIResponse404 | DeleteAMIResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteAMIResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DeleteAMIResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteAMIResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteAMIResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = DeleteAMIResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteAMIResponse200 | DeleteAMIResponse401 | DeleteAMIResponse403 | DeleteAMIResponse404 | DeleteAMIResponse500]:
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

) -> Response[DeleteAMIResponse200 | DeleteAMIResponse401 | DeleteAMIResponse403 | DeleteAMIResponse404 | DeleteAMIResponse500]:
    """ Deletes an AMI in the application.

     AMIs exist in AWS accounts that are attached to a project.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteAMIResponse200 | DeleteAMIResponse401 | DeleteAMIResponse403 | DeleteAMIResponse404 | DeleteAMIResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,

) -> DeleteAMIResponse200 | DeleteAMIResponse401 | DeleteAMIResponse403 | DeleteAMIResponse404 | DeleteAMIResponse500 | None:
    """ Deletes an AMI in the application.

     AMIs exist in AWS accounts that are attached to a project.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteAMIResponse200 | DeleteAMIResponse401 | DeleteAMIResponse403 | DeleteAMIResponse404 | DeleteAMIResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteAMIResponse200 | DeleteAMIResponse401 | DeleteAMIResponse403 | DeleteAMIResponse404 | DeleteAMIResponse500]:
    """ Deletes an AMI in the application.

     AMIs exist in AWS accounts that are attached to a project.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteAMIResponse200 | DeleteAMIResponse401 | DeleteAMIResponse403 | DeleteAMIResponse404 | DeleteAMIResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,

) -> DeleteAMIResponse200 | DeleteAMIResponse401 | DeleteAMIResponse403 | DeleteAMIResponse404 | DeleteAMIResponse500 | None:
    """ Deletes an AMI in the application.

     AMIs exist in AWS accounts that are attached to a project.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteAMIResponse200 | DeleteAMIResponse401 | DeleteAMIResponse403 | DeleteAMIResponse404 | DeleteAMIResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
