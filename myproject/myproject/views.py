from django.shortcuts import render, redirect
from .models import Feedback

def submit_feedback(request):
    if request.method == 'POST':
        order_id = request.POST['order_id']
        rating = request.POST['rating']
        review = request.POST['review']
        feedback = Feedback(order_id=order_id, rating=rating, review=review)
        feedback.save()
        return redirect('menu')  
    return render(request, 'feedback_form.html')
