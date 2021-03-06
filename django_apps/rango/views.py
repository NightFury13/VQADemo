from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page
from rango.forms import CategoryForm
from rango.forms import PageForm

def index(request):
	category_list = Category.objects.order_by('-name')[:5]
	context_dict = {'categories': category_list}

	return render(request, 'rango/index.html', context_dict)

def category(request, category_name):

	# Create a context dictionary which we can pass to the template rendering engine.
	context_dict = {}

	try:
		category = Category.objects.get(name=category_name)
		context_dict['category_name'] = category.name

		# Retrieve all of the associated pages.
		# Note that filter returns >= 1 model instance.
		pages = Page.objects.filter(category=category)

		# Adds our results list to the template context under name pages.
		context_dict['pages'] = pages
		# We also add the category object from the database to the context dictionary.
		# We'll use this in the template to verify that the category exists.
		context_dict['category'] = category
	except Category.DoesNotExist:
		# We get here if we didn't find the specified category.
		# Don't do anything - the template displays the "no category" message for us.
		pass

	# Go render the response and return it to the client.
	return render(request, 'rango/category.html', context_dict)

def add_category(request):
	# A HTTP POST?
	if request.method == 'POST':
		form = CategoryForm(request.POST)

		# Have we been provided with a valid form?
		if form.is_valid():
			# Save the new category to the database.
			form.save(commit=True)

			# Now call the index() view.
			# The user will be shown the homepage.
			return index(request)
		else:
			# The supplied form contained errors - just print them to the terminal.
			print form.errors
	else:
		# If the request was not a POST, display the form to enter details.
		form = CategoryForm()

	# Bad form (or form details), no form supplied...
	# Render the form with error messages (if any).
	return render(request, 'rango/add_category.html', {'form': form})

def add_page(request, category_name):

	try:
		cat = Category.objects.get(name=category_name)
	except Category.DoesNotExist:
		cat = None

	if request.method == 'POST':
		form = PageForm(request.POST)
		if form.is_valid():
			if cat:
				page = form.save(commit=False)
				page.category = cat
				page.views = 0
				page.save()
				# probably better to use a redirect here.
				return category(request, category_name)
		else:
			print form.errors
	else:
		form = PageForm()

	context_dict = {'form':form, 'category': cat}

	return render(request, 'rango/add_page.html', context_dict)

def like_category(request):

	cat_id = None
	if request.method == 'GET':
		cat_id = request.GET['category_id']

	likes = 0
	if cat_id:
		cat = Category.objects.get(id=int(cat_id))
		if cat:
			likes = cat.likes + 1
			cat.likes =  likes
			cat.save()

	return HttpResponse(likes)
