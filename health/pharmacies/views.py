from material.frontend.views import ListModelView

from pharmacies.models import Drug


class DrugSearchView(ListModelView):
    """View for searching availability of a drug. Returns all (nearby) pharmacies with the drug and pricing.
    Would be good letting a user search  by;
    1. Proximity
    2. Price """
    model = Drug
