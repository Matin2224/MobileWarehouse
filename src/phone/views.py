from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .forms import BrandForm, MobileForm, SearchBrandForm, NationalitySearchForm, NotesForm
from .models import Brand, Mobile


class BrandAndMobileView(FormView):
    """
       A view for handling the creation of Mobile instances via a form.

       - Displays a form for adding mobile information.
       - Includes a secondary form for adding a brand (BrandForm).
       - Upon successful submission, the mobile information is saved, and a success message is displayed.
       """

    template_name = 'brand_and_mobile.html'
    form_class = MobileForm
    success_url = reverse_lazy('phone:brand_and_mobile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand_form'] = BrandForm()
        context['mobile_form'] = self.get_form()
        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Mobile saved successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return self.render_to_response(self.get_context_data(mobile_form=form))


class AddBrandView(CreateView):
    """
       A view for creating a new Brand instance using an AJAX-based request.

       - Returns a JSON response with the created brand's details upon success.
       - Returns a JSON response with error details if the form submission is invalid.
       """

    model = Brand
    form_class = BrandForm

    def form_invalid(self, form):
        errors = {}
        for field, error_list in form.errors.items():
            errors[field] = [{'message': error} for error in error_list]
        return JsonResponse({'success': False, 'errors': errors})

    def form_valid(self, form):
        brand = form.save()
        return JsonResponse({
            'success': True,
            'id': brand.id,
            'name': brand.name,
        })


class BrandListView(ListView):
    """
        A view for listing all Brand instances.

        - Allows filtering by the brand's nationality via a GET parameter.
        - Includes a form for searching brands by nationality.
        """

    model = Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'

    def get_queryset(self):

        nationality = self.request.GET.get('nationality')
        if nationality:
            return Brand.objects.filter(nationality__iexact=nationality)
        else:
            return Brand.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = NationalitySearchForm()
        return context


class MobileByBrandView(FormView):
    """
        A view for displaying mobiles belonging to a specific brand.

        - Accepts a brand name via a form.
        - Displays mobiles associated with the specified brand.
        - Returns an error message if the brand is not found.
        """

    template_name = 'mobile_by_brand.html'
    form_class = SearchBrandForm

    def form_valid(self, form):
        brand_name = form.cleaned_data['brand_name']
        brand = Brand.objects.filter(name__iexact=brand_name).first()
        if brand:
            mobiles = Mobile.objects.filter(brand=brand)
            return render(self.request, 'mobile_by_brand.html', {'mobiles': mobiles, 'form': form})
        else:
            return render(self.request, 'mobile_by_brand.html', {'error': 'Brand not found', 'form': form})


class MobileByMatchingCountryView(ListView):
    """
        A view for listing mobiles where the brand's nationality matches the assembling country.

        - Iterates through all mobiles and includes only those where the brand's nationality matches the assembling country.
        """

    model = Mobile
    template_name = 'mobile_matching_country.html'
    context_object_name = 'mobiles'

    def get_queryset(self):
        mobiles = Mobile.objects.all()
        return [mobile for mobile in mobiles if mobile.brand.nationality == mobile.assembling_country]


class MobileModelListView(ListView):
    """
        A view for listing mobiles based on the company's name.

        - Filters mobiles by the associated brand's name if a company name is provided via GET parameters.
        - Returns all mobiles with related brand information if no filter is applied.
        """

    model = Mobile
    template_name = 'mobile_model_list.html'
    context_object_name = 'mobiles'

    def get_queryset(self):
        company_name = self.request.GET.get('company_name', '').strip()

        if company_name:
            brand = Brand.objects.filter(name__iexact=company_name).first()
            if brand:
                return Mobile.objects.filter(brand=brand)
            else:
                return Mobile.objects.none()
        else:
            return Mobile.objects.select_related('brand').all()


class NotesSectionView(FormView):
    """
        A view for submitting notes through a form.

        - Displays a form for notes submission.
        - Prints the submitted notes to the console upon success.
        - Redirects to the home page upon successful submission.
        """

    template_name = 'notes_section.html'
    form_class = NotesForm
    success_url = '/'

    def form_valid(self, form):
        notes = form.cleaned_data['notes']
        print("Notes submitted:", notes)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class BrandWithMobilesListView(ListView):
    """
        A view for listing brands along with their associated mobiles.

        - Uses `prefetch_related` to optimize the query by preloading mobile data for each brand.
        """

    model = Brand
    template_name = 'brand_with_mobiles.html'
    context_object_name = 'brands'

    def get_queryset(self):
        return Brand.objects.prefetch_related('mobiles').all()
