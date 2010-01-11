{% load rest2pdf_tags %}
{% autoescape off %}

.. header::

   {{ title }}

.. footer::

   ###Page###
.. raw:: pdf

   SetPageCounter 1 lowerroman

{% block heading %}{% if heading %}{{ heading|rst_heading:"=" }}{% else %}{{ title|rst_heading:"=" }}

:date: Last Updated: {{ document_date|date:"d M Y" }}

{% endif %}{% endblock %}
{% block content %}
.. contents:: Table of Contents


.. raw:: pdf

   PageBreak oneColumn
   SetPageCounter 1 arabic

{% if articles %}
{% for article in articles %}
.. This is a anchor tag for use in creating an index.
..  _{{ article.question }}:

{{ article.question|rst_heading:"-" }}

**Category:** {{ article.category }}

**Keywords:** {{ article.tags }}

**Posted:** {{ article.date_posted|date:"d-M-y" }}, Database ID: {{ article.id }}

{{ article.answer }}

{% endfor %}

{{ "Index"|rst_heading:"-" }}

If you use django-tagging with your models, you could add an index of tags,
with links to document content.

{% else %}
No articles.
{%endif %}
{% endblock %}
{% endautoescape %}