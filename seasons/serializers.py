from rest_framework import serializers

from .models import Season



class SeasonSerializer(serializers.ModelSerializer):


    
    class Meta:
        model = Season

        fields = [

            "title",
            "slogan",
            "number",
            "numeral",
            "season_minted_nfts_count",
        ]