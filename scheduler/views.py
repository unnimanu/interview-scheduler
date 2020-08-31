from rest_framework.response import Response
from .models import Schedule
from rest_framework.views import APIView


class Scheduler(APIView):
    def get(self, request):
        interviewer_id = request.data.get('interviewer_id')
        candidate_id = request.data.get('candidate_id')
        interviewer_schedule = Schedule.objects.filter(user_id=interviewer_id).first()
        candidate_schedule = Schedule.objects.filter(user_id=candidate_id).first()
        interviewer_from_time = interviewer_schedule.start_time
        interviewer_to_time = interviewer_schedule.end_time
        candidate_to_time = candidate_schedule.end_time
        candidate_from_time = candidate_schedule.start_time
        interviewer_to_time += 1
        candidate_to_time += 1
        if interviewer_from_time and interviewer_to_time and candidate_from_time and candidate_to_time is not None:
            response = range_conversion(interviewer_from_time=interviewer_from_time,
                                        interviewer_to_time=interviewer_to_time,
                                        candidate_from_time=candidate_from_time, candidate_to_time=candidate_to_time)
            return Response(response)
        else:
            response = {'message': 'interview times not entered'}
            return Response(response)

    def post(self, request):
        id = request.data.get('id')
        start_time = request.data.get('start_time')
        end_time = request.data.get('end_time')
        interview_date = request.data.get('interview_date')
        try:
            Schedule.objects.create(user_id=id, start_time=start_time, end_time=end_time,
                                    interview_date=interview_date)
            return Response({'message': 'Created Interview Slots Successfully'})
        except:
            return Response({'message': 'Error while creating slots'})

    def put(self, request):
        id = request.data.get('id')
        schedule = Schedule.objects.get(user_id=id)
        schedule.start_time = request.data['start_time']
        schedule.end_time = request.data['end_time']
        schedule.interview_date = request.data['interview_date']
        schedule.save()
        return Response({'message': 'Interview Schedule updated Successfully'})


def range_conversion(interviewer_from_time, interviewer_to_time,
                     candidate_from_time, candidate_to_time):
    interviewer_slot = list(range(interviewer_from_time, interviewer_to_time))
    candidate_slot = list(range(candidate_from_time, candidate_to_time))
    slots = [slot for slot in candidate_slot if slot in interviewer_slot]
    available_slots = []
    number_of_slots = len(slots) - 1
    for time in range(number_of_slots):
        if (slots[time + 1] - slots[time]) == 1:
            available_slots.append([slots[time], slots[time + 1]])
    return available_slots
