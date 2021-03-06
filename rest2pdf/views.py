"""
Views to provide downloadable pdf files from a Django project.

"""
from django.conf import settings
from django.http import HttpResponse
from django.template import loader, Context
from cStringIO import StringIO
from rst2pdf import createpdf
DEFAULT_RST2PDF_ARGUMENTS = {
    'breaklevel': 0,
    'breakside': 'any',
    }
def rst_to_pdf(request, queryset, paginate_by=None, page=None,
        allow_empty=True, template_name=None, template_loader=loader,
        extra_context=None, context_processors=None,
        template_object_name='objects', mimetype='text/pdf',
        style_sheets=['pdf.style'], file_name='file.pdf',
        rst_to_pdf_kwargs={}):
    """View for rendering data to a pdf via reStructured Text.
    Uses the same parameters as
    django.views.generic.list_datail.object_list,
    adding:

        style_sheets, a list of rst2pdf stylesheets,

        file_name, a default download file name.


    **Template:**

    ``template.rst``

    **Context:**

    Context is generatated and used internally in the view to produce
    the pdf file.

    **Response:**

    An HttpResponse containing a pdf file.

    """
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(mimetype=mimetype)
    response['Content-Disposition'] = (
        ''.join(['attachment; filename=', file_name]))

    # Context
    if extra_context is None:
        extra_context = {}
    queryset = queryset._clone()
    c = Context({template_object_name: queryset,
        })
    # Add extra _context items
    for key, value in extra_context.items():
        if callable(value):
            c[key] = value()
        else:
            c[key] = value
    # Get template
    if not template_name:
        model = queryset.model
        template_name = "%s/%s_list.rst" % (model._meta.app_label,
                model._meta.object_name.lower())
    t = template_loader.get_template(template_name)
    # Check for any settings.
    style_path = getattr(settings, 'RST2PDF_STYLESHEET_DIRS', [])
    # Create in-memory buffer for file
    string_buffer = StringIO()

    #
    # Build arguments for createpdf.RstToPdf()
    #
    kwargs = {}
    # First, default arguments
    kwargs.update(DEFAULT_RST2PDF_ARGUMENTS)
    kwargs['style_path'] = style_path
    # Next, arguments passed to the view
    kwargs['stylesheets'] = style_sheets
    # Finally, ``rst_to_pdf_kwargs``, so that it is authoritative
    kwargs.update(rst_to_pdf_kwargs)

    createpdf.RstToPdf(**kwargs).createPdf(
            text=t.render(c), output=string_buffer, compressed=True,
            )
    response.write(unicode(string_buffer.getvalue(), 'utf-8', 'ignore'))
    return response
