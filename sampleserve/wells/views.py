
from flask import abort, g, jsonify, request

from sampleserve.rest.views import BaseView
from sampleserve.rest.validators import validate_schema
from sampleserve.schemas import schema, date, number, integer, add_remove, string, array, boolean

from .models import (
    Well,
    Frequency,
    WellImage,
)


class WellsView(BaseView):
    model = Well

    def post(self):
        """POST /model

        Creates a new object of model, returning it as JSON with an `id` key.
        """
        if hasattr(self, 'post_roles'):
            if current_user.is_anonymous or not current_user.role:
                abort(httplib.UNAUTHORIZED)
            if current_user.role.name not in self.post_roles:
                abort(httplib.UNAUTHORIZED)

        r = request.json
        post_schema = {
            "$schema": schema,
            "properties": {
                "site_id": integer,
                "active": boolean,
                "title": string,
                "top_of_casing": number,
                "xpos": integer,
                "ypos": integer,
                "xpos_fields": integer,
                "ypos_fields": integer,
            },
            "required": [
                "site_id",
                "title",
            ]
        }
        validate_schema(r, post_schema)

        instance = self.model()
        instance.patch(g.body)
        instance.save_or_error()
        res = instance.json()
        return jsonify(res)


class FrequenciesView(BaseView):
    model = Frequency


class WellImagesView(BaseView):
    model = WellImage


wells = WellsView.as_view('wells')
frequencies = FrequenciesView.as_view('frequencies')
wellimages = WellImagesView.as_view('wellimages')
