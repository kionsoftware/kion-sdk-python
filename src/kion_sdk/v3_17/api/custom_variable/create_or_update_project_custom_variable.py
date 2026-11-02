from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_or_update_project_custom_variable_response_400 import CreateOrUpdateProjectCustomVariableResponse400
from ...models.create_or_update_project_custom_variable_response_401 import CreateOrUpdateProjectCustomVariableResponse401
from ...models.create_or_update_project_custom_variable_response_403 import CreateOrUpdateProjectCustomVariableResponse403
from ...models.create_or_update_project_custom_variable_response_404 import CreateOrUpdateProjectCustomVariableResponse404
from ...models.create_or_update_project_custom_variable_response_422 import CreateOrUpdateProjectCustomVariableResponse422
from ...models.create_or_update_project_custom_variable_response_500 import CreateOrUpdateProjectCustomVariableResponse500
from ...models.project_custom_variable_create_or_update import ProjectCustomVariableCreateOrUpdate
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    project_id: int,
    custom_variable_id: int,
    *,
    body: ProjectCustomVariableCreateOrUpdate | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v3/project/{project_id}/custom-variable/{custom_variable_id}".format(project_id=quote(str(project_id), safe=""),custom_variable_id=quote(str(custom_variable_id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | CreateOrUpdateProjectCustomVariableResponse400 | CreateOrUpdateProjectCustomVariableResponse401 | CreateOrUpdateProjectCustomVariableResponse403 | CreateOrUpdateProjectCustomVariableResponse404 | CreateOrUpdateProjectCustomVariableResponse422 | CreateOrUpdateProjectCustomVariableResponse500 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = CreateOrUpdateProjectCustomVariableResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = CreateOrUpdateProjectCustomVariableResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = CreateOrUpdateProjectCustomVariableResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = CreateOrUpdateProjectCustomVariableResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = CreateOrUpdateProjectCustomVariableResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = CreateOrUpdateProjectCustomVariableResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | CreateOrUpdateProjectCustomVariableResponse400 | CreateOrUpdateProjectCustomVariableResponse401 | CreateOrUpdateProjectCustomVariableResponse403 | CreateOrUpdateProjectCustomVariableResponse404 | CreateOrUpdateProjectCustomVariableResponse422 | CreateOrUpdateProjectCustomVariableResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: int,
    custom_variable_id: int,
    *,
    client: AuthenticatedClient,
    body: ProjectCustomVariableCreateOrUpdate | Unset = UNSET,

) -> Response[Any | CreateOrUpdateProjectCustomVariableResponse400 | CreateOrUpdateProjectCustomVariableResponse401 | CreateOrUpdateProjectCustomVariableResponse403 | CreateOrUpdateProjectCustomVariableResponse404 | CreateOrUpdateProjectCustomVariableResponse422 | CreateOrUpdateProjectCustomVariableResponse500]:
    """ Creates or updates a project custom variable override.

    Args:
        project_id (int):
        custom_variable_id (int):
        body (ProjectCustomVariableCreateOrUpdate | Unset): ProjectCustomVariableCreateOrUpdate
            represents the fields necessary to create or update a project custom variable override.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateOrUpdateProjectCustomVariableResponse400 | CreateOrUpdateProjectCustomVariableResponse401 | CreateOrUpdateProjectCustomVariableResponse403 | CreateOrUpdateProjectCustomVariableResponse404 | CreateOrUpdateProjectCustomVariableResponse422 | CreateOrUpdateProjectCustomVariableResponse500]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
custom_variable_id=custom_variable_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    project_id: int,
    custom_variable_id: int,
    *,
    client: AuthenticatedClient,
    body: ProjectCustomVariableCreateOrUpdate | Unset = UNSET,

) -> Any | CreateOrUpdateProjectCustomVariableResponse400 | CreateOrUpdateProjectCustomVariableResponse401 | CreateOrUpdateProjectCustomVariableResponse403 | CreateOrUpdateProjectCustomVariableResponse404 | CreateOrUpdateProjectCustomVariableResponse422 | CreateOrUpdateProjectCustomVariableResponse500 | None:
    """ Creates or updates a project custom variable override.

    Args:
        project_id (int):
        custom_variable_id (int):
        body (ProjectCustomVariableCreateOrUpdate | Unset): ProjectCustomVariableCreateOrUpdate
            represents the fields necessary to create or update a project custom variable override.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateOrUpdateProjectCustomVariableResponse400 | CreateOrUpdateProjectCustomVariableResponse401 | CreateOrUpdateProjectCustomVariableResponse403 | CreateOrUpdateProjectCustomVariableResponse404 | CreateOrUpdateProjectCustomVariableResponse422 | CreateOrUpdateProjectCustomVariableResponse500
     """


    return sync_detailed(
        project_id=project_id,
custom_variable_id=custom_variable_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    project_id: int,
    custom_variable_id: int,
    *,
    client: AuthenticatedClient,
    body: ProjectCustomVariableCreateOrUpdate | Unset = UNSET,

) -> Response[Any | CreateOrUpdateProjectCustomVariableResponse400 | CreateOrUpdateProjectCustomVariableResponse401 | CreateOrUpdateProjectCustomVariableResponse403 | CreateOrUpdateProjectCustomVariableResponse404 | CreateOrUpdateProjectCustomVariableResponse422 | CreateOrUpdateProjectCustomVariableResponse500]:
    """ Creates or updates a project custom variable override.

    Args:
        project_id (int):
        custom_variable_id (int):
        body (ProjectCustomVariableCreateOrUpdate | Unset): ProjectCustomVariableCreateOrUpdate
            represents the fields necessary to create or update a project custom variable override.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateOrUpdateProjectCustomVariableResponse400 | CreateOrUpdateProjectCustomVariableResponse401 | CreateOrUpdateProjectCustomVariableResponse403 | CreateOrUpdateProjectCustomVariableResponse404 | CreateOrUpdateProjectCustomVariableResponse422 | CreateOrUpdateProjectCustomVariableResponse500]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
custom_variable_id=custom_variable_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    project_id: int,
    custom_variable_id: int,
    *,
    client: AuthenticatedClient,
    body: ProjectCustomVariableCreateOrUpdate | Unset = UNSET,

) -> Any | CreateOrUpdateProjectCustomVariableResponse400 | CreateOrUpdateProjectCustomVariableResponse401 | CreateOrUpdateProjectCustomVariableResponse403 | CreateOrUpdateProjectCustomVariableResponse404 | CreateOrUpdateProjectCustomVariableResponse422 | CreateOrUpdateProjectCustomVariableResponse500 | None:
    """ Creates or updates a project custom variable override.

    Args:
        project_id (int):
        custom_variable_id (int):
        body (ProjectCustomVariableCreateOrUpdate | Unset): ProjectCustomVariableCreateOrUpdate
            represents the fields necessary to create or update a project custom variable override.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateOrUpdateProjectCustomVariableResponse400 | CreateOrUpdateProjectCustomVariableResponse401 | CreateOrUpdateProjectCustomVariableResponse403 | CreateOrUpdateProjectCustomVariableResponse404 | CreateOrUpdateProjectCustomVariableResponse422 | CreateOrUpdateProjectCustomVariableResponse500
     """


    return (await asyncio_detailed(
        project_id=project_id,
custom_variable_id=custom_variable_id,
client=client,
body=body,

    )).parsed
