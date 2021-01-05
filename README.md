# blog_project
## Lab-27: Django Models
## Overview
Django has a powerful Object Relational Mapper that allows us to persist data using Python instead of SQL.

In this repo will build out a project with one model and wire up that model using Django Views.

## Feature Tasks and Requirements
* create blog_project project
* create blog app
* migrate data
* create Post model
* add title as a CharField with maximum length of 64 characters.
* add author ForeignKey related to Django’s built in user model with CASCADE delete option.
* add body TextField
* add model to admin
* modify Post model have user friendly display in admin
* create migrations and migrate data
* create a super user
* Add a few posts via Admin panel
* Addtemplates folder in root of project
* register templates folder in project settings
* create HomePageView
* extend ListView
* give a template of home.html
* associate Post model
* create home.html template
* use Django Templating Language to display each post’s title
* create base.html ancestor template
* add main html document
* use Django Templating Language to allow child templates to insert content
* update url patterns for app and project
* view home page and confirm posts showing properly
* add detail view
* link post_detail.html template
* associate Post model
* create post_detail.html template
* template should extend base
* content should display post title and body
* update app urlpatterns to handle detail view
* account for primary key in url
* add link in home page template to related post detail page
## Lab-28: Django CRUD and Forms
## Overview
Add full CRUD functionality to your bag of tricks by building a Django project that allows Creating, Reading, Updating and Deleting.

## Feature Tasks and Requirementsw
* Create BlogCreateView that extends appropriate generic view
associated url path is post/new/
* Create BlogUpdateView that extends appropriate generic view
associated url path is post/<int:pk>/edit/
* Create BlogDeleteView that extends appropriate generic view
associated url path is post/<int:pk>/delete/
