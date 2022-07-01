from django.http import HttpResponseRedirect

from commentapp.models import Comment


def comment_delete(request, pk):

    comment = Comment.objects.get(pk=pk)
    comment.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))