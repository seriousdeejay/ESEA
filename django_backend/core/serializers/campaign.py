from rest_framework import serializers

from ..models import Campaign, EseaAccount

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ['id', 'name', 'network', 'method', 'organisation_accounts', 'open_survey_date', 'close_survey_date']

    
    def create(self, validated_data):
        campaign = Campaign.objects.create(**validated_data)
        #print
        #for organisation in 
        return campaign
    
    def update(self, instance, validated_data):
        for organisation in instance.network.organisations.all():
            EseaAccount.objects.create(organisation=organisation, method=instance.method, campaign=instance)
        return instance
