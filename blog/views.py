from django.shortcuts import render


posts =[
    {
        'author': 'fahad',
        'title': 'blog post 1',
        'date_posted': 'Agust 27, 2020'
    },
      {
        'author': 'adel',
        'title': 'blog post 2',
        'date_posted': 'may 23, 2020'
    }

]


def home(request):
    context ={
        'posts': posts
    }
    return render(request, 'blog/home.html', context)



def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})
