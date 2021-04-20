from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Disco
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Concat
from django.db.models import Q, Value


def index(request):
    return render(request, 'discos/index.html')


@login_required(redirect_field_name='login')
def home(request):
    discos = Disco.objects.all().order_by('artista')
    paginator = Paginator(discos, 20)

    page = request.GET.get('p')
    discos = paginator.get_page(page)

    return render(request, 'discos/home.html', {
        'discos': discos,
    })


def detalhes(request, disco_id):
    try:
        disco = Disco.objects.get(id=disco_id)
        return render(request, 'discos/detalhes.html', {'disco': disco})
    except:
        return render(request, 'discos/erro.html')


'''

    disco = get_object_or_404(Disco, id=disco_id)
        return render(request, 'discos/detalhes.html', {
            'disco': disco
        })
'''


def busca(request):
    termo = request.GET.get('termo')  # pegar o termo

    if termo is None or not termo:
        # raise Http404
        messages.add_message(
            request,
            messages.ERROR,
            'Campo termo não pode ficar vazio'
        )
        return redirect('index')

    campos = Concat('artista', Value(' '), 'album')
    discos = Disco.objects.annotate(banda_album=campos).filter(
        Q(artista__icontains=termo) | Q(album__icontains=termo) | Q(banda_album__icontains=termo))

    paginator = Paginator(discos, 5)  # Show 5 contacts per page.

    page = request.GET.get('p')
    discos = paginator.get_page(page)
    return render(request, 'discos/busca.html', {
        'discos': discos
    })
