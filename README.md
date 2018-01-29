
# SampleServe API

## Intro

Built on Flask, this API powers React clients on the web and mobile with React Native. The API is available from multiple subdomains, for each Lab to have it's own instance of the app.

### Patterns

Each API endpoint uses a [Flask MethodView](http://flask.pocoo.org/docs/0.12/api/#flask.views.MethodView). Before each route is reached, [validators](#validators) are run via decorators. Then the posted JSON is checked against a [JSON Schema](#schema) for correctness and authorization. Once validated, the query is run against the database model as a [subquery](#subquery). Finally, the JSON response is returned, whether the request is successful or throws an [error](#errors).

#### Versioning

Since the mobile app will initially use v1, all routes are imported into a collecting file named `v1.py`. The routes are then imported again to the app factory for attachment. This is done so that a new `v2` API can be seamless, while leaving the v1 API up and running.

#### Validators

Validators check access permissions, JSON validity and populate commonly used objects into Flask's global object, `g`. These objects are:

 - `current_role`: The core of authorization in the rest of the app
 - `current_lab`: The Lab context based on the API subdomain.

Permissions are checked via properties on the MethodView, describing which roles have access to which API methods. Besides purely checking sigined in/signed out, this is the first authorization step.

For example, if we want to give LabAdmins the ability to create users, but not give that ability to Consultants (while still allowing them to view users, we can do this.

```
get_roles = ['LabAdmin', 'Consultant']
post_roles = ['LabAdmin']
```

#### Schema

Once a route is accessed, the JSON validates against an appropriate JSON Schema, stored alongside the views file. Schemas can be different depending on the `current_role`. For example, we might want to allow an Admin to change a users company, but we might not want that user to be able to switch to a different company on their own.

#### Subquery

Models can extend the base query by adding extra parameters before the query is returned, based on the user's role. For example, an Admin can see all Sites belonging to any Lab. All other users can only see Sites belonging to their own Lab:

```
if current_role == 'Admin':
    return model.query
return model.query.filter_by(lab=site.lab)
```

This allows us to run queries on a higher level without worrying about leaking data, as it will only return data the user can access:

```
return jsonify(Sites.role_query.all())
```

#### Errors

Whether it's a 404 error or a database error, all errors should be returned as JSON. This is done by calling `Flask.abort` with an error code, or by raising an exception handled by `Flask.register_error_handler`.

## Data

[Users Readme](https://github.com/NickWoodhams/sampleserve-api/tree/master/sampleserve/users).

## Setup

    docker-compose exec app flask dropdb
    docker-compose exec app flask initdb
    docker-compose exec app flask populatedb
    docker-compose exec app alembic current
    docker-compose exec app alembic stamp head
    docker-compose exec app flask cleanup_substances
    docker-compose exec app flask update_sitemap_urls
