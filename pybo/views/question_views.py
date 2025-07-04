from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question, QuestionHistory


@login_required(login_url='common:login')
def question_create(request):
    """
    pybo 질문등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user  # 추가한 속성 author 적용
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_modify(request, question_id):
    """
    pybo 질문수정
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            QuestionHistory.objects.create(
                question=question,
                subject=question.subject,
                content=question.content,
            )
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_delete(request, question_id):
    """
    pybo 질문삭제
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')

@login_required
def question_restore(request, history_id):
    history = get_object_or_404(QuestionHistory, pk=history_id)
    question = history.question

    if request.user != question.author:
        messages.error(request, '복원 권한이 없습니다.')
        return redirect('pybo:detail', question.id)

    # 복원: 현재 질문 내용을 다시 히스토리로 백업
    QuestionHistory.objects.create(
        question=question,
        subject=question.subject,
        content=question.content,
    )

    # 질문 내용 복원
    question.subject = history.subject
    question.content = history.content
    question.save()

    messages.success(request, '이전 버전으로 복원되었습니다.')
    return redirect('pybo:detail', question.id)
