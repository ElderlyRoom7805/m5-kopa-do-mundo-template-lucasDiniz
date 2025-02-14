from rest_framework.views import APIView, Response, Request, status
from .models import Team
from django.forms.models import model_to_dict
from utils import data_processing
from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError


class TeamView(APIView):
    def post(self, request: Request) -> Response:
        try:
            data_processing(request.data)
        except NegativeTitlesError:
            return Response(
                {"error": "titles cannot be negative"}, status.HTTP_400_BAD_REQUEST
            )
        except InvalidYearCupError:
            return Response(
                {"error": "there was no world cup this year"}, status.HTTP_400_BAD_REQUEST,
            )
        except ImpossibleTitlesError:
            return Response(
                {"error": "impossible to have more titles than disputed cups"},
                status.HTTP_400_BAD_REQUEST,
            )

        team = Team.objects.create(**request.data)

        return Response(model_to_dict(team), status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        teams = Team.objects.all()
        teams_dict = []
        
        for team in teams:
            teams_dict.append(model_to_dict(team))

        return Response(teams_dict)