from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Genre(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Book(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('book-detail', args=[str(self.id)])
import uuid # Required for unique book instances

class BookInstance(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('d', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='d', help_text='Book availability')

    class Meta:
        ordering = ["due_back"]
        

    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s (%s)' % (self.id,self.book.title)

class Author(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


#from django.db import models


class InternPrjPawAllActivity(models.Model):
    project_name = models.CharField(max_length=64, blank=True, null=True)
    opr_status = models.CharField(max_length=64, blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    percent_share = models.FloatField(blank=True, null=True)
    drilling_activity = models.CharField(max_length=2000, blank=True, null=True)
    production_activity = models.CharField(max_length=2183, blank=True, null=True)
    seismic_activity = models.CharField(max_length=3254, blank=True, null=True)
    activity_type = models.CharField(max_length=30, blank=True, null=True)
    point_size = models.CharField(max_length=1, blank=True, null=True)
    day = models.CharField(max_length=11, blank=True, null=True)
    project_code = models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.project_name

    class Meta:
        managed = True
        db_table = 'INTERN_PRJ_PAW_ALL_ACTIVITY'
    



class InternPrjPawDrillAct(models.Model):
    land_project = models.CharField(max_length=64, blank=True, null=True)
    day = models.CharField(max_length=10, blank=True, null=True)
    drilling_activity = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'INTERN_PRJ_PAW_DRILL_ACT'


class InternPrjPawSeisAct(models.Model):
    land_project = models.CharField(max_length=64, blank=True, null=True)
    activity_date = models.DateField(blank=True, null=True)
    seq = models.FloatField(blank=True, null=True)
    col1 = models.CharField(max_length=2028, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'INTERN_PRJ_PAW_SEIS_ACT'

class AccountInfo(models.Model):
    account = models.CharField(max_length=30)
    type = models.CharField(max_length=10)
    scope = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=2000, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    build = models.IntegerField(blank=True, null=True)
    model_version = models.CharField(max_length=64, blank=True, null=True)
    entitled = models.NullBooleanField()
    audit_history = models.NullBooleanField()
    audit_override = models.NullBooleanField()
    auto_guid = models.NullBooleanField()
    default_tablespace = models.CharField(max_length=30, blank=True, null=True)
    temporary_tablespace = models.CharField(max_length=30, blank=True, null=True)
    storage_configuration = models.CharField(max_length=30, blank=True, null=True)
    security_configuration = models.CharField(max_length=30, blank=True, null=True)
    coordinate_system = models.CharField(max_length=64, blank=True, null=True)
    transform_wgs84 = models.CharField(max_length=64, blank=True, null=True)
    vertical_reference = models.CharField(max_length=64, blank=True, null=True)
    unit_system = models.CharField(max_length=30, blank=True, null=True)
    owner = models.CharField(max_length=30)
    create_date = models.DateField(blank=True, null=True)
    modify_date = models.DateField(blank=True, null=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.scope

    class Meta:
        managed = False
        db_table = 'ACCOUNT_INFO'


class Area(models.Model):
    insert_date = models.DateField(blank=True, null=True)
    insert_user = models.CharField(max_length=64, blank=True, null=True)
    produced_by = models.CharField(max_length=64, blank=True, null=True)
    sdat_label = models.IntegerField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=64, blank=True, null=True)
    existence_kind = models.CharField(max_length=64)
    guid = models.CharField(max_length=128, blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)
    version = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    original_source = models.CharField(max_length=64, blank=True, null=True)
    remarks = models.CharField(max_length=2000, blank=True, null=True)
    source = models.CharField(max_length=64, blank=True, null=True)
    bulk_coordinate_system_id = models.BigIntegerField(blank=True, null=True)
    bulk_data_id = models.BigIntegerField(blank=True, null=True)
    shape = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'area_'

class InternPrjMwPawAllActivity(models.Model):
    project_name = models.CharField(max_length=64, blank=True, null=True)
    opr_status = models.CharField(max_length=64, blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    percent_share = models.FloatField(blank=True, null=True)
    drilling_activity = models.CharField(max_length=2000, blank=True, null=True)
    production_activity = models.CharField(max_length=2183, blank=True, null=True)
    seismic_activity = models.CharField(max_length=3254, blank=True, null=True)
    activity_type = models.CharField(max_length=30, blank=True, null=True)
    point_size = models.CharField(max_length=1, blank=True, null=True)
    day = models.CharField(max_length=11, blank=True, null=True)
    project_code = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intern_prj_mw_paw_all_activity'