from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_idms_group_association_response_200 import DeleteIDMSGroupAssociationResponse200
from ...models.delete_idms_group_association_response_400 import DeleteIDMSGroupAssociationResponse400
from ...models.delete_idms_group_association_response_401 import DeleteIDMSGroupAssociationResponse401
from ...models.delete_idms_group_association_response_403 import DeleteIDMSGroupAssociationResponse403
from ...models.delete_idms_group_association_response_404 import DeleteIDMSGroupAssociationResponse404
from ...models.delete_idms_group_association_response_500 import DeleteIDMSGroupAssociationResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/idms/group-association/{id}".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteIDMSGroupAssociationResponse200 | DeleteIDMSGroupAssociationResponse400 | DeleteIDMSGroupAssociationResponse401 | DeleteIDMSGroupAssociationResponse403 | DeleteIDMSGroupAssociationResponse404 | DeleteIDMSGroupAssociationResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteIDMSGroupAssociationResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteIDMSGroupAssociationResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteIDMSGroupAssociationResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteIDMSGroupAssociationResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteIDMSGroupAssociationResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = DeleteIDMSGroupAssociationResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteIDMSGroupAssociationResponse200 | DeleteIDMSGroupAssociationResponse400 | DeleteIDMSGroupAssociationResponse401 | DeleteIDMSGroupAssociationResponse403 | DeleteIDMSGroupAssociationResponse404 | DeleteIDMSGroupAssociationResponse500]:
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

) -> Response[DeleteIDMSGroupAssociationResponse200 | DeleteIDMSGroupAssociationResponse400 | DeleteIDMSGroupAssociationResponse401 | DeleteIDMSGroupAssociationResponse403 | DeleteIDMSGroupAssociationResponse404 | DeleteIDMSGroupAssociationResponse500]:
    """ Deletes a saml IDMS user group association from the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteIDMSGroupAssociationResponse200 | DeleteIDMSGroupAssociationResponse400 | DeleteIDMSGroupAssociationResponse401 | DeleteIDMSGroupAssociationResponse403 | DeleteIDMSGroupAssociationResponse404 | DeleteIDMSGroupAssociationResponse500]
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

) -> DeleteIDMSGroupAssociationResponse200 | DeleteIDMSGroupAssociationResponse400 | DeleteIDMSGroupAssociationResponse401 | DeleteIDMSGroupAssociationResponse403 | DeleteIDMSGroupAssociationResponse404 | DeleteIDMSGroupAssociationResponse500 | None:
    """ Deletes a saml IDMS user group association from the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteIDMSGroupAssociationResponse200 | DeleteIDMSGroupAssociationResponse400 | DeleteIDMSGroupAssociationResponse401 | DeleteIDMSGroupAssociationResponse403 | DeleteIDMSGroupAssociationResponse404 | DeleteIDMSGroupAssociationResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteIDMSGroupAssociationResponse200 | DeleteIDMSGroupAssociationResponse400 | DeleteIDMSGroupAssociationResponse401 | DeleteIDMSGroupAssociationResponse403 | DeleteIDMSGroupAssociationResponse404 | DeleteIDMSGroupAssociationResponse500]:
    """ Deletes a saml IDMS user group association from the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteIDMSGroupAssociationResponse200 | DeleteIDMSGroupAssociationResponse400 | DeleteIDMSGroupAssociationResponse401 | DeleteIDMSGroupAssociationResponse403 | DeleteIDMSGroupAssociationResponse404 | DeleteIDMSGroupAssociationResponse500]
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

) -> DeleteIDMSGroupAssociationResponse200 | DeleteIDMSGroupAssociationResponse400 | DeleteIDMSGroupAssociationResponse401 | DeleteIDMSGroupAssociationResponse403 | DeleteIDMSGroupAssociationResponse404 | DeleteIDMSGroupAssociationResponse500 | None:
    """ Deletes a saml IDMS user group association from the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteIDMSGroupAssociationResponse200 | DeleteIDMSGroupAssociationResponse400 | DeleteIDMSGroupAssociationResponse401 | DeleteIDMSGroupAssociationResponse403 | DeleteIDMSGroupAssociationResponse404 | DeleteIDMSGroupAssociationResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
