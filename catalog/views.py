from django.shortcuts import render

# Create your views here.

from .models import Book, Author, BookInstance, Genre
from .models import InternPrjPawAllActivity, InternPrjPawDrillAct, InternPrjPawSeisAct, AccountInfo, Area
from .models import InternPrjMwPawAllActivity
def index(request):
    """
    View function for home page of site.
    """

    # Generate counts of some of the main objects
#    num_books=Book.objects.all().count()
#    num_instances=BookInstance.objects.all().count()
    # Available books (status = 'a')
#    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
#    num_authors=Author.objects.count()  # The 'all()' is implied by default.
    
#    genres=Genre.objects.count()
    #genres=Genre.objects.count()
#    genres=Genre.objects.get(name__exact='Horror')
#    genre_obj = genres.name


    #ARTHIT=InternPrjPawAllActivity.objects.filter(project_name__exact = 'ARTHIT')
    

#    num_account_info=AccountInfo.objects.all().count()

    
#    obj = AccountInfo.objects.all()
#    ARTHIT_obj = AccountInfo.objects.all()
    #dbQuery = AccountInfo.objects.order_by('?')[:4]
#    obj_query = obj#('scope')[0]
#    obj_scope = obj_query.values('account','type','scope')
#    account_info = obj.values('account','type','scope')
#    area_data = Area.objects.all().values('insert_date','name')
#    x = 'hello '


    #intern_prj_data = intern_prj.values('project_name','opr_status','longitude','latitude','percent_share','drilling_activity')

    intern_obj_num = InternPrjMwPawAllActivity.objects.all().count()
    intern_prj_data = InternPrjMwPawAllActivity.objects.all().values('project_name','latitude','longitude')
    intern_prj_list = InternPrjPawAllActivity.objects.values_list('project_name','longitude')

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        #context={'area_data':area_data,'account_info':account_info,'x':x,'obj_scope':obj_scope,'num_account_info':num_account_info,'genre_obj':genres,'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
        context={'intern_obj_num':intern_obj_num,'intern_prj_data':intern_prj_data,'intern_prj_list':intern_prj_list},
    )

    #'ARTHIT_obj':ARTHIT_obj,
    #'intern_prj_data':intern_prj_data,
    #'account_info_scope':account_info_scope,'account_info':account_info,