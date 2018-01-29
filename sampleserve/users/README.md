
## Users

Users are associated with a lab. To access a new lab, a person must create a new user account (the same email address can be used).

Each user is assigned a role. Roles give users different permissions. The possible roles are listed here: http://test.sampleserve.dev/api/v1/roles/

- Admin
- LabAdmin
- LabAssociate
- CompanyAdmin
- CompanyAssociate
- ClientManager
- Technician

The Admin role gives a user access to all data, but queries must still be made to the correct API endpoint.

The role can be checked in several different places for access. It can be set on the API view, like the site view:

```
class SiteView(PrivateView):
    model = Site
    get_roles = ['LabAdmin', 'LabAssociate',]
    post_roles = ['LabAdmin', 'LabAssociate',]
    patch_roles = ['LabAdmin', 'LabAssociate',]
    delete_roles = ['LabAdmin',]
```

It can be used for more granular permissions in each object method, where it is available as `g.current_role`. This is useful for limiting what values certain users can write to fields, while still allowing higher users better access.

## User Relationships

Users can be associated with Companies and Sites as well. This is useful for permissions on the company admin level and below:

```
user.companies.append(CSI)
user.sites.append(SiteA)
```

To do this via the API (along with any other many-to-many relationship), send a normal PATCH request to the user endpoint, with `"add"` and `"remove"` keys:

```
PATCH
/users/1
{
    "companies": {
        "add": [1],
        "remove": [2]
    }
}
```

This API call removes the user's association with company 2, and associates the user with company 1.

Both `"add"` and `"remove"` keys must be included, but they can be empty arrays.
