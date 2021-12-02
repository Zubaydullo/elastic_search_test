from books.models import Book
from django.conf import settings
from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl_drf.compat import KeywordField, StringField
from elasticsearch_dsl import analyzer

# Name of the Elasticsearch index
INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])

# See Elasticsearch Indices API reference for available settings
INDEX.settings(number_of_shards=1, number_of_replicas=1)

html_strip = analyzer(
    "html_strip",
    tokenizer="standard",
    filter=["standard", "lowercase", "stop", "snowball"],
    char_filter=["html_strip"],
)


@INDEX.doc_type
class BookDocument(Document):
    """Book Elasticsearch document."""

    id = fields.IntegerField(attr="id")

    title = StringField(
        analyzer=html_strip,
        fields={
            "raw": StringField(analyzer="keyword"),
        },
    )

    description = StringField(
        analyzer=html_strip,
        fields={
            "raw": StringField(analyzer="keyword"),
        },
    )

    summary = StringField(
        analyzer=html_strip,
        fields={
            "raw": StringField(analyzer="keyword"),
        },
    )

    publisher = StringField(
        attr="publisher_indexing",
        analyzer=html_strip,
        fields={
            "raw": StringField(analyzer="keyword"),
        },
    )

    publication_date = StringField()

    state = StringField(
        analyzer=html_strip,
        fields={
            "raw": StringField(analyzer="keyword"),
        },
    )

    isbn = StringField(
        analyzer=html_strip,
        fields={
            "raw": StringField(analyzer="keyword"),
        },
    )

    price = fields.FloatField()

    pages = fields.IntegerField()

    stock_count = fields.IntegerField()

    tags = StringField(
        attr="tags_indexing",
        analyzer=html_strip,
        fields={
            "raw": StringField(analyzer="keyword", multi=True),
            "suggest": fields.CompletionField(multi=True),
        },
        multi=True,
    )

    class Django(object):
        """Inner nested class Django."""

        model = Book  # The model associate with this Document
