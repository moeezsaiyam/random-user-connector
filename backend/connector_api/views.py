from rest_framework.views import APIView  
from .models import User
from rest_framework.response import Response
from rest_framework import status

class UserView(APIView):
    """
    RESPONSE: 
    [“countries”: [{“name”: <country>, users: [{“name”: <userName>, “gender”: <gender>, “email”: <email>}]}]]
    """

    def get_queryset(self):
        """
        QUERYSET: Filter by countries and Order the records
        """
        query = {}
        countries = self.request.query_params.get("countries")
        if countries:
            query["nationality__in"] = countries.split(",")
        queryset = User.objects.filter(**query).order_by("nationality").values()

        return queryset

    def get(self, request):
        queryset = self.get_queryset()

        # Serialize the data in requied format
        countries = {}
        for q in queryset:
            if q["country"] not in countries:
                countries[q["country"]] = []

            countries[q["country"]].append({
                    "name": q["name"],
                    "gender": q["gender"],
                    "email": q["email"],
                })
                
        data = [{"name": country, "users":countries[country]} for country in countries]

        return Response({"countries": data},status=status.HTTP_200_OK)
