from django.urls import path
from .views import BrandAndMobileView, AddBrandView, BrandListView, MobileByBrandView, MobileByMatchingCountryView, \
    MobileModelListView, NotesSectionView, BrandWithMobilesListView

app_name = 'phone'

urlpatterns = [
    path('', BrandAndMobileView.as_view(), name='brand_and_mobile'),
    path('add-brand/', AddBrandView.as_view(), name='add_brand'),
    path('brands/', BrandListView.as_view(), name='brand-list-korea'),
    path('mobiles/by-brand/', MobileByBrandView.as_view(), name='mobile-by-brand'),
    path('mobiles/matching-country/', MobileByMatchingCountryView.as_view(), name='mobile-matching-country'),
    path('notes/', NotesSectionView.as_view(), name='notes-section'),
    path('mobiles/', MobileModelListView.as_view(), name='mobile-list'),
    path('brands-with-mobiles/', BrandWithMobilesListView.as_view(), name='brand-with-mobiles'),

]
