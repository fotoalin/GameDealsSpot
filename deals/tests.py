from django.template import Context, Template
from django.test import TestCase


class DealsPartialTestCase(TestCase):
    def test_deals_partial(self):
        template = Template(
            "{% include 'deals/snippets/deals_partial.html' with deals=deals %}"
        )
        context = Context({"deals": [{"title": "Deal 1"}, {"title": "Deal 2"}]})
        rendered = template.render(context)

        self.assertInHTML("Deal 1", rendered)
        self.assertInHTML("Deal 2", rendered)
