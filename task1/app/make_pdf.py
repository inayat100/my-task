from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from  xhtml2pdf import pisa
from django.conf import settings
def render_to_pdf(template_src,context_dic={}):
    template = get_template(template_src)
    html = template.render(context_dic)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")),result)
    
    try:
        with open(str(settings.BASE_DIR)+f'/media/{filename}.pdf','wb+') as myfile:
            pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")),myfile)
    except Exception as e:
        print(e)
        
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type='application/pdf')
    else:
        return None
def html_to_pdf(template_src,filename,context_dic={}):
    template = get_template(template_src)
    html = template.render(context_dic)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")),result)
    
    try:
        with open(str(settings.BASE_DIR)+f'/media/{filename}.pdf','wb+') as myfile:
            pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")),myfile)
    except Exception as e:
        print(e)
        
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type='application/pdf')
    else:
        return None