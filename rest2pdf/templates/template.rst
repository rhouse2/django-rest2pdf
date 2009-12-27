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
{{ article.title|rst_heading:"-" }}

**Category:** {{ article.category }}

**Keywords:** {{ article.tags }}

**Posted:** {{ article.date_posted|date:"d-M-y" }}, Database ID: {{ article.id }}

{{ article.content }}

{% if article.resources.all %}
**Resources:**

{% for r in article.resources.all %}{{ r.name }} `<{{ r.link }}>`__
{% endfor %}
{% endif %}
{% endfor %}
{% else %}
No articles.
{%endif %}
{% endblock %}
{% endautoescape %}